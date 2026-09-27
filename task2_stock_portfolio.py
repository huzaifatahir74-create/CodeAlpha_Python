stock_names = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN", "META", "NVDA"]
stock_prices = [180, 250, 420, 175, 190, 550, 120]

print("Stock Portfolio Tracker\n")

print("Enter name of stock from the following list you want to invest in:\n")
name = input("""
    AAPL
    TSLA
    MSFT
    GOOGL
    AMZN
    META 
    NVDA:\n""")

quantity = int(input("\nEnter Quantity you want to buy: "))

if name in stock_names:
    index = stock_names.index(name)
    price = stock_prices[index]
    total_investment = quantity * price

    print(f"\nCurrent price of {name} stock is {price}")
    print(f"\nYou bought {quantity} stocks of {name}")
    print(f"\nYour Total Investment is {total_investment}")

    file = open("stock_portfolio_results.csv", "a")
    file.write("Name,Quantity,Price,Total Investment\n")
    file.write(name + "," + str(quantity) + "," + str(price) + "," + str(total_investment) + "\n")
    file.close()
else:
    print("InValid Stock name")
