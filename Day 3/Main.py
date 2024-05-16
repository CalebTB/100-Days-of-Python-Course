# number = int(input("Enter a number: "))
#
#
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

bmi_height = float(input("Enter your height in m: "))
bmi_weight = float(input("Enter your weight in kg: "))

bmi_calc = bmi_weight / (bmi_height * bmi_height)

if bmi_calc < 35:
    if bmi_calc < 30:
        if bmi_calc < 25:
            if bmi_calc < 18.5:
                print("Your BMI is", bmi_calc)
                print("You're underweight")
            else:
                print("Your BMI is", bmi_calc)
                print("You're normal weight")
        else:
            print("Your BMI is", bmi_calc)
            print("You're slightly overweight")
    else:
        print("Your BMI is", bmi_calc)
        print("You're obese")
else:
    print("Your BMI is", bmi_calc)
    print("You're clinically obese")


year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("You are a leap year")
        else:
            print("You are not a leap year")
    else:
        print("You are a leap year")
else:
    print("You are not a leap year")
    
age = int(in)







