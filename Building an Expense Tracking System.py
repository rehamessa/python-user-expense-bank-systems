#--------------------------------------------------------
#simulated database
#---------------------------------------------------------

expenses=[]
#--------------------------------------------------------
#simulated database
#---------------------------------------------------------

def add_expense(amount:float, category:str, description:str)->dict:
    if amount<=0:
        raise ValueError("the amount is invalid")
    expense={
        "amount":amount,
        "category":category,
        "description":description
    }
    
    expenses.append(expense)
    return expense