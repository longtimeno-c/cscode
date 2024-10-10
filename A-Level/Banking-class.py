class Banking:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

def main():
    print("Welcome to the Banking System")
    account_holder = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    
    account = Banking(account_holder, initial_balance)
    
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print(f"Deposited {amount}. New balance: {account.get_balance()}")
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
            print(f"New balance: {account.get_balance()}")
        elif choice == '3':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '4':
            print("Transaction history:")
            for transaction in account.get_transactions():
                print(transaction)
        elif choice == '5':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()