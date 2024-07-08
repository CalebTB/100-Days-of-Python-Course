from math import gcd

strVar = "Hello World"
print(strVar)

# num1, num2 = int(input("Enter two numbers: ")), int(input("Enter two numbers: "))
# print(num1 + num2)

# print("A 'single quote' inside double quotes")
# print('A "single quote" inside double quotes')
# print("A newline is created with\nand now on new line")
# print("----------------------------------------------")
#
# str1, str2 = "Hello World", " ,Caleb"
# print(str1 + str2)
# print("----------------------------------------------")
#
# name = input("Enter your name: ")
# print("Hello " + name)
# # or
# strLength = len(input())
# print(strLength)
#
# city_grew = input("What is the name of the city you grew up in? \n")
# fav_pet = input("What was the name of your favorite dog? \n")
#
#
# print("Your band name should be: " + city_grew + " " + fav_pet)
str1 = "ABCABCD"
str2 = "ABC"

if (str1+str2) == (str2+str1):
    lengthOfCommonString = gcd(len(str1), len(str2))
    print(lengthOfCommonString)
    print(str1[0:lengthOfCommonString])

print("")
