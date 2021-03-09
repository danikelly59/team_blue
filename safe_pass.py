"""
CSE 5408
"""

def pass_check(password):
    special_sym = [ '!','@','#','$','%','^','&','*']
    value = True
    
    if (len(password) < 7):
        print("Length should be at least 7 characters long")
        value = False
    
    if not any(char in special_sym for char in password):
        print("Password should have at least 1 special character")
        value = False
        
    if not any(char.isdigit() for char in password):
        print("Password should have at least 1 number")
        value = False
        
    if value:
        return value
    

print("Test out Password.")
password = input()
    
if(pass_check(password)):
    print("Password is Valid.")
else:
    print("Invalid Password. Please consider a different password.")