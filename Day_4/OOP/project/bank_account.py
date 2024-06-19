class BalanceException(Exception):
    pass
class Bankaccount:
    def __init__(self,initialAmount,accName) :
        self.balance=initialAmount
        self.name=accName
        print(f"\nAccount '{self.name}' created.\nBalance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=$'{self.balance:.2f}'")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("\nDeposit complete.")
        self.getBalance()

    def variableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n Sorry, account '{self.name}' only has a balance of $'{self.balance:.2f}'")
        
    def withdraw(self,amount):
        try:
            self.variableTransaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw Intrupted : {error}')

    def transfer(self,amount,account):
        try:
            print('\n**********\n\nBeginning Transfer..🚀') 
            self.variableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete!✅\n\n*********')
        except BalanceException as error:
            print(f'\nTransfer intrupted. ❌ {error}')

class IntrestRewardsAcct(Bankaccount):
    
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\nDeposit Complete.")
        self.getBalance()
    
class SavingsAcct(IntrestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount,acct_name)
        self.fee = 5
        
 
    def withdraw(self, amount):
        try:
            self.variableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
        
        



