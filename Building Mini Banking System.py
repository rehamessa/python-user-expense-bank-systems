"""
Mini Banking System
 
A simple banking system that allows:
- Account creation
- Deposits
- Withdrawals
- Transaction tracking
- Account summary display
"""

#-------------------------------------------------------
# Simulate a Database
#-------------------------------------------------------

accounts=[]

# -------------------------------------------------
# Helper Function
# -------------------------------------------------

def find_account(name:str):

    for account in accounts:
        if account["name"].lower()==name.lower():
            return account
    return None

#-------------------------------------------------------
# Add Expense Function
#-------------------------------------------------------

def create_account(name:str, initial_balance:float)->bool:

    if initial_balance<0:
        raise ValueError("balance is invalid")
    
    if find_account(name):
        raise ValueError("account with this name already exist")

    account={
        "name":name,
        "initial_balance":initial_balance,
        "transactions":[]

    }

    accounts.append(account)
    return True


'''result = create_account("Reham", 1000)

print("Account created:", result)



print("\nAccounts:")
print(accounts) '''



