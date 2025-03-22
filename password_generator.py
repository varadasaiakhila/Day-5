# to generate characters of a password in a randomised order
# letters - numbers - symbols
# easy method in order
# difficult = randomise the easy password

import random

easy_password = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", ":", ";", "'", "<",
           ">", ",", ".", "?", "/"]

no_of_letters = int(input("Enter the number of letters you want in your password "))
no_of_numbers = int(input("Enter the number of numbers you want in your password "))
no_of_symbols = int(input("Enter the number of symbols you want in your password "))

# adding letters
i = 0
while i < no_of_letters:
    letter = random.choice(letters)
    easy_password.append(letter)
    i += 1

# adding numbers
j = 0
while j < no_of_numbers:
    num = random.randint (0,9)
    easy_password.append(str(num))
    j += 1


# adding symbols
k = 0
while k < no_of_symbols:
    sym = random.choice(symbols)
    easy_password.append(sym)
    k += 1


# converting the list into a string using explicit type conversion
result = ''.join(easy_password)
print(result)

# printing the difficult password after shuffling the characters
random.shuffle(easy_password)
difficult_password_str = ''.join(easy_password)
print(f"Difficult Password: {difficult_password_str}")