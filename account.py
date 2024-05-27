class Account:
    def __init__ (self, number, pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        
    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
        
    
    #   View Account Details: Method to display the account owner's details and current balance.

    def account_details(self, owner, balance = 500):
        self.owner = owner
        self.balance = balance
        
        print(f"Dear {self.owner}, your current bank account balance is {self.balance}")
        
        
     
    # Change Account Owner: Method to update the account owner's information.
    def update_info(self, new_owner, balance = 500):
        self.new_owner = new_owner
        self.balance = balance
        
        print(f"The new owner of this account is {self.new_owner}")
    
    # Account Statement: Method to generate a statement of recent transactions.
    def generate_statement(self, amount):
        self.amount = amount
        
        print(f"amount withdrawn was {self.amount} last week")   
    
    
    
    
    # Set Overdraft Limit: Method to set an overdraft limit for the account.
    def overdraft(self, limit):
        if limit >= 500:
            self.limit = limit
            print(f"The overdraft limit is {self.limit}")
    

    # Interest Calculation: Method to calculate and apply interest to the balance.
    def apply_interest(self, rate, months, balance):
        self.rate = rate
        self.months = months
        self.balance = balance
        
        int = (balance * rate * months) / 100
        print(f"The interest to be applied is {int}")

    
    # Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze(self):
        self.account_frozen = True
        print(f"No transactions are allowed. The account is frozen")
        
    def unfreeze(self):
        self.account_frozen = False
        print("Transactions are allowed back. The account is unfrozen")


    # Transaction History: Method to retrieve the history of all transactions made on the account.
    
    def history(self):
        print(f"All transactions for the month")


    # Set Minimum Balance: Method to enforce a minimum balance requirement.
    def min_bal(self, bal):
        self.bal = bal
        bal == 500
        
        print(f"The minimum amount balance is {bal}")


    # Transfer Funds: Method to transfer funds from one account to another.
    def transfer_funds(self, account2, amount):
        if self.amount <= 500:
            print(f"Amount too low")
            
        else:
            self.account2 = account2
            self.amount = amount
            
            print(f"Transfer {self.amount} to {self.account2}")     
        


    # Close Account: Method to close the account and perform necessary cleanup.
    def close_account(self):
        if self.account_frozen == True:
            print(f"Account cannot be closed when frozen")
            
        else:
            self.balance = 0
            print(f"Account successfully cleaned")



