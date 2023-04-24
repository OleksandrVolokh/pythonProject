
# int_1 = 10
# int_float = 12.1
# int_bool = False
# int_1 = 12
# print(int_bool)
# ---------------------------------
# COMMENTS AND MATH OPERATIONS
# exponentiation 4 ** 4
# floor_division = 16 // 3
# modulo = 7 % 3
# ---------------------------------
# add_assign = 5
# add_assign += 7
# print(add_assign)

# summmed = 2 + 3
# print(summmed)
# divided = 1000 / 20

# ---------- PRINT -------------
# print(12345)
# print((4+9) * 3)

# ------ FLOATS --------
# print(1.23 + 2.81)
# ex2 = (123 + 281) / 100
# print(ex2)

# ex2 = (1.23 + 2.81)
# print(round(ex2, 1))

# penne = 16.68
# arrabiata = 6.98
# garlic_cloves = 16.78
# italian = 15.26
# artisan_baguettes = 3.00
# meatballs = 4.39
# subtotal = (round(penne + arrabiata + garlic_cloves + italian + artisan_baguettes + meatballs, 2))
# print(subtotal)

# -----------------------------------------------------------------------------------------
# ------------ STRINGS --------------
# a = 'This is a string'
# ex_8 = "orange"
# print(ex_8[2])
# print("apple"[3])

# ----- STRING SLICING -------------
# ex_10 = "apricots"
# print(ex_10[:3])
# print(ex_10[2:5])
# print(ex_10[3:])

# ------ CONCATENATION --------
# print("pecan" + " " + "pie")
#
# concatenated = "R2" + "-" + "D2"
# print(concatenated)
# print(concatenated[3])
# print(concatenated[1:4])

# EXERCISES
# a = "Just Do It!"
# print(a[10])
# print(a[5:7])
# print(a[8:])
# print(a[:4])
# print("Don't" + " " + a[5:])

# --------- TYPE---------STR -----------
# a = 23
# print(type(a))
# b = False
# print(type(b))

# a = str(True)
# b = str(5)
# c = 3.21
# print(type(a))
# print(type(b))
# print(type(c))

# -------- ESCAPE SEQUENCES -----------
# \t (for space)
# print("This\tis\tan\tapple")

# \n (for new lane)
# print("Hello,\nHow are You?")

# \' or \" (for quotes)
# print("\'White fish\', I said")

# EXERCISES
# a = 3.14
# print(type(a))
# a = str(3.14)
# print(a + " is a float")

# print("\'Hello, I'm Alex, it's nice to meet you!\'")

# print("*******\n ***** \n  ***  \n   *")

# ----------------- INPUT --------------

# name = input("Enter your name: ")
# print("Your name is " + name + ".")
# print(type(name))

# name = input('What is your name? ')
# quest = input('What is your quest? ')
# fav_color = input('What is your favorite color? ')
# print("So your name is " + name + ",Your quest is " + quest + ",Your favorite color is " + fav_color)

# ----------INT --------FLOATS
# user_int =int(input("please enter your integer: "))
# print(user_int)
# print(type(user_int))

# user_float = float(input("Please enter a float: "))
# print(user_float)
# print(type(user_float))

# user_int = int(input("Please enter your integer: "))
# print(user_int + 10)
# print(int3(user_int) + 10)

# ------------ FUNCTIONS --------------------
# def function_name():
#     print(2 + 2)
#
# function_name()

# def function_name(parameter):
#     print(parameter + 2)
#
# function_name(8)
# first_str = "The number "

# def function_name(p1, p2, p3):
#     print(p1 + str(p2) + p3)
#
#
# function_name(first_str, 5, " is an integer.")

# def default_example(num1=7, num2=8):
#     print(num1 * num2)
#
#
# default_example(4, 6)

# def default_example(num1=7, num2=8):
#     return num1 * num2
#
#
# print(default_example() + 44)

# EXERCISE
# def hello_world_printer():
#     print("Hello World")
# hello_world_printer()

# def name_printer(user_name):
#     print(user_name)
#
# name = input("Please enter your name: ")
# name_printer(name)

# length = int(input("Please enter you number, length"))
# width = int(input("Please enter your number, width"))
# height = int(input("Please enter your number, height"))
#
#
# def prism_vol(l, w, h):
#     return l * w * h
#
#
# print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")

# celsius = int(input("Please enter temperature in C: "))
#
#
# def fahrenheit (cel):
#     return(18 * cel +320) / 10
#
#
# print("The fahrenheit equivalent of " + str(celsius) + " degrees celsius is " + str(fahrenheit(celsius)) + ".")

# MODULES
# import random
#
# print(random.randint(1, 10))

# from random import randint
#
# print(randint(10, 20))

# from random import *
#
# print(random())

# EXERCISE
# from random import randint
# fuel = randint (10, 25)
# miles = randint(200, 400)
# print("The car will travel " + str(miles // fuel) + " miles per gallon")
# print("The car's fuel tank can hold " + str(fuel) + " gallons")
# print("The car can travel " + str(miles) + " miles on the full tank")

# --------- VAriable SCOPE ---------------

# example = "Hello World"       # GLOBAL
#
#
# def loc_ex():
#     example = "This is a string"          # LOCAL
#     return example
#
#
# print(example)
# print(loc_ex())



