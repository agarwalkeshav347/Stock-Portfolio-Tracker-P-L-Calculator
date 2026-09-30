from data.stocks import NSE_STOCKS


def validate_ticker(ticker):
    if ticker not in NSE_STOCKS:
        raise ValueError("Stock is not listed in the supported stock database.")


def validate_shares(shares):
    if shares <= 0:
        raise ValueError("Number of shares must be greater than zero.")


def validate_price(price):
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
