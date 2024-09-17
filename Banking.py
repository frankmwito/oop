# Banking System with multiple accounts

class Bank_accounts:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, initial_balance = 0.00):
        number_of_accounts = int(input("Enter your preffered number of accounts: "))
        for i in range(number_of_accounts):
            name = input(f"Enter name of your account {i+1}: ")
            account_number = int(input(f"Enter your account number {i+1}: "))
            initial_balance = float(input(f"Enter the deposit amount of money {i+1}: "))
            account = {"account_name" : name, "number" : account_number, "deposit" : initial_balance }
            self.accounts.append(account)
        print(f"You have created {number_of_accounts} accounts")
    
    def get_account(self):
        account_number = int(input("Enter your account number: "))
        for account in self.accounts:
            if account["number"] == account_number:
                print(f"Your account details are: {account}")
            else:
                print("Account not found")
    
    def transfer(self, transfer_amount = 0.00):
        account_number = input("account number you want to transfer money to: ")
        transfer_amount = float(input("Enter the amount you want to transfer: "))
        for account in self.accounts:
            if account["number"] == account_number and transfer_amount >= 0:
                initial_balance = initial_balance - transfer_amount
                account["deposit"] = initial_balance
                print(f"Transfer successful on {transfer_amount}, your new balance is {initial_balance}")
            else:
                print("Invalid account number or insuficient funds in account for transfer")
                
        
    
    
person1 = Bank_accounts()

person1.add_account()
person1.transfer()
person1.get_account()