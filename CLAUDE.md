# CLAUDE.md

This file provides guidance for Claude Code when working in this repository.

## Project Overview

This repository contains two standalone Python command-line tools:

- **`budget_control.py`** — A company finance tracker. Stores budgets and transactions in a JSON file and supports setting category budgets, recording income/expenses, generating reports, and listing transactions.
- **`rock_paper_scissors.py`** — A simple Rock Paper Scissors game in Arabic.

No third-party dependencies are required. Both scripts use only the Python standard library.

## Running the Tools

```bash
# Budget control tool
python3 budget_control.py set-budget Marketing 5000
python3 budget_control.py add-income Sales 15000 --description "Retainer" --date 2023-11-01
python3 budget_control.py add-expense Marketing 1200 --description "Ad campaign"
python3 budget_control.py report
python3 budget_control.py report --category Marketing
python3 budget_control.py list
python3 budget_control.py list --category Marketing

# Rock Paper Scissors game (interactive, Arabic prompts)
python3 rock_paper_scissors.py
```

Use `--data-file <path>` on the budget tool to point to a custom storage file (default: `budget_data.json`).

## Development

### Linting

```bash
flake8 budget_control.py rock_paper_scissors.py
```

### Testing

```bash
pytest
```

There are no test files yet. Add them as `test_*.py` files in the project root.

## Code Structure

### `budget_control.py`

- `Transaction` — dataclass representing a single income or expense record.
- `BudgetControl` — manages storage (JSON), budgets, and transactions. Key methods: `set_budget`, `add_transaction`, `get_category_summary`, `get_overall_summary`, `format_report`.
- `build_parser` / `main` — CLI entry point using `argparse`.

### `rock_paper_scissors.py`

- `play_round` — handles one round of user input and comparison.
- `main` — game loop that runs until the user quits.
