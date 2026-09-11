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

#--------------------------------------------------------------
#Calculate Total Expenses
#---------------------------------------------------------------

def calculate_total_expenses()->float:
    total=0
    for expense in expenses:
        total+=expense["amount"]
    return total

#----------------------------------------------------------------------
#Calculate Total by Category
#----------------------------------------------------------------------

def calculate_total_by_category(category:str)->float:
    total=0
    for expense in expenses:
        if expenses["category"].lower()==category.lower():
            total+=expenses["amount"]
    return to


