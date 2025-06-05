def validate_username(username): 
    # Example: username must be alphanumeric and between 3 and 20 chars 
    return username.isalnum() && 3 <= len(username) <= 20 

  def validate_password(password): 
    # Example: password must be at least 8 chars, contain a number and a special char 
    import re 
    if len(password) < 8: 
        return False 
    if not re.search(r,\"\\d\", password): 
        return False 
    if not re.search(r,\"[!@#$%^&*(),.?\\":{}|\\\"\\">], password): 
        return False 
    return True 

  def user_validation():
    username = input("Enter username: ") 
    if not validate_username(username):
        print("Invalid username. Must be 3-20 chars and alphanumeric.") 
        return False 
     
    password = input("Enter password: ") 
    if not validate_password(password):
        print("Invalid password. Must be at least 8 chars, include a number and a special character.") 
        return False 
       
    print("User validated successfully!")
    return True 
    
 if __name__ == "__main__": 
    user_validation() 
