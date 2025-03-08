# Dictionary to store user credentials
user_credentials = {}

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Store in dictionary
user_credentials["Username"] = username
user_credentials["Password"] = password

# Display stored credentials
print("\nStored Credentials:")
print(user_credentials)