import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Define characters to use in password generation
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("=================================")
    
    try:
        length = int(input("Enter the length of the password you want to generate: "))
    except ValueError:
        print("Invalid input. Length should be a positive integer.")
        return
    
    if length <= 0:
        print("Invalid input. Length should be a positive integer.")
        return
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() in ['yes', 'y']
    use_digits = input("Include digits? (yes/no): ").lower() in ['yes', 'y']
    use_special = input("Include special characters? (yes/no): ").lower() in ['yes', 'y']
    
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"\nGenerated Password: {password}")

if __name__ == '__main__':
    main()
