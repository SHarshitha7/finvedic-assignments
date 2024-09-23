class Portfolio:
    def __init__(self):
        self.stocks = {}  
        self.stock_prices = {
            "AAPL": 150.00,
            "GOOGL": 2800.00,
            "MSFT": 300.00,
            "TSLA": 700.00
        }  

    def buy_stock(self, symbol, quantity):
        if symbol not in self.stock_prices:
            print(f"Stock symbol {symbol} does not exist.")
            return
        
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        total_cost = self.stock_prices[symbol] * quantity
        print(f"Buying {quantity} shares of {symbol} at ${self.stock_prices[symbol]} each. Total cost: ${total_cost:.2f}")

        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def sell_stock(self, symbol, quantity):
        if symbol not in self.stocks or self.stocks[symbol] < quantity:
            print(f"Insufficient shares of {symbol} to sell.")
            return

        total_revenue = self.stock_prices[symbol] * quantity
        print(f"Selling {quantity} shares of {symbol} at ${self.stock_prices[symbol]} each. Total revenue: ${total_revenue:.2f}")

        self.stocks[symbol] -= quantity
        if self.stocks[symbol] == 0:
            del self.stocks[symbol]  

    def get_portfolio(self):
        return self.stocks

if __name__ == "__main__":
    portfolio = Portfolio()

    while True:
        action = input("Enter action (buy, sell, portfolio, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'buy':
            symbol = input("Enter stock symbol: ").strip().upper()
            quantity = int(input("Enter quantity: "))
            portfolio.buy_stock(symbol, quantity)
        elif action == 'sell':
            symbol = input("Enter stock symbol: ").strip().upper()
            quantity = int(input("Enter quantity: "))
            portfolio.sell_stock(symbol, quantity)
        elif action == 'portfolio':
            print("Current Portfolio:")
            print(portfolio.get_portfolio())
        else:
            print("Invalid action. Please try again.")
