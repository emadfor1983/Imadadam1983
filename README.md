# Imadadam1983

## Rock Paper Scissors Game
This repository includes a simple command-line game written in Python.
Run the game using:
```bash
python3 rock_paper_scissors.py
```

## Budget Control Tool
The repository also contains a command-line budget controller to help track
company finances. It stores budgets and transactions in a JSON file (default
`budget_data.json`) and supports the following commands:

```bash
# Set or update the budget for a category
python3 budget_control.py set-budget Marketing 5000

# Add income or expense transactions
python3 budget_control.py add-income Sales 15000 --description "Retainer" --date 2023-11-01
python3 budget_control.py add-expense Marketing 1200 --description "Ad campaign"

# Generate a budget report (optionally filtered by category)
python3 budget_control.py report
python3 budget_control.py report --category Marketing

# List all recorded transactions
python3 budget_control.py list
```

Use `--data-file` to point to a different storage file if needed.
