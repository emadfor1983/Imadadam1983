"""Command-line budget control tool for tracking company finances."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional


@dataclass
class Transaction:
    """Represents an income or expense transaction."""

    type: str
    category: str
    amount: float
    description: str = ""
    date: str = field(default_factory=lambda: date.today().isoformat())

    def to_dict(self) -> Dict[str, object]:
        return {
            "type": self.type,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "date": self.date,
        }

    @staticmethod
    def from_dict(data: Dict[str, object]) -> "Transaction":
        return Transaction(
            type=str(data["type"]),
            category=str(data["category"]),
            amount=float(data["amount"]),
            description=str(data.get("description", "")),
            date=str(data.get("date", date.today().isoformat())),
        )


class BudgetControl:
    """Manages budgets and transactions stored in a JSON file."""

    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.budgets: Dict[str, float]
        self.transactions: List[Transaction]
        self._load()

    def _load(self) -> None:
        if not self.storage_path.exists():
            self.budgets = {}
            self.transactions = []
            return

        data = json.loads(self.storage_path.read_text())
        self.budgets = {k: float(v) for k, v in data.get("budgets", {}).items()}
        self.transactions = [
            Transaction.from_dict(raw) for raw in data.get("transactions", [])
        ]

    def _save(self) -> None:
        payload = {
            "budgets": self.budgets,
            "transactions": [t.to_dict() for t in self.transactions],
        }
        self.storage_path.write_text(json.dumps(payload, indent=2, sort_keys=True))

    def set_budget(self, category: str, amount: float) -> None:
        if amount < 0:
            raise ValueError("Budget amount must be non-negative")
        self.budgets[category] = amount
        self._save()

    def add_transaction(
        self,
        *,
        transaction_type: str,
        category: str,
        amount: float,
        description: str = "",
        transaction_date: Optional[str] = None,
    ) -> Transaction:
        if transaction_type not in {"income", "expense"}:
            raise ValueError("transaction_type must be 'income' or 'expense'")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if transaction_date:
            try:
                datetime.fromisoformat(transaction_date)
            except ValueError as exc:
                raise ValueError(
                    "transaction_date must be in ISO format (YYYY-MM-DD)"
                ) from exc
        else:
            transaction_date = date.today().isoformat()

        transaction = Transaction(
            type=transaction_type,
            category=category,
            amount=amount,
            description=description,
            date=transaction_date,
        )
        self.transactions.append(transaction)
        self._save()
        return transaction

    def get_category_summary(self) -> Dict[str, Dict[str, float]]:
        summary: Dict[str, Dict[str, float]] = {}
        for transaction in self.transactions:
            category = transaction.category
            category_summary = summary.setdefault(
                category, {"income": 0.0, "expense": 0.0}
            )
            category_summary[transaction.type] += transaction.amount
        return summary

    def get_overall_summary(self) -> Dict[str, float]:
        totals = {"income": 0.0, "expense": 0.0}
        for transaction in self.transactions:
            totals[transaction.type] += transaction.amount
        totals["net"] = totals["income"] - totals["expense"]
        return totals

    def format_report(self, category: Optional[str] = None) -> str:
        category_summary = self.get_category_summary()
        overall_summary = self.get_overall_summary()

        lines = ["Budget Control Report", "======================", ""]
        if category:
            categories = [category]
        else:
            categories = sorted(category_summary.keys() | self.budgets.keys())

        if not categories:
            lines.append("No transactions or budgets available.")
        else:
            for cat in categories:
                summary = category_summary.get(cat, {"income": 0.0, "expense": 0.0})
                budget = self.budgets.get(cat)
                remaining = budget - summary["expense"] if budget is not None else None
                lines.append(f"Category: {cat}")
                lines.append(f"  Income:   ${summary['income']:.2f}")
                lines.append(f"  Expenses: ${summary['expense']:.2f}")
                if budget is not None:
                    lines.append(f"  Budget:   ${budget:.2f}")
                    lines.append(f"  Remaining:${remaining:.2f}")
                lines.append("")

        lines.append("Overall Totals")
        lines.append(f"  Income:   ${overall_summary['income']:.2f}")
        lines.append(f"  Expenses: ${overall_summary['expense']:.2f}")
        lines.append(f"  Net:      ${overall_summary['net']:.2f}")

        return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Budget control tool for managing company finances.",
    )
    parser.add_argument(
        "--data-file",
        default="budget_data.json",
        help="Path to the JSON file used for storage (default: budget_data.json)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    budget_parser = subparsers.add_parser("set-budget", help="Set or update a category budget")
    budget_parser.add_argument("category", help="Category name (e.g., Marketing)")
    budget_parser.add_argument("amount", type=float, help="Budget amount in dollars")

    income_parser = subparsers.add_parser("add-income", help="Record an income transaction")
    _add_transaction_arguments(income_parser)

    expense_parser = subparsers.add_parser("add-expense", help="Record an expense transaction")
    _add_transaction_arguments(expense_parser)

    report_parser = subparsers.add_parser("report", help="Display budget report")
    report_parser.add_argument(
        "--category",
        help="Limit the report to a single category",
    )

    list_parser = subparsers.add_parser("list", help="List recorded transactions")
    list_parser.add_argument(
        "--category",
        help="Filter transactions by category",
    )

    return parser


def _add_transaction_arguments(subparser: argparse.ArgumentParser) -> None:
    subparser.add_argument("category", help="Category name for the transaction")
    subparser.add_argument("amount", type=float, help="Transaction amount in dollars")
    subparser.add_argument(
        "--description",
        default="",
        help="Optional description for the transaction",
    )
    subparser.add_argument(
        "--date",
        help="Transaction date in ISO format (YYYY-MM-DD). Defaults to today.",
    )


def handle_set_budget(args: argparse.Namespace, controller: BudgetControl) -> None:
    controller.set_budget(args.category, args.amount)
    print(f"Budget for '{args.category}' set to ${args.amount:.2f}.")


def handle_add_income(args: argparse.Namespace, controller: BudgetControl) -> None:
    transaction = controller.add_transaction(
        transaction_type="income",
        category=args.category,
        amount=args.amount,
        description=args.description,
        transaction_date=args.date,
    )
    print(
        "Recorded income of ${0:.2f} for {1} on {2}.".format(
            transaction.amount, transaction.category, transaction.date
        )
    )


def handle_add_expense(args: argparse.Namespace, controller: BudgetControl) -> None:
    transaction = controller.add_transaction(
        transaction_type="expense",
        category=args.category,
        amount=args.amount,
        description=args.description,
        transaction_date=args.date,
    )
    print(
        "Recorded expense of ${0:.2f} for {1} on {2}.".format(
            transaction.amount, transaction.category, transaction.date
        )
    )


def handle_report(args: argparse.Namespace, controller: BudgetControl) -> None:
    print(controller.format_report(category=args.category))


def handle_list(args: argparse.Namespace, controller: BudgetControl) -> None:
    transactions = controller.transactions
    if args.category:
        transactions = [
            txn for txn in transactions if txn.category.lower() == args.category.lower()
        ]

    if not transactions:
        print("No transactions found.")
        return

    print("Transactions")
    print("============")
    for txn in transactions:
        sign = "+" if txn.type == "income" else "-"
        print(
            f"{txn.date} | {txn.category:<15} | {sign}${txn.amount:>9.2f} | {txn.description}"
        )


def main(argv: Optional[Iterable[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    controller = BudgetControl(Path(args.data_file))

    handlers = {
        "set-budget": handle_set_budget,
        "add-income": handle_add_income,
        "add-expense": handle_add_expense,
        "report": handle_report,
        "list": handle_list,
    }

    handler = handlers[args.command]
    handler(args, controller)


if __name__ == "__main__":
    main()
