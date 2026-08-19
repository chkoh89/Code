"""Small moving-average backtest example."""

from __future__ import annotations

import pandas as pd


def moving_average_returns(prices: pd.Series, window: int = 3) -> pd.Series:
    """Return strategy returns for a long-only moving-average signal."""
    if window < 1:
        raise ValueError("window must be positive")
    signal = prices.rolling(window).mean().shift(1) < prices
    return prices.pct_change().where(signal, 0.0).fillna(0.0)


def main() -> None:
    prices = pd.Series([100, 101, 99, 102, 104, 103, 106], name="close")
    returns = moving_average_returns(prices)
    print(f"Cumulative return: {(1 + returns).prod() - 1:.2%}")


if __name__ == "__main__":
    main()
