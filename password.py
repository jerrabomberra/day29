# make a password generator - used LIST in python
import random

alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "l",
    "k",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "L",
    "K",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "%", "^", "&", "*", "(", ")", "-", "="]

print("---- Welcome to Password Generator ----------")

count_alpha = int(input("Enter the number of characters you want: "))
count_numbers = int(input("Enter the number of numbers you want: "))
count_symbols = int(input("Enter the number of symbols you want: "))

total_password = count_alpha + count_numbers + count_symbols
password = []

for i in range(count_alpha):
    password += random.choice(alpha)

for i in range(count_numbers):
    password += random.choice(numbers)

for i in range(count_symbols):
    password += random.choice(symbols)

random.shuffle(password)

print("\nGenerated password:", password)
print("Total length:", total_password)

final_password = "".join(password)
print("Your final password:", final_password)
print("\n\nYour password consists of:", total_password, "characters.")
print("Thank you for using our Password Generator!")
