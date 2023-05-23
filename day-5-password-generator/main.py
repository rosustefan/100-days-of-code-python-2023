#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the `PyPassword` Generator!\nMinimum password length is 12-characters.\n")
min_pass_len = 12
pass_len = 0
first_pass = True
while pass_len < min_pass_len:
    try:
        if first_pass == True:
            pass_len = int(input(f"How many characters-long would you like your new password to be?\n"))
        else:
            pass_len = int(input(f"Sorry, it has to be at least {min_pass_len}-characters-long.\nHow long would you like your password to be?\n"))
        first_pass = False
    except:
        print("Invalid input. Please enter a number.")

nr_letters = int(0.6 * pass_len)
nr_symbols = int(0.2 * pass_len)
nr_numbers = int(0.2 * pass_len)

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pass = ''
for letter in range(0, nr_letters):
    easy_pass += random.choice(letters)

for number in range(0, nr_numbers):
    easy_pass += random.choice(numbers)

for symbol in range(0, nr_symbols):
    easy_pass += random.choice(symbols)

# print(f"The easy level (not randomized) password is {easy_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass_list = list(easy_pass)
random.shuffle(pass_list)
hard_pass = ''.join(pass_list)

print(f"\nHere is your new password: {hard_pass}")
