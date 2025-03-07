import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase  # Always include lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        print("Error: No character set selected!")
        return None
    
    password = ''.join(random.choices(characters, k=length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_special)
        
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input! Please enter a valid number for length.")
