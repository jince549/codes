import random



letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

print("Welcome to Password Generator")

password = ""
password_list = []

ltr_input = int(input("How many letters do you want to add in the password :"))
for i in range(ltr_input):
    ltr = random.choice(letters)
    password_list.append(ltr)
num_input = int(input("How many numbers do you want to add in the password :"))
for i in range(num_input):
    num = random.choice(numbers)
    password_list.append(num)
sym_input = int(input("How many symbols do you want to add in the password :"))
for i in range(sym_input):
    sym = random.choice(symbols)
    password_list.append(sym)

random.shuffle(password_list)

for i in password_list:
    password += i

print("Password is :", password)


