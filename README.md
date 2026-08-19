# Code

A Python workspace for developing and evaluating backtests.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the example

```powershell
py -m backtest.example
```

## Run tests

```powershell
pytest
```

## Layout

- `src/backtest/`: reusable backtesting code
- `tests/`: automated checks
- `data/`: local market data; raw and processed data are ignored by Git
