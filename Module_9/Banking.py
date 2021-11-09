#Travis Nickerson
#Feb 20th 2021
#Module 9
#Goal 1: To have user input account and display their balance with fee and new balances
#Goal 2: To have user input account and diplay a balance below the minimum
#Goal 3: To ask user for saving account number and display balance and what it will
        # be after one year of interest at given interest rate

class BankAccount:
    """parent account"""
    def __init__(self, accountNum, balance):
        self.accountNum = accountNum
        self.balance = balance
    """withdraw"""
    def withdraw(self, withdrawAmount):
        print(f"You are withdrawing: ${withdrawAmount}")
        print(f"Your new Balance: ${newChecking.balance - withdrawAmount}")
    """deposit"""
    def deposit(self, depositAmount):
        print(f"You are depositing: ${depositAmount}")
        print(f"Your new Balance: ${newChecking.balance + depositAmount}")
    """balance"""
    def getBalance(self):
        print(f"Balance: ${newChecking.balance}")

# Adding a checking account with BankAccount inheritance
class CheckingAccount(BankAccount):
    """checking account"""
    def __init__(self, accounNum, balance):
        super().__init__(accounNum, balance)
        """ add in fee and min balance requirements"""
        self.fee = 5
        self.minBalance = 50
    """deduct fee from account"""
    def deductFee(self):
        print(f"Fee: ${self.fee}")
    """check min Balance and display if needed"""
    def checkMinBalance(self):
        print(f"Min Balance: ${self.minBalance}")
    """ check if current balance is below min balance after fee"""
    def newBalance(self):
        # calculate new balance
        newBal = newChecking.balance - self.fee
        print(f"New Balance: ${newBal}")
        # if balance is below min balance display how much to add to account
        if newBal < self.minBalance:
            print(f"Your account is below our Min Balance of ${self.minBalance}!")
            print(f"Please deposit ${self.minBalance - newBal} to bring your account to the ${self.minBalance} Minimum!")
    
    def isMinBalance(self):
        if newChecking.balance < self.minBalance:
            print(f"Your account is below our Min Balance of ${self.minBalance}!")
            print(f"Please deposit ${self.minBalance - newBal} to bring your account to the ${self.minBalance} Minimum!")

#Adding a Savings account with BankAccount inheritance
class SavingAccount(BankAccount):
    """savings account"""
    def __init__(self, accountNum, balance):
        super().__init__(accountNum, balance)
        self.interestRate = 0.02
    """ display interest rate as percentage"""
    def addInterest(self):
        print(f"Interest Rate: %{self.interestRate * 100}")
    """ display new balance with interest rate after year of savings"""
    def balanceWithInterest(self):
        print(f"Balance with interest: ${newSavings.balance * self.interestRate + newSavings.balance} after 1 year!")

# Only allow users to input int for account number
while True:
    try:
# Ask user for their Checking Account Num
        accountNumCheck = int(input("\nPlease enter your Checking Account Number: "))
        break
    except ValueError:
        print("\nPlease enter only numbers for your account!")

# *****DISPLAY CHECKING ACCOUNT DETAILS! THIS IS WHERE YOU CAN CHANGE THE BALANCE AMOUNT****

newChecking = CheckingAccount(accountNumCheck, 200)
print(f"\nChecking Account: {accountNumCheck}\nBalance: ${newChecking.balance}")
# Displaying Fee
newChecking.deductFee()
# Displaying New Balance after fee
newChecking.newBalance()
# Displaying current min balance for account
newChecking.checkMinBalance()
print()

# DISPLAYING AN EXAMPLE IF USER BALANCE IS TOO LOW
while True:
    try:
# Ask user for their Checking Account Num again
        accountNumCheck2 = int(input("\nPlease enter your Checking Account Number again: "))
# if the user inputs and differnt Account Num, Reprompt unitl it matches
        if accountNumCheck2 != accountNumCheck:
            print("\nYou did not match your Checking Account Number")
        else:
            break   
    except ValueError:
        print("\nPlease enter only numbers for your account!")
    

# Display account info when balance is too Low

# **** THIS IS WHERE YOU CAN CHANGE THE BALANCE*******

newChecking = CheckingAccount(accountNumCheck, 25)
print(f"\nChecking Account: {accountNumCheck2}\nBalance: ${newChecking.balance}")
# Display fee deduction
newChecking.deductFee()
# Display balance after fee
newChecking.newBalance()
# Check if balance is below min balance and display how much is needed to get back to the 
# minimum balance
newChecking.checkMinBalance()

print()

# SAVINGS ACCOUNT EXAMPLE WITH INTEREST RATE
while True:
    try:
        # Ask user for their Savings Acccount Num
        accountNumSavings = int(input("\nPlease enter your Savings Account Number: "))
        # Check if Savings Account num != Checking account num. 
        if accountNumSavings == accountNumCheck2:
            print(f"\nYour Savings Account Number cannot be your Checking Account Number!")
        else:
            break
    except ValueError:
        print("\nPlease enter only numbers for your account!")

#*** THIS IS WHERE YOU CAN ADJUST SAVINGS ACCOUNT****
newSavings = SavingAccount(accountNumSavings, 200)
print(f"\nSavings Account: {accountNumSavings}\nBalance: ${newSavings.balance}")
newSavings.addInterest()
newSavings.balanceWithInterest()






    
   