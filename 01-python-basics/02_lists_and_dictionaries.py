# --- MY PORTFOLIO: LISTS AND DICTIONARIES ---

# 1. Using a LIST to store a stock watchlist (ordered collection of data)
watchlist = ["AAPL", "TSLA", "NVDA", "MSFT"]

# 2. Using a DICTIONARY to store details of a specific asset (key-value pairs)
portfolio_asset = {
    "ticker": "AAPL",
    "company": "Apple Inc.",
    "price": 175.50,
    "shares": 15
}

# 3. Performing a calculation using the dictionary data
# Total Value = Price * Shares
portfolio_value = portfolio_asset["price"] * portfolio_asset["shares"]

# 4. Displaying the market data on the screen
print("=========================================")
print("QUANT PORTFOLIO DASHBOARD")
print("=========================================")
print("My Current Watchlist (List):", watchlist)
print("Top priority asset:", watchlist[0]) # Lists start counting at index 0
print("-----------------------------------------")
print("Asset Details (Dictionary):")
print("Company Name:", portfolio_asset["company"])
print("Ticker Symbol:", portfolio_asset["ticker"])
print("Current Price: $", portfolio_asset["price"])
print("Shares Owned:", portfolio_asset["shares"])
print("-----------------------------------------")
print("TOTAL POSITION VALUE: $", round(portfolio_value, 2))
print("=========================================")