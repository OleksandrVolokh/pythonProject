#OPERATORU SRAVNENIA
# (==) ravenstvo
# (!=) ne ravenstvo
import sys

# compare = 3 == 3
# print(compare)
# -----------------------------------------
# x = 5
# AND
# x > 3 and x < 8
# OR
# x > 3 or x < 8
# NOT
# not x > 5 not x == 5
# x > 3 and not x > 8
# EXAMPLEs
# x = 5
# print(x > 3 or x < 8)
# print(x > 3 and x > 8)

# a = 3
# print(a > 2 and a > 8)

# YSLOVNUE OPERATORU IF and ELSE
# EXAMPLE
# x = 3
# if x != 5:
#     print('Five')
# else:
#     print('Not Five')


# EXAMPLE
# x = 9
# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More Than Five')
# else:
#     print('Less than five')


# EXAMPLE
# age = int(input('Please, enter your age: '))
# if age >= 18:
#     print("Welcome")
# else:
#     print('Go home, baby')

# EXAMPLE
# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')
# try:
#         result = num1 / num2
#         print(f'Result = {result}')
# except ZeroDivisionError:
#         print('NO DIVISION WITH ZERO')

# EXAMPLE
# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/') or num1 > 5:
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('NO DIVISION WITH ZERO')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')
# Example
# try:
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
# except ValueError:
#     print('You entered not number')
#     sys.exit()
# -----------------------------------------------------
# CUKL WHILE

# num = 0
# while num < 5:
#     print(num)
#     num += 1
# num = num + 1
# ---------
# message = 'Hello'
# i = 1
# while i < 6:
#     print(i, message)
#     i += 1
#------------------------
# message = 'Hello'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)
# -------------------------

# for i in range(6):
#     print(i)
# -----------------------
# for i in range(1, 6, 2):
#     print(i)
# ---------------------
# for i in "Hello":
#     print(i)
# ------------------
# message = 'Hello'
# print(message[0: 5: 2])
# ----------------------
# i = 0
# x = 0
# while i < 5:
#     x += i
#     i += 1
#     # print(x)
#     print(f"x = {x}, i = {i}")
# ------------------------------------
# message = 'Hello'
# if message:
#     print(message)
# else:
#     print('The string is empty')
# --------------------------------
# message = ''
# if message:
#     print(message)
# else:
#     print('The string is empty')
# -----------------------------
# num = 11
# if  num%2:
#     print("Odd")
# else:
#     print("Even")
# --------------------
# def num(num1, num2):
#     return num1 * num2
#
# print(num(10, 5))
# print(num(37, 82))
# ---------------------------
# def num(num1, num2):
#      return num1 * num2
# start = num(10, 18)
# stop = 21
# step = 2
# for i in range(1, 19, 4):
#      print(i)
# -----------------------------







# ---------------------------------------------------------------------
# ------------------ SPLIT ---------------
# s = 'hello world'
# print(s.replace('l', '?',))

# s = 'hello world'
# print(s.replace(' ', ''))

# s = 'hello world'
# print(s.count('o'))

# w = 'Alex goldeneagle'
# w1 = '1, 2, 3, 4, 5'
# print(w1.split(',', maxsplit=2))

# ----------- JOIN ---------------
# w2 = w1.split(',')
# print(''.join(w1))

# w3 = '  123Hello123  '
# print(w3)
# print(w3.strip().strip('123'))

# ----------------- FIND -------------
# w4 = 'hello world'
# # print(w4.find('e'))
# print(w4.find('o', 2, 5))

# ---------------------- INDEX -------------------
# w4 = 'hello world'
# print(w4.find('l', 2, 5))
# print(w4.index('l', 2, 5))

# w5 = "NAme"
# print(w5.upper())
# print(w5.lower())

# w5 = "name world title"
# print(w5.title())

# print(w5.capitalize())
# print(w5.swapcase())

# w6 = 'qwerrty'
# w7 = ' Qwertyyu'
# w8 = '123'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())

# print(w8.isdigit())

# print(w8.isalpha())

# ------------IF ELSE ----------------

# a = int(input('Enter your number: '))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f'{a} division 2 and 10')
#     else:
#         print("delete by 2, but not 10")
# else:
#     print(f'{a} no delete by 2')


# q = int(input('Enter your grade: '))
# if q >= 90:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >= 70:
#     print(3)
# else:
#     print(2)

# if 10 < 20:
#     print(" Space with 8 digits")

# number = int(input("Enter the number: "))
# if number < 10:
#     print('1 digit Number')
# elif number < 99:
#     print(' 2 digit number')
# elif number < 999:
#     print(' 3 digit number')
# else:
#     print('big number')
#
# x, y = 55, 50
# s = x if x > y else y
# print(s)

# ---------------- WHILE --------------------
# c = 0
# while c < 5:
#      print('Hello')
#      c += 1

# text = int(input('Enter the number: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input('To coninue enter the number, if not, enter STOP: ')
# print(f'total equals {count}')

# --------------------- FOR ----------------------
# num = 10
# for i in range(1,num+1, 2):
#     print(i)
#
# string_1 = 'hello'
# for i in string_1:
#     print(i)
# string_1 = 'hello'
# for i in range(len(string_1)):
#     if string_1[i].islower():
#         print(i, string_1[i])

# --------------------------------     HOMEWORK # 2    ----------------------------

# health = int(input("Please enter your health level: "))
# if health <= 0:
#     print(False)
# else:
#     print(True)
# ---------------------
# num = int(input("Please enter your number: "))
# if num % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
# ----------------------
# year = int(input("Please enter the year: "))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("Even year")
#         else:
#             print("Odd year")
#     else:
#         print("Even Year")
# else:
#     print("Not even")

# OR

# year = int(input("Please enter the year: "))
# if not year%4 and year%100 or not year%400:
#     print("Even")
# else:
#     print("Odd Year")
# -----------------------------
# WHILE
# text = input("Please, enter your text: ")
# num = int(input("How many times? "))
# i = 1
# while i <= num:
#     print(text)
#     i += 1

# OR

# FOR
# text = input("Please, enter your text: ")
# num = int(input("How many times? "))
# for i in range(1, num +1):
#     print(text)
    # i += 1
# ---------------------------------
# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# operator = input('Enter operation:  \'+\', \'-\', \'/\', \'*\', \'%\': ')
# if operator not in '+-*/%':
#     print("NOT OPERATOR!")
#     sys.exit()
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print('NO ZERO DIVISION!')
#         sys.exit()
# elif operator == '+':
#     result = num1 + num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = num1/num2
# print(f'{num1} {operator} {num2} = {result}')


# ??????
# num1 = input('Please, enter first number: ')
# num2 = input('Please, enter second number: ')
# operator = input("Please enter operator: ")
# result = 0
# if operator == '+':
#     result = num1 + num2
#
# print(f'{num1} {operator} {num2} = {result}')