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

#-------------------------------------------------------
# Deposit Function
#-------------------------------------------------------

def deposit(name:str, amount:float):
    if amount<=0:
        raise ValueError("amount must be greated than 0")

    account=find_account(name)

    if not account:
        raise ValueError("account not Found")

    account["initial_balance"]+=amount

    account["transactions"].append({

    "type":"deposite",
    "amount":amount
    })

    return account["initial_balance"]


''' create_account("Reham", 1000)
new_balance = deposit("Reham", 500)
print("Deposit successful!")
print("New balance:", new_balance)'''
    

#-------------------------------------------------------
# Withdraw Function
#-------------------------------------------------------

def withdraw(name:str, amount:float):
    if amount<=0:
        raise ValueError("amount is inavlid")

    account=find_account(name)

    if not account:
        raise ValueError("account not Found")

    if amount>account["initial_balance"]:
        raise ValueError("insuficient balance")
    
    
    account["initial_balance"]-=amount

    account["transactions"].append({

    "type":"withdraw",
    "amount":amount
    })

    return account["initial_balance"]

'''create_account("Reham", 1000)
new_balance = withdraw("Reham", 500)
print("withdarw successful!")
print("New balance:", new_balance)'''

#-------------------------------------------------------
# Show Account Summary
#-------------------------------------------------------

def show_account(name:str):

    account=find_account(name)
    if not account:
        print("Account is not found")
        return
    
    print(f"\nAccount summary for {account['name']}")
    print(f"Current Balance: ${account['initial_balance']}")

    print ("Transaction:")

    if not account["transactions"]:
        print("No transaction yet")
    else:
        for transaction in account["transactions"]:
            print(f"- {transaction['type']} : ${transaction['amount']}")

'''
create_account("Reham", 1000)

withdraw("Reham", 500)
deposit("Reham", 100)

show_account("Reham")'''

