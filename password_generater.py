import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user for password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length < 1:
        print("Password length must be greater than 0.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password: " + password)
except ValueError:
    print("Please enter a valid number for password length.")