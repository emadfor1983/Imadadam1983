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

## WhatsApp OSINT Tool

A command-line tool to query public WhatsApp account information via the
[whatsapp-osint RapidAPI](https://rapidapi.com/hub) endpoint.

### Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your RapidAPI key:
   ```bash
   cp .env.example .env
   # Edit .env and set RAPIDAPI_KEY=your_key_here
   ```

### Usage

```bash
python3 whatsapp_osint.py
```

You will be prompted to select one of the following query types:

| Option | Description |
|--------|-------------|
| 1 | Profile Photo — downloads and saves the profile picture |
| 2 | User Status — retrieves the about/status text |
| 3 | Business Verification — checks if the number is a WhatsApp Business account |
| 4 | Device Information — lists linked devices |
| 5 | Full OSINT Information — returns all available data |
| 6 | Privacy Settings — shows visibility settings for profile, last seen, etc. |

Enter the phone number with the country code but without the leading `+`
(e.g. `51916574069` for a Peruvian number).
