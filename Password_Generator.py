import random
import string
def password_generator(password_length, use_lowercase, use_uppercase, use_digits, use_symbols):
    # Define the character sets for the password based on the input
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    # Use random.choices() to generate a password of the desired length
    password = "".join(random.choices(characters, k=password_length))
    return password
# Example usage
password_length = 16
use_lowercase = True
use_uppercase = True
use_digits = True
use_symbols = True
password = password_generator(password_length, use_lowercase, use_uppercase, use_digits, use_symbols)
print("Your password is:", password)