from models.portfolio import Portfolio
from utils.validators import validate_price, validate_shares, validate_ticker
from data.stocks import NSE_STOCKS


class PortfolioService:
    """Business operations for buying and selling stocks."""

    def buy_stock(self, portfolio: Portfolio, ticker: str, shares: int, price: float):
        ticker = ticker.upper()
        validate_ticker(ticker)
        validate_shares(shares)
        validate_price(price)
        portfolio.add_stock(ticker, shares, price)

    def sell_stock(self, portfolio: Portfolio, ticker: str, shares: int, price: float):
        ticker = ticker.upper()
        validate_ticker(ticker)
        validate_shares(shares)
        validate_price(price)
        return portfolio.sell_stock(ticker, shares, price)
