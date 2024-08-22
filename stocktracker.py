import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol] > shares:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol} from your portfolio.")
            elif self.portfolio[symbol] == shares:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from your portfolio.")
            else:
                print(f"You don't have that many shares of {symbol} in your portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def get_portfolio_value(self):
        total_value = 0.0
        print("\nCurrent Portfolio:")
        for symbol, shares in self.portfolio.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")["Close"][0]
            value = price * shares
            total_value += value
            print(f"{symbol}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

    def track_performance(self):
        print("\nTracking Portfolio Performance:")
        for symbol in self.portfolio:
            stock = yf.Ticker(symbol)
            history = stock.history(period="1y")
            print(f"\nPerformance for {symbol}:")
            print(history[["Close"]])

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Value")
        print("4. Track Stock Performance")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            portfolio.get_portfolio_value()
        elif choice == '4':
            portfolio.track_performance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
