Stock Portfolio Tracker & P&L Calculator 📈
Overview
The Stock Portfolio Tracker is a fully interactive, terminal-based FinTech application built entirely using core Python concepts. It allows users to simulate buying and selling shares, automatically calculates the Average Cost Basis for multiple purchases, and tracks both realized and unrealized Profit & Loss (P&L).
To ensure realistic data entry, the program includes a built-in validation engine containing over 300 real National Stock Exchange (NSE) tickers mapped to their full corporate names.
Note for Evaluators: This project was developed without the use of external data science or financial libraries (like pandas or yfinance). Complex financial calculations and data storage are handled entirely through standard Python dictionaries, iterative loops, and mathematical algorithms.
Features
NSE Ticker Validation: Users can only buy stocks listed in the internal NSE database. The system automatically fetches and confirms the full corporate name upon valid entry.
Average Cost Basis Algorithm: If a user buys the same stock at different price points, the system automatically recalculates the weighted average cost of the total position.
Realized P&L Tracking: When a stock is sold, the system calculates the profit or loss of that specific trade and adds it to a permanent "Realized P&L" ledger.
Unrealized P&L Engine: Calculates current standing by comparing the user's initial investment against real-time market prices provided by the user.
Zero External Dependencies: Runs on pure, out-of-the-box Python.
Environment Setup & Prerequisites
Because this project relies strictly on fundamental Python programming, the environment setup is highly lightweight.
Prerequisites:
Python: Version 3.6 or higher must be installed on your system.
Dependencies: None. (No pip install or external packages are required).
OS: Works on Windows, macOS, and Linux.
Installation & Configuration
Create the Project Directory:
Create a new folder on your computer to host the project.
Bash
mkdir stock_portfolio_project
cd stock_portfolio_project
Create the Python Script:
Inside the directory, create a new file named portfolio_tracker.py.
Add the Source Code:
Copy the complete Python code provided into portfolio_tracker.py and save the file. No API keys, environment variables (.env), or external configuration files are needed.
Execution Instructions
To run the application, open your terminal (or command prompt), navigate to the folder where you saved the script, and run the following command:
On Windows:
Bash
python portfolio_tracker.py
On macOS/Linux:
Bash
python3 portfolio_tracker.py
How to Use the Application (Walkthrough)
Upon execution, you will be greeted by the main menu inside an infinite while loop. Enter a number 1-4 to navigate.
1. Buying a Stock
Select 1 from the main menu.
Enter a valid NSE Ticker (e.g., TCS, RELIANCE, ZOMATO).
Validation: If you enter a random string (e.g., XYZ123), the system will block the transaction and output: "stock is not listed, company not available".
If valid, the system confirms the full company name (e.g., "Company Confirmed: Tata Consultancy Services Limited").
Enter the number of shares and your purchase price.
2. Selling a Stock
Select 2 from the main menu.
Enter the ticker of a stock you currently own.
Validation: The system will prevent you from selling shares you do not own, or attempting to sell more shares than you currently hold.
Enter the selling price. The system will immediately display the specific Profit or Loss from that trade and update your total Realized P&L.
3. Viewing Portfolio & Calculating P&L
Select 3 from the main menu.
The system will iterate through your current holdings. For every stock you own, it will pause and ask you for the current live market price.
Once all prices are entered, it generates a formatted tabular report showing your Total Invested amount, Current Value, Unrealized P&L (active positions), and Realized P&L (closed positions).
4. Exit
Select 4 to break the program loop and safely exit the application. (Note: Because data is stored in runtime dictionaries, exiting the program clears your portfolio).
