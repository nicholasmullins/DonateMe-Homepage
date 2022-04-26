

def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("\nWelcome to the Matrix: ", username.upper())
            return username
        print("\nInvalid password for:", username.upper())
        return ""            
    print("\nUsername not found. Please register")
    return ""

def register(database, username):
    if username in database:
        print("\nUsername already exists")
        return ""    
    print("\nThe username", username, "has been registered")
    return username
        
            



