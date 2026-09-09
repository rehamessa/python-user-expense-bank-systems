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

# -------------------------------------------------------------------
# Registration Function
# -------------------------------------------------------------------

def create_user_account(name: str, email: str, password: str):
    try:
        validate_user_data(name,email,password)
        if any(user["email"]==email for user in registered_users):
            raise ValueError("An account with this email exists")

        user_record={
            "name":name,
            "password":password,
            "email":email,
            "status":"active",
        }

        registered_users.append(user_record)
        return user_record
    except ValueError as error:
        failed_registrations.append({"email":email,
                                     "error":str(error)})
        return None
    