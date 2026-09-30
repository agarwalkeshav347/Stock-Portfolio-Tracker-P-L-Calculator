from data.stocks import NSE_STOCKS
from models.portfolio import Portfolio
from services.portfolio_service import PortfolioService
from services.pnl_service import PnLService
from ui.menu import show_menu


def read_positive_int(prompt):
    value = int(input(prompt))
    if value <= 0:
        raise ValueError("Value must be greater than zero.")
    return value


def read_positive_float(prompt):
    value = float(input(prompt))
    if value <= 0:
        raise ValueError("Value must be greater than zero.")
    return value


def buy_flow(portfolio, service):
    ticker = input("Enter stock ticker (e.g., TCS, RELIANCE): ").strip().upper()
    service.validate_ticker if hasattr(service, "validate_ticker") else None
    if ticker not in NSE_STOCKS:
        raise ValueError("Stock is not listed, company not available.")

    print(f"Company Confirmed: {NSE_STOCKS[ticker]}")
    shares = read_positive_int("Enter number of shares to buy: ")
    price = read_positive_float("Enter price per share: ₹")
    service.buy_stock(portfolio, ticker, shares, price)
    print(f"Successfully bought {shares} shares of {ticker}.")


def sell_flow(portfolio, service):
    ticker = input("Enter stock ticker to sell: ").strip().upper()
    if ticker not in portfolio.holdings:
        raise ValueError(f"You do not own any shares of {ticker}.")
    owned = portfolio.holdings[ticker]["shares"]
    print(f"Selling shares of: {NSE_STOCKS.get(ticker, ticker)}")
    shares = read_positive_int(f"Enter number of shares to sell (You own {owned}): ")
    price = read_positive_float("Enter selling price per share: ₹")
    pnl = service.sell_stock(portfolio, ticker, shares, price)
    print(f"Sold {shares} shares of {ticker}.")
    print(f"Trade P&L: ₹{pnl:.2f}")


def view_flow(portfolio, pnl_service):
    if not portfolio.holdings:
        print("\nYour portfolio is currently empty.")
        print(f"Total Realized P&L: ₹{portfolio.realized_pnl:.2f}")
        return

    current_prices = {}
    for ticker in portfolio.holdings:
        current_prices[ticker] = read_positive_float(
            f"What is the current market price for {ticker}? ₹"
        )

    summary = pnl_service.portfolio_summary(portfolio, current_prices)

    print("\n" + "-" * 90)
    print(f"{'Ticker':<10} | {'Shares':<10} | {'Avg Price':<12} | "
          f"{'Current Price':<15} | {'Unrealized P&L':<15}")
    print("-" * 90)

    for row in summary["rows"]:
        print(f"{row['ticker']:<10} | {row['shares']:<10} | "
              f"₹{row['avg_price']:<11.2f} | "
              f"₹{row['current_price']:<14.2f} | "
              f"₹{row['unrealized_pnl']:<14.2f}")

    print("-" * 90)
    print(f"Total Invested: ₹{summary['total_invested']:.2f}")
    print(f"Total Current Value: ₹{summary['total_current_value']:.2f}")
    print(f"Total Unrealized P&L: ₹{summary['total_unrealized_pnl']:.2f}")
    print(f"Total Realized P&L: ₹{summary['total_realized_pnl']:.2f}")


def main():
    portfolio = Portfolio()
    portfolio_service = PortfolioService()
    pnl_service = PnLService()

    while True:
        choice = show_menu()
        try:
            if choice == "1":
                buy_flow(portfolio, portfolio_service)
            elif choice == "2":
                sell_flow(portfolio, portfolio_service)
            elif choice == "3":
                view_flow(portfolio, pnl_service)
            elif choice == "4":
                print("Exiting Portfolio Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except (ValueError, TypeError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
