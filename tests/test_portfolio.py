import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from models.portfolio import Portfolio


def test_buy_new_stock():
    portfolio = Portfolio()
    portfolio.add_stock("TCS", 10, 1000)
    assert portfolio.holdings["TCS"]["shares"] == 10
    assert portfolio.holdings["TCS"]["avg_price"] == 1000


def test_weighted_average_buy():
    portfolio = Portfolio()
    portfolio.add_stock("TCS", 10, 1000)
    portfolio.add_stock("TCS", 10, 1200)
    assert portfolio.holdings["TCS"]["shares"] == 20
    assert portfolio.holdings["TCS"]["avg_price"] == 1100
