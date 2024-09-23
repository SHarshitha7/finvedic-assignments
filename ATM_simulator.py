import datetime

class ATM:
    def __init__(self, pin):
        self.pin = pin
        self.balance = 0.0
        self.transactions = []  

    def validate_pin(self, input_pin):
        return input_pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.datetime.now()
        })
        print(f"${amount} deposited successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            self.transactions.append({
                "type": "Withdrawal",
                "amount": amount,
                "date": datetime.datetime.now()
            })
            print(f"${amount} withdrawn successfully!")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def get_transaction_history(self):
        if not self.transactions:
            return "No transactions made."
        history = "Transaction History:\n"
        for transaction in self.transactions:
            history += f"{transaction['date']} - {transaction['type']}: ${transaction['amount']}\n"
        return history


def atm_simulator():
    atm = ATM("1234")  #default PIN as "1234"
    print("Welcome to the ATM Simulator!")
    
    input_pin = input("Enter your 4-digit PIN: ")
    
    if atm.validate_pin(input_pin):
        print("PIN validated successfully.")
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. View Transaction History")
            print("5. Exit")
            
            choice = input("Choose an option (1-5): ")
            
            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == '4':
                print(atm.get_transaction_history())
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid PIN. Access denied.")


if __name__ == "__main__":
    atm_simulator()
