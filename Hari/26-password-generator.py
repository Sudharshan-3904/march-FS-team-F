import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_uppercase=True, use_lowercase=True):
    char_pool = ''
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character set must be enabled.")
    
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    print("Password Generator")
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    
    try:
        password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
