# Function to register a user by taking username and password and storing them
def registerd_user():
    """
    Prompts the user to enter a username and password,
    and stores them in a dictionary.
    Returns the dictionary containing the user data.
    """
    user_data = {}  # Dictionary to store username and password
    username = input("Enter a username to register: ")
    password = input("Enter a password: ")
    user_data[username] = password  # Store the username and password
    print("Registration successful!\n")
    return user_data
# Function to login a user by checking entered credentials against stored data
def login_user(user_data):
    """
    Prompts the user to enter username and password,
    and checks them against the stored user data.
    Prints whether login is successful or failed.
    """
    username = input("Enter your username to login: ")
    password = input("Enter your password: ")
    # Check if username exists and password matches
    if username in user_data and user_data[username] == password:
        print("Login successful!")
    else:
        print("Login failed! Invalid username or password.")
# Example usage:
if __name__ == "__main__":
    # Register a user and store the data
    users = registerd_user()
    # Attempt to login with the stored data
    login_user(users)
