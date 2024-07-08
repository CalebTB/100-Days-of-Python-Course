import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "="]

print("Welcome to Password Generator")
num_letters = int(input("How many letters would you like to generate? "))
num_numbers = int(input("How many numbers would you like to generate? "))
num_symbols = int(input("How many symbols would you like to generate? "))

password = []
final_password = ""
for i in range(num_letters):
    password.append(random.choice(letters))
for j in range(num_numbers):
    password.append(random.choice(numbers))
for k in range(num_symbols):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
password = "".join(password)
print("Your password is: ", password)
