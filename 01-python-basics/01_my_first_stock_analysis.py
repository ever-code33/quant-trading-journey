# --- MY FIRST ANALYSIS ---

# 1. Variables (The information analyzed by the program)
ticker = "AAPL"
current_price = 175.50
target_buy_price = 180.00

# 2. Mathematical operation
price_difference = target_buy_price - current_price

# 3. Instructing Python to display the results on the screen
print("=========================================")
print("QUANT SYSTEM: MARKET MONITOR")
print("=========================================")
print("Stock to analyze:", ticker)
print("Current market price: $", current_price)
print("My target buy price: $", target_buy_price)
print("Price gap to target: $", round(price_difference, 2))
print("-----------------------------------------")

# 4. Conditional to take action
if current_price <= target_buy_price:
    print("SIGNAL: [ BUY ] - The stock is cheap or at its target price.")
    print("Action: Executing automated buy order...")
else:
    print("SIGNAL: [ HOLD ] - The stock is too expensive right now.")
    print("Action: Waiting for a better entry point.")

print("=========================================")