# # print("Welcome to the rollercoaster!")
# # height = int(input("What is your height in cm? "))
# #
# # if height >= 120:
# #     age = int(input("enter the age"))
# #     if age <18:
# #         print("You can ride the rollercoaster pay 7$")
# #     else:
# #         print("You can ride the rollercoaster pay 12$")
# # else:
# #     print("Sorry you have to grow taller before you can ride.")
# #
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height>=120:
#     age = int(input("enter the age"))
#     if age >=1218:
#         print("it costs 12$")
#     elif age>12 and age<18:
#         print("it costs 7$")
#     elif age <=12:
#         print("it costs 5$")
#     else:
#         print("check the value ")
# else:
#     print("u are not ready to go")


height = float(input("enter the height "))
weight = float(input("enter the weight"))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("over weigh")
else:
    print("check the values")
