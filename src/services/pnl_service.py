class PnLService:
    """Portfolio analytics and P&L calculations."""

    @staticmethod
    def realized_pnl(buy_price, sell_price, shares):
        return (sell_price - buy_price) * shares

    @staticmethod
    def unrealized_pnl(shares, average_price, current_price):
        return (current_price - average_price) * shares

    def portfolio_summary(self, portfolio, current_prices):
        total_invested = 0.0
        total_current_value = 0.0
        rows = []

        for ticker, data in portfolio.holdings.items():
            shares = data["shares"]
            avg_price = data["avg_price"]
            current_price = current_prices[ticker]
            invested = shares * avg_price
            current_value = shares * current_price
            pnl = current_value - invested

            total_invested += invested
            total_current_value += current_value
            rows.append({
                "ticker": ticker,
                "shares": shares,
                "avg_price": avg_price,
                "current_price": current_price,
                "unrealized_pnl": pnl,
            })

        return {
            "rows": rows,
            "total_invested": total_invested,
            "total_current_value": total_current_value,
            "total_unrealized_pnl": total_current_value - total_invested,
            "total_realized_pnl": portfolio.realized_pnl,
        }
