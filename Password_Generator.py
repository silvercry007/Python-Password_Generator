import random
import string
import csv



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
    # Using random.choices() to generate a password of the desired length
    password = "".join(random.choices(characters, k=password_length))
    return password

password_length = int(input("Specify the lenght of the password :- "))
lowercase = str(input("Do you want to use lowercase? (T/F):- ").upper())
if lowercase == "T":
    use_lowercase = True
else:
    use_lowercase = False    
uppercase = str(input("Do you want to use uppercase? (T/F):- ").upper())
if uppercase == "T":    
    use_uppercase = True
else:
    use_uppercase = False   
digits = str(input("Do you want to use Digits? (T/F):- ").upper())
if digits == "T":
    use_digits = True
else:
    use_digits = False   
symbols = str(input("Do you want to use Symbols? (T/F):- ").upper())
if symbols == "T":
    use_symbols = True
else:
    use_symbols = False   
password = password_generator(password_length, use_lowercase, use_uppercase, use_digits, use_symbols)
print("Your password is:", password)

title = input("Title of Password:>>")
 
print("Title:" + title +"\nPassword:"+ password)

# # create the csv writer to create the file with the headings (Comment out if you want to add the title once)
# f = open('demo.csv', 'w')
  

# writer = csv.writer(f)
# header = ['Title','Password']
# writer.writerow(header)

with open("passwords.csv", "a", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
        # Writes the title
    writer.writerow([str(title),str(password)])



