# DICTIONARIES DICT {}

# console = {"nintendo": "wii"}  #nintendo = key  wii = value  KEY VALUE PAIR
# consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
# print(consoles["microsoft"])
# val = consoles["microsoft"]
# print(val)
# print("The " + consoles["sony"] + " 5 is Sony's newest gaming console.")

# KEY VALUES
# mohs_hardness = {9: "corumdum", 10: "diamond"}
# floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
# mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}
# print(mixed[10210])

# # DICTIONARIES ARE UNORDERED    -----   DICT{}  ------
# print([2, 4, 6] == [2, 4, 6])  # list has to be in a complete order
# print([2, 4, 6] == [6, 4, 2])

# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}     # dictionaries don't have to be in an exact order
# second = {2: 2.3, 1: 2.2, 3: 2.4, 0: 2.1}
# print(first == second)

# KEY ERROR
# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# print(first[3])

# IN AND NOT IN
# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# print(0 not in first)

# EX 94
# a = {1: 1.1, 2: 2.2, 3: 3.3, 4: 4.4, 5: 5.5}
# print(a[3])
# print(5 in a)
# print(3 not in a)

# DICTIONARY METHODS 1: .keys(), .values(), .items(), .get()
# .KEYS()

# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years.keys())
#
# for key in birth_years.keys():
#     print(key)

# .VALUES()
# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years.values())
#
# for val in birth_years.values():
#     print(val)

# .ITEMS()
# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years.items())
#
# for key, value in birth_years.items():
#     print(key, value)
#
# print(type(birth_years.keys()))
# print(type(birth_years.values()))
# print(type(birth_years.items()))

# TO DO IT IN A LIST
# print(list(birth_years.keys()))
# print(list(birth_years.values()))
# print(list(birth_years.items()))

# USING IN AND NOT IN ON VALUES
# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print("elizabeth" in birth_years.values())

# .GET()
# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# if 1975 in birth_years:
#     print(birth_years[1975])
# else:
#     print("1975 not in birth_years!")
# OR WITH .GET()
# print(birth_years.get(1975, "1975 not in birth_years!"))

# OTHER THINGS ABOUT DICTIONARIES
# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years)
# people = birth_years
# people[1969] = "madeline"
# print(birth_years)

# birth_years = {1994: "bill",
#                1969: "emily",
#                1982: "elizabeth",
#                2000: "turner"}
#
# print(len(birth_years))

# EX 97
# dic = {"Queen": "Bohemian Rhapsody",
#        "Bee Gees": "Stayin' Alive",
#        "U2": "One",
#        "Michael Jackson": "Billie Jean",
#        "The Beatles": "Hey Jude",
#        "Bob Dylan": "Like A Rolling Stone"}
# print(len(dic))
# for k in dic.keys():
#     print(k)
# print(dic.values())
# for key, value in dic.items():
#     print(key, value)
# print(dic.get("Promise of the Real", "Key 'Promise of the Real' is not found"))
# ---------------------------------------------------

# .fromkeys(), .pop(), .pop.items()

# # .FROMKEYS()
# ex_1 = {}.fromkeys(["address"], "Placid drive")
# print(ex_1)
#
# ex_1 = {}.fromkeys(["address"])
# print(ex_1)
#
# ex_1 = {}.fromkeys("addr", "Placid drive")
# print(ex_1)
# ----------
# .POP()
# ex_2 = {"make": "Honda", "model": "Civic", "year": "1996"}
# ex_2.pop("model")
# print(ex_2)

# ex_2 = {"make": "Honda", "model": "Civic", "year": "1996"}
# popped = ex_2.pop("model")
# print(ex_2)
# print(popped)
# -----------
# .POPITEMS()   REMOVES THE LAST ITEM
# ex_3 = {"name": 'Bob', "age": 38, "occupation": "accountant", "workplace": "H&R block"}
# ex_3.popitem()
# print(ex_3)

# EX 100
# a = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
# for key, value in a.items():
#     print(key, value)
#
# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# fast_food_items.pop("McDonald's")
# print(fast_food_items)
#
# fast_food_items.popitem()
# print(fast_food_items)
# ---------------------------


# .CLEAR()  .COPY()  .UPDATE()
# ex_1 = {1: "England", 2: "USA", 3: "Canada", 4: "Marocco"}
# print(ex_1)
# ex_1.clear()
# print(ex_1)

# .COPY()
# birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years)
# people = birth_years.copy()
# people[1969] = "madeline"
# print(birth_years)

# .UPDATE()
# city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
# population = {"population": 2930000}
# city_info.update(population)
#
# city_info["population"] = 3000000
# print(city_info)

# EX 103
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)
# a = internet_celebrities.copy()
# internet_celebrities.clear()
# print(internet_celebrities)
# print(a)

# .SETDEFAULT()

# computers = {"Google": "Chromebook", "Apple": "Macbook", "Microsoft": "Surface Pro"}
# if "Lenovo" not in computers:
#     computers["Lenovo"] = "ThinkPad"
#
# print(computers)

# OR
# computers.setdefault("Lenovo", "ThinkPad")
# print(computers)

# computers.setdefault("Apple", "<MacBook Pro")
# print(computers)

# DICT()
# empty = dict()
# print(empty)
#
# with_values = dict(a=1, b=2, c=3)
# print(with_values)
#
# with_values = dict(a1=1, b_=2, c_3=3)
# print(with_values)

family_1 = input("Enter family 1 members: ")
print(family_1)