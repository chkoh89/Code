import pandas as pd

from backtest.example import moving_average_returns


def test_moving_average_returns_are_series_aligned_to_prices():
    prices = pd.Series([100, 101, 102, 100])

    returns = moving_average_returns(prices, window=2)

    assert isinstance(returns, pd.Series)
    assert returns.index.equals(prices.index)
    assert returns.iloc[0] == 0.0
