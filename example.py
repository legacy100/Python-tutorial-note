# print("Hello World")
# name= "paul"
# surname= "nwofor"
# age = 34

# name1="promise"
# surname1 = "abimbola"
# age1= 25

# print(name.title(), surname.title(), str(age), sep=", ")
# print(name1.title()+ "\n" + surname1.title(), "\n" + str(age1))
# print("Total: ", age + age1)


# name = "King"
# # times = name * 5

# print((name+ "\n") * 5 )

# print("Hello " + "world")
# x = "zander"
# y = 1
# print(x + str(y))
# print(x + " is " + str(y))

# x = "first name: zander"
# y = "surname: park"
# print(x + "\n" + y)

# x = input("Enter your name: ")
# y = str(input("Enter your age: "))
# print(f"my name is {x} and my age is {y}")

# slices = 12
# eaten = input("eaten: ")
# x = slices - int(eaten)
# print(f"remaining slice: {x}")

# currentYear = 2022
# birthYear = input("Input your year of birth: ")
# age = currentYear - int(birthYear)
# age += 1
# print(f"Your will be {age} next year")

# customer_name = input("Customers name: ")
# total_bill = input("Total bill: ")
# tax = float(total_bill)*10 / 100
# paid = input("amount received: ")
# balance = format(int(paid) - float(total_bill) - float(tax), '.2f')
# print(f"name: {customer_name} \nbill: ${total_bill} \ntax: ${tax} \npaid: ${paid} \nbalance: ${balance}")

# textInput = input("Enter your first name: ")
# print(f"Hello {textInput}")

# age = input("Enter your age: ")
# print(age)

# textInput = input("Enter your first name: ")
# numInput = input("Enter your age: ")
# print(f"{textInput} @ {int(numInput)}")

# age = int(input("Enter your age: "))
# requiredAge = 18
# expectedAge = requiredAge - age

# if age >= requiredAge:
#     print("You are Eligible")
# else:
#     print(f"Sorry, You will be Eligible in {expectedAge} years")

# x = 1
# y = 2
# if x < y: print("hello world")

# name = "paul"
# password = "zander"
# username = input("Enter Username: ")
# enterPass = input("Enter the password: ")

# if name == username and password == enterPass:
#     print(f"Congratulations {name} you have access")
# elif name == username and password != enterPass:
#     print("kindly check your password")
# else:
#     print("sorry you can not have access")

# bronze = 20
# silver = 40
# gold = 41

# user = int(input("Enter aquired coin: "))

# if user >= 0 and user <= 20:
#     print("Bronze")
# elif user >= 21 and user <= 40:
#     print("Silver")
# elif user >= 41 :
#     print("Gold")
# else:
#     print("Nigga go home")

# pizzaslice = 12
# userbite = int(input("Enter your pizza bite: "))

# if userbite >= 0 and userbite <= 12:
#     limit = pizzaslice - userbite
#     print(f"You have {limit} number of slice/bite left")
# else:
#     print(f"please put a valid bite between 0 to {pizzaslice} range")


# x = "HELLO \"world\" "
# print(x)

# y = ["yam", "beans","garri"]

# try:
#     z = y.index("beans")
# except ValueError:
#     print("There is an Error")

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# confirmPassword = input("Confirm your password: ")

# if confirmPassword == password and len(password) >= 8:
#     username1 = input("Enter your username: ")
#     password1 = input("Enter your password: ")

#     if username1 == username and password1 == password:
#         print(f"Welcome, {username}")

#     else:
#         print("sorry username or password do not match")

# else:
#     print("""
#     Re-Enter/choose your username and password again
#     your password must be more than 8 characters long
#     make sure you enter the same password twice
#     """)

# phoneNumber = input("Enter your phone number:")

# if len(phoneNumber) == 11:
#     selectNum = phoneNumber.replace(phoneNumber[0:8], "********")
#     print(selectNum)
# else:
#     print("The phone number entered is incomplete")

# fname = input("Enter your first name: ")
# sname = input("Enter your surname: ")
# result = fname[0].title()
# result1 = sname[0].title()
# print(result, result1)
# print(fname[0].upper(), sname[0].upper())
# print(fname[0].title(), sname[0].title())

# x = [10,1,12,42,51,1010,124,10,23,10,42,52,3,10]
# y = x.count(10)
# z = y * 10
# print(z)

# x = "A Free Python Beginners Course for 2021.This is a 10 part course slowly and progressively developing your skills through explanations, examples and code challenges.In this first module we focus on learning the basic underpinning skills used throughout this course, Print, Variables & Data Types."
# y = x.replace(".", ". ")
# print(y)

# x = ["Aarav", "Zander", "Kjetil"]
# y = input("Enter Your name: ")

# try:
#     x.index(y)
#     print('we have a match')
# except ValueError:
#     print("No match was found")

# for name in x:
#     if y == name:
#         try:
#             print(f"{y} is found in the database")
#         except ValueError:
#             print("Please check the name and try again")
#         break

# x = 1.7632828299
# print(round(x, 2))
# print(format(x, ".2f"))


# import math

# x = math.pi
# print(round(x, 2))

# price = float(input("Enter the price: "))
# discount = price * 0.20
# productPrice = price - discount
# print(round(productPrice, 2))


# import math as m

# x = float(input("Enter radius: "))
# area = m.pi*x*x
# print(format(area, ".2f"))
# print(round(y, 2))


# num1 = int(input("Enter first number: "))
# opt = input("+ - * /: ")
# num2 = int(input("Enter second number: "))

# if opt == "+":
#     result = num1 + num2
# elif opt == "-":
#     result = num1 - num2
# elif opt == "*":
#     result = num1 * num2
# elif opt == "/":
#     result = num1 / num2
# else:
#     print("Value unknown")
# print(result)


