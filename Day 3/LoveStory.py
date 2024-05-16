name_1 = str(input("Enter your name: "))
name_2 = str(input("Enter your name: "))

lowered_combined_name = name_1.lower() + name_2.lower()  # Makes all lowercase
t = lowered_combined_name.count("t")
r = lowered_combined_name.count("r")
u = lowered_combined_name.count("u")
e = lowered_combined_name.count("e")
first_num = t + r + u + e

l = lowered_combined_name.count("l")
o = lowered_combined_name.count("o")
v = lowered_combined_name.count("v")
e = lowered_combined_name.count("e")
second_num = l + o + v + e

score = int(str(first_num) + str(second_num))
print(score)
