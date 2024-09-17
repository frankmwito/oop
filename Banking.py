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
    
    def transfer(self, from_account_number, to_account_number ,transfer_amount = 0.00):
        from_account = None
        to_account = None
        transfer_amount = float(input("Enter the amount you want to transfer: "))
        # Find the source and destination accounts by account number
        for account in self.accounts:
          if account["number"] == from_account_number:
            from_account = account
          if account["number"] == to_account_number:
            to_account = account
    
        # Check if both accounts exist
        if from_account and to_account:
        # Check if there are sufficient funds in the source account
           if from_account["deposit"] >= transfer_amount:
            from_account["deposit"] -= transfer_amount  # Subtract from source account
            to_account["deposit"] += transfer_amount    # Add to destination account
            print(f"Transfer successful! ${transfer_amount:.2f} transferred from Account {from_account_number} to Account {to_account_number}.")
            print(f"New balance in Account {from_account_number}: ${from_account['deposit']:.2f}")
            print(f"New balance in Account {to_account_number}: ${to_account['deposit']:.2f}")
           else:
            print("Insufficient funds for the transfer.")
        else:
         print("One or both account numbers are invalid.")
        
    
    
person1 = Bank_accounts()

person1.add_account()
person1.transfer()
person1.get_account()