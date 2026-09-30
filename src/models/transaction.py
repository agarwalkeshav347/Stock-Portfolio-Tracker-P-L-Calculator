class Transaction:
    """Represents one buy or sell transaction."""

    def __init__(self, ticker, transaction_type, shares, price):
        self.ticker = ticker
        self.transaction_type = transaction_type
        self.shares = shares
        self.price = price
