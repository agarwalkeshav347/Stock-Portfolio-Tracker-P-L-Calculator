class Portfolio:
    """In-memory portfolio model."""

    def __init__(self):
        self.holdings = {}
        self.realized_pnl = 0.0

    def add_stock(self, ticker, shares, price):
        if ticker in self.holdings:
            old = self.holdings[ticker]
            old_cost = old["shares"] * old["avg_price"]
            new_cost = shares * price
            total_shares = old["shares"] + shares
            avg_price = (old_cost + new_cost) / total_shares
            self.holdings[ticker] = {
                "shares": total_shares,
                "avg_price": avg_price,
            }
        else:
            self.holdings[ticker] = {"shares": shares, "avg_price": price}

    def sell_stock(self, ticker, shares, price):
        if ticker not in self.holdings:
            raise ValueError(f"You do not own any shares of {ticker}.")
        owned = self.holdings[ticker]["shares"]
        if shares > owned:
            raise ValueError("Cannot sell more shares than you own.")

        avg_price = self.holdings[ticker]["avg_price"]
        pnl = (price - avg_price) * shares
        self.realized_pnl += pnl
        self.holdings[ticker]["shares"] -= shares

        if self.holdings[ticker]["shares"] == 0:
            del self.holdings[ticker]

        return pnl
