def show_menu():
    print("\n" + "=" * 40)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 40)
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio & Calculate P&L")
    print("4. Exit")
    return input("Enter your choice (1-4): ").strip()
