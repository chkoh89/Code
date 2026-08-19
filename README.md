# Code

A Python workspace for developing and evaluating backtests.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The Bloomberg `blpapi` package must be installed from Bloomberg's package
index, and Bloomberg Terminal or another authorized Bloomberg API session must
be running locally:

```powershell
uv pip install --python .venv\Scripts\python.exe --index-url https://blpapi.bloomberg.com/repository/simple/ blpapi
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
