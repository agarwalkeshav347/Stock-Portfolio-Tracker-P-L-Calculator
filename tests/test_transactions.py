import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest
from models.portfolio import Portfolio


def test_sell_calculates_realized_pnl():
    portfolio = Portfolio()
    portfolio.add_stock("TCS", 10, 1000)
    pnl = portfolio.sell_stock("TCS", 4, 1200)
    assert pnl == 800
    assert portfolio.realized_pnl == 800
    assert portfolio.holdings["TCS"]["shares"] == 6


def test_cannot_oversell():
    portfolio = Portfolio()
    portfolio.add_stock("TCS", 5, 1000)
    with pytest.raises(ValueError):
        portfolio.sell_stock("TCS", 6, 1200)
