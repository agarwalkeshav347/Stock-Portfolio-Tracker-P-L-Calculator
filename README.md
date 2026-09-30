# Stock Portfolio Tracker

A modular Python CLI project for managing simulated stock holdings and calculating realized and unrealized profit/loss.

## Features

- Buy stocks
- Sell stocks
- Maintain weighted average purchase price
- Validate supported stock tickers
- Prevent invalid share quantities and prices
- Calculate realized P&L
- Calculate unrealized P&L
- Display portfolio summary
- Automated unit tests

## Technologies

- Python 3
- Object-oriented programming
- pytest
- Git/GitHub

## Project Structure

```text
src/
├── data/          # Stock reference data
├── models/        # Portfolio and transaction models
├── services/      # Business logic and P&L calculations
├── ui/            # CLI menu
└── utils/         # Validation helpers

tests/             # Unit tests
docs/              # Design documentation
report/            # Final project report
```

## Installation

```bash
python -m venv .venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the project root:

```bash
PYTHONPATH=src python src/main.py
```

On Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
python src/main.py
```

## Testing

```bash
pytest
```

## Project Scope

This is a portfolio tracking/simulation project. The current implementation asks the user to provide the current market price when calculating portfolio value; it does not claim to be a live market-data application.

## VITyarthi Alignment

The project is organized around:
- Three major functional modules: portfolio management, transaction management, and portfolio analytics/P&L
- Modular Python files
- Input validation and error handling
- Unit testing
- Documentation and design artifacts
- Git/GitHub-ready structure

## Future Enhancements

- Persistent database storage
- Transaction history
- CSV import/export
- Live market-data API integration
- Graphical dashboard
- Authentication and user accounts
