# list_1 = [5, 6, 8, 2, 1]
# list_2 = [[1, 2, 3], [4, 6], [8, 9, 3, 8]]
# list_3 = [10, 3.1888, "tree", False, [1, 2, 3]

# print(list("blah"))
# checked_list = [1, 2, 3, 4]
# print(8 in checked_list)

# EX 84
# mixed = [12, 3.89, True, "water", [3, 28, 74]]
# li_str = list('cheese')
# print("h" in li_str)
# print("e" not in li_str)
# print(li_str)
# -----------------------------------------------
# INDEXES AND LIST SLICING

# indexes = ["CARPET", "HARDWARE", "LINOLEUM"]
# print(indexes[1])

# indexes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(indexes[2] [1])

# ----------------NEGATIVE INDEXES --------------

# negative = [1, 2, 3, 4, 5]
# print(negative[-1])

# mixed = [False, 365, 4.24, "this is a string"]
# print(mixed[2] + 1.76)
# print("I have used \"" + mixed[3] + "\"  as an example too many times.")

# --------- LIST SLICING ---------

# sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sliced[:4])
# print(sliced[3:8])
# print(sliced[6:])

# ---------- REASSIGNING A LIST'S ITEMS -------------

# example = [2, 4, 6, 8, 0]
# print(example)
# example[3] = 10
# print(example)

# example = [2, 4, 6, 8, 0]
# print(example)
# example[1:4] = [3, 2, 1]
# print(example)

# example = [2, 4, 6, 8, 0]
# print(example)
# example[4:7] = [7, 6, 5]
# print(example)

# EX 87

# a = [[0, 2], [4, 6], [8, 10], [12, 14]]
# print(a[0])
# print(a[3][1])
# b = ["chair", "table", "desk", "lamp", "bed"]
# print(b[-5])
# print("Most people own at least " + str(a[0][1]) + " " + str(b[0] + "s."))
# c = [0.98, 8.76, 6.54, 4.32]
# print(c[1:])
# print(c[1:3])
# print(c[:2])

# ----------------- DEL AND LIST METHODS --------------------

# planets = ["Pluto", "Mars", "Earth", "Venus"]
# del planets[0]
# print(planets)

# planets = ["Pluto", "Mars", "Earth", "Venus"]
# planets.remove("Pluto")
# print(planets)

# colors = ["blue", "red", "blue", "red", "white", "black"]
# colors.remove("blue")
# print(colors)

# .APPEND()
# pets = ["cat", "dog", "parrot"]
# print(pets)
# pets.append("fish")
# print(pets)
#
# .INSERT()
# pets = ["cat", "dog", "parrot"]
# pets.insert(2, "turtle")
# print(pets)

# .SORT()
# num_list = [2.718, 4, -19, 10000, 0]
# print(num_list)
# num_list.sort()
# print(num_list)

# REVERSE = TRUE
# num_list = [2.718, 4, -19, 10000, 0]
# print(num_list)
# num_list.sort(reverse=True)
# print(num_list)

# USING .SORT ON MIXED DATA TYPE LISTS
# mixed = [False, 5.67, "string", -2]
# mixed.sort()

# ASCllbetical ORDER
# ASCllbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
# ASCllbetical.sort(key=str.lower)
# print(ASCllbetical)

# .INDEX()
# metals = ["cooper", "gold", "silver", "iron"]
# print(metals.index("silver"))

# numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
# print(numbers.index(3))

# .POP()
# bands = ["Queen", "Nirvana", "Offspring", "Radioheads"]
# end = bands.pop()  # or choose index for chosen bands for removal/reassigning
# print(bands)
# print(end)

# EX 90
# arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# del arctic_animals[4]
# arctic_animals.remove("elephant")
# arctic_animals.append("arctic fox")
# arctic_animals.insert(2,"snowy owl")
# arctic_animals.sort()
# print(arctic_animals)
# print(arctic_animals.index("reindeer"))
# print(arctic_animals.pop())

# LISTS AND STRINGS
# ex_1 = [1, 2, 3]
# ex_1[1] = 5
# print(ex_1)

# ex_2 = "123"
# ex_2 = "5"
# print(ex_2)

# ex_3 = "No, you can't."
# ex_4 = "Yes" + ex_3[3:11] + "!"
# print(ex_4)


# ex_5 = 3.14
# ex_6 = "coconut"
# ex_7 = ex_5
# ex_8 = ex_6
# print(ex_8)
# print(ex_7)

# ex_9 = [1, 2, 3, 4, 5]
# ex_10 = ex_9
# ex_10[2] = 4
# print(ex_9)
# print(ex_10)

# DEEP COPY FUNCTION
# import copy
# ex_12 = [1, 2, 3, 4, 5]
# ex_13 = copy.deepcopy(ex_12)
# ex_13[2] = 4
# print(ex_12)
# print(ex_13)

# ex_15 = ["bush",
#          "fern",
#          "tree",
#          "moss"]
# print(ex_15)

# ex_16 = 2 + \
#         4 + \
#         1
# print(ex_16)

# ex_17 = " The \
# Empi\
# re Str\
# ik\
# es Back"
# print(ex_17)