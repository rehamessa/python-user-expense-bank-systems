"""
User Registration System
 
A simple user registration module that demonstrates:
- Validation functions
- Exception handling
- Duplicate checking
- Basic in-memory storage
"""
#--------------------------------------------------------------------------
#simulated data base
#---------------------------------------------------------------------------------

registered_users=[]
failed_registrations=[]

# -------------------------------------------------------------------
# Validation Functions
# -------------------------------------------------------------------
def validate_name(name:str)->bool:
    return len(name)>=3

def validate_email(email:str)->bool:
    return "@" in email and "." in email
"""
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one digit"""
def validate_password(password:str)->bool:
    if len(password)>8:
        return False
    has_upper=any(char.isupper() for char in password)
    has_digit=any(char.isdigit() for char in password)
    return has_digit and has_upper
# -------------------------------------------------------------------
# Orchestrator Validation Function
# -------------------------------------------------------------------

def validate_user_data(name:str, email:str, password:str)->bool:
    if not validate_name(name):
        raise ValueError("Name must contain at least 3 characters")
    if not validate_email(email):
        raise ValueError("Email must contain '@' and '.'")
    if not validate_password(password):
        raise ValueError(  "Password must be at least 8 characters long and "
            "contain one uppercase letter and one digit")
    return True
    