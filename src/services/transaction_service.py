from models.transaction import Transaction


class TransactionService:
    """Creates transaction records."""

    @staticmethod
    def create_buy(ticker, shares, price):
        return Transaction(ticker, "BUY", shares, price)

    @staticmethod
    def create_sell(ticker, shares, price):
        return Transaction(ticker, "SELL", shares, price)
