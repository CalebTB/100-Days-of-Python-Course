# print("Welcome to Python Days 2!"[4])  # Output is o
#
# intToString = len(input("Enter a number: "))
# print(str(intToString))
# intToString = str(intToString)
# print(type(intToString))


# Program 2
current_bill = int(input("What is your current bill? ->"))
tip_percent = int(input("How much tip would you like to give to the person? 12%, 15%, 20% ->"))
num_split = int(input("How many people would you like to split the bill with? ->"))
total_bill_per_person = (current_bill + (current_bill * (tip_percent/100))) / num_split
print(f"The total bill is per person${total_bill_per_person:.2f}")
