class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
            return
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}")

    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    account = BankAccount()

    while True:
        operation = input("Enter operation (deposit, withdraw, balance, exit): ").strip().lower()
        if operation == 'exit':
            break
        elif operation == 'deposit':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif operation == 'withdraw':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif operation == 'balance':
            balance = account.get_balance()
            print(f"Current Balance: ${balance:.2f}")
        else:
            print("Invalid operation. Please try again.")
