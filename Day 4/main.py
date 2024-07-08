import random
#  Check Documentation for more functions

print("Printing Heads or Tails: ")
random_integer = random.randint(0, 1)
if random_integer == 1:
    print("Heads")
if random_integer == 0:
    print("Tails")

#  Lists
letters_of_vowels = ["a", "e", "i", "o", "u"]
print(letters_of_vowels)
print(letters_of_vowels[1])

letters_of_vowels.append("z")
print(letters_of_vowels)


#  Nested Lists
even_numbers = ["2", "4", "6", "8", "10"]
old_numbers = ["1", "3", "5", "7", "9"]

numbers = [even_numbers, old_numbers]
print(numbers)
