class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"You have withdrawn: {amount}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited: {amount}"
    
    def get_balance(self):
        return f"Your current balance is: {self.balance}"

# Simulate a simple banking system
def simulate_banking_system():
    name = input("Enter your name: ")
    initial_balance = float(input("Enter your initial balance: "))
    
    account = BankAccount(name, initial_balance)
    
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == '3':
            print(account.get_balance())
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the banking system simulation
simulate_banking_system()
