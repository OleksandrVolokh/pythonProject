# all_low = "there are no capitals here."
# print(all_low.upper())
#
# all_up = "ALL CAPITALS"
# print(all_up.lower())

# print("SHOUT!".lower())
# print("SHOUT!".lower().isupper())

# .isalpha()     ONLY LETTERS
# .isalnum ()    ONLY NUMBERS AND LETTERS
# .isdecimal ()  ONLY NUMBERS
# .isspace ()    ONLY SPACES
# .istitle ()    ONLY TITLECASE

# print("Batman".isspace())

# print("the great gatsby".title())
# print("the great gatsby".istitle())

# print("this is a string".startswith("this"))
# print("this is a string".endswith("g"))
# -------- JOIN ----------
# print("".join(["one", "two", "three"]))
# print(" ".join(["one", "two", "three"]))
# print("...".join(["one", "two", "three"]))
# print(", ".join(["one", "two", "three"]))

# ---------------SPLIT ------------
# print("Eggs, Milk, Waffles, Bacon".split(":"))

# Exercise_72

# mixed_case = "A Song of Ice and Fire"
# # print(mixed_case.isupper())
# # print(mixed_case.islower())
# # print(mixed_case.upper())
# # print(mixed_case.lower())
# print(mixed_case.istitle())
# title_case = mixed_case.title()
# print(title_case)
# print(mixed_case.startswith("A"))
# print(mixed_case.endswith("e"))
# words = mixed_case.split()
# print(words)
# print("".join(words).isalpha())

# --------    STRING METHODS 2    --------
# .rjust and .ljust
# print("hello world".rjust(15))
# print("hello world".ljust(15))

# print("hello world".rjust(15, "-"))
# print("hello world".ljust(15, "*"))

# .center()
# print("hello world".center(15, ":"))

# .strip(), .rstrip(), /lstrip()

# print("I had an exciting trip!!!11111")
# print("I had an exciting trip!!!11111".strip("1"))
# print("I had an exciting trip!!!11111".rstrip("1"))
# print("I had an exciting trip!!!11111".lstrip("1"))

# print("juice, bread, cheese, beef, bread".rstrip(", bread"))
# print("juice, bread, cheese, beef, bread".rstrip(", ed arb"))
# print("blueblueyellowblue".strip("eulb"))

# .replace()

# print("Good morning.".replace("morning", "afternoon"))

# EXERCISES
# 75
# the_string = "North Dacota"
# print(the_string.rjust(17))
# print(the_string.ljust(17, "*"))
# center_plus = the_string.center(16, "+")
# print(center_plus)
# print(the_string.lstrip("North"))
# print(center_plus.rstrip("+"))
# print(center_plus.strip("+"))
# print(the_string.replace("North", "South"))

# ---------------- len() ---------
# print(len("tree"))

# user_string = input("Please enter a string.")
# reversed = ""
#
# for item in range(len(user_string) -1, -1, -1):
#     reversed += user_string[item]
#
# print(reversed)

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

# def word_counter(words):
#     spaces_and_letters = ""
#     word_count = 1
#     for i in words:
#         if i.isalnum() or i.isspace() or i == "-" or i == "'":
#             spaces_and_letters += i
#     for j in spaces_and_letters:
#         if j == " ":
#             word_count += 1
#     return word_count
#
#
# print(word_counter(str_1))
# print(word_counter(str_2))
# print(word_counter(str_3))

# ------------------ FORMAT () ------------------------

# name = input("please Enter you name: ")
# degree = input("Please enter your degree: ")
# experience = input("How many years of experience: ")
# desire = input("Please enter you goals: ")
# # print("My name is " + name + " I have a Bachelor degree in " + degree + " I have " + experience + " years experience in manual testing " + " and my goal is " + desire)
# # OR
# print("{} majored in {}, has {} years experience, and has a desire to {}.".format(name, degree, experience, desire))

