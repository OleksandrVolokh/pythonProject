# ---------------LISTS ---------------

#
# sentence = 'Python is awesome!'
# print(sentence.split(' ', maxsplit=1))

# my_list = [1, 'hello', 2.0, True, None]
# print(my_list[-2])
# print('Before', my_list)
# my_list[0] = 25
# # print(my_list)
# print('After', my_list)
# print(id(my_list))

# my_list = [1, 'hello', 2.0, True, None]
# sentence = 'Python is awesome!'
# my_list.append(sentence)
# print(my_list)
# print(len(my_list))

# my_list = [1, 'hello', 2.0, True, None]
# sentence = 'Python is awesome!'
# my_list.insert(0, sentence)
# print(my_list)
# print(len(my_list))

# my_list = [1, 'hello', 2.0, True, None, 1, 2]
# print(my_list.count(1))

# my_list = [1, 'hello', 2.0, True, None, 1, 2]
# print(my_list.index(None))
#
# my_list = [1, 'hello', 2.0, True, None]
# my_list1 = [1, 2, 3, 4, 5]
# print(sum(my_list1))
# print(min(my_list1))
# print(max(my_list1))

# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 7]]
# print(my_list1[-1][-3])

# -------FOR  LOOP WITH LIST ------
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num*5)
#
# new_l = [i for i in numbers if i%2==0]
# print(new_l)

# ----------  TUPLES ---------------------(KORTEZHU) --------
# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))
#
# name = 'Mark' ,
# print(name)
# print(type(name))

# my_tutle = ('apple', 'banana', 'cat')
# a, b, c = my_tutle
# print(a)
# print(b)
# print(c)

# my_tutle[0] = 'ananas'
# print(my_tutle)

# change TUTLE to LIST
# letters = list(my_tutle)
# letters[0] = 'ananas'
# print(letters)

# TUPLE FILTERING
# my_tutle = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tutle if isinstance(item, int)])
# print(result)
# ISINSTANCE  ----- IS CHECKING FOR THE CLASS
#
# my_tutle = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tutle if isinstance(item, int)])
# print(result)
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of my_tutle is: {len(my_tutle)}')
# print(f'Length of result is: {len(result)}')

# my_tutle = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tutle if isinstance(item, int)])
# print(result)

# ITERATE TUPLE WITH THE LOOP
# my_tutle = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tutle if isinstance(item, int)])
# print(result)
# for (index, item) in enumerate(my_tutle):
#     print(index, item)

#  ITERATE TUPLE WITH WHILE LOOP
# my_tutle = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tutle if isinstance(item, int)])
# print(result)
# i = 0
# while i < len(my_tutle):
#     print(i, my_tutle[i])
#     i += 1

# SWAPPING VARiaABLES
# a = 5
# b = 7
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')

# PASSING TUPLE AS AN ARGUMENT IN FUNCTION
# def sum_it(*args):    # * (raspakovka)
#     total = 0
#     print(args)
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))
# print(sum_it(4, 5, 10, 6, 20, 4, 6, 8, 28))

# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append(item*item)
#     return l
#
# print(func(2, 5, 6, 8, 10))

# # TUPLES UDEMY
# tuple_1 = ("a", "b", "c", "d", "e")
# tuple_2 = (2.718, False, [1, 2, 3])
# tuple_3 = (1, 1, 0, 0, 0)
#
# tuple_5 = tuple([3.14, 2.205, 10])
# tuple_6 = tuple("edcba")
# print(tuple_5)
# print(tuple_6)
#
# tuple_7 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(tuple_7[3])
# print(tuple_7[3:7])

# FIND OUT THE SIZE of FILE
# tuple_12 = (1, 3, 5)
# list_1 = [1, 3, 5]
# print(tuple_12.__sizeof__())
# print(list_1.__sizeof__())

# TUPLE LOOPING
# major_cities = ("Tokyo", "NewYork", "Paris", "Milan", "Odessa")
#
# for city in major_cities:
#     print(city)

# major_cities = ("Tokyo", "NewYork", "Paris", "Milan", "Odessa")
#
# count = 0
# while count < len(major_cities):
#     print(major_cities[count])
#     count += 1

# major_cities = ("Tokyo", "NewYork", "Paris", "Milan", "Odessa")
#
# backwards = len(major_cities) - 1
# while backwards >= 0:
#     print(major_cities[backwards])
#     backwards= -= 1

# TUPLE METHODS
# .count()
# repeat = (7, 3, 3, 3, 4, 4, 2, 2, 8)
# print(repeat.count(3))


# .index()
# int = (1, 5, 7)
# print(int.index(7))
# print(int.index(1))




# ---------------------------------- DICTIONARIES -----------------------------------
# dictionary = {key1: zna4enie, key2: zna4enie, ...}  # key, value
# my_dict = {}
# print(type(my_dict))

# my_dict = {
#     'Name': 'Anna',
#     'Last Name': 'Pavlova',
#     'age': '30',
#     'Department': 'IT'
# }
# print(my_dict)
# print(id(my_dict))
# print(my_dict['Name'])
# my_dict['Last Name'] = 'Smirnova'
# print(my_dict)
# print(id(my_dict))
# print(len(my_dict))

# TO ADD A KEY -------------------
# my_dict['Salary'] = 5000
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# keys = ['Name', 'salary', 'department']
# values = ['Alex', 10000, 'HR']
# employee = dict(zip(keys, values))
# print(employee)

# OR

# employee1 = dict(name='Joe', position='Electrician', salary='100K', department='Tech')
# print(employee1)


# ------------------ SETS( MNOZHESTVA ) my_set = {'A', 'B', 'C'}, FUNCTION my_set = set{}
#
# my_set = set([1,2,3,3,4,2,1,7,8])
# print(my_set)
#
# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 6, 100, 525}
# set3 = {1, 2, 3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set1.remove(1))
# print(set1)
# print(set1.add(8))
# print(set1)

# FROZENSET -------------------------- SET IS NOT CHANGING

# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)


# def sum_it(num1, num2, num3):
#     sum = num1 + num2 + num3
#     return sum

# print(sum_it(29,30,33))

# SETS UDEMY
# set_3 = set(range(1, 12, 2))
# print(set_3)

# set_5 = {3, 6, 9, 12, 15}
# print(12 in set_5)

# SET METHODS

# scifi = {"star trek", "star wars", "halo"}
# scifi.add("mass attack")
# print(scifi)

# .UNION()
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {6, 7, 8, 9, 10}
# set_3 = set_1.union(set_2)  # OR set_1 | set_2
# print(set_3)

# # SET COMPREHENSIONS
# comp_1 = {even+2 for even in range(2, 11, 2)}
# print(comp_1)
#
# comp_2 = {char.lower() for char in "ALLCAPS"}
# print(comp_2)




#   ---------------------- HOMEWORK --------------------------

3.1
# my_list = ('a', 'b', [1, 2, 3], 'd')
# print(my_list[-2])

# 3.2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#a
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
#
# #b
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])

# 3.3
# List и Tuple в Python — это классы структур данных Python. Список является динамическим, тогда как кортеж имеет
# статические характеристики. Это означает, что списки могут быть изменены, тогда как кортежи не могут быть изменены
# Для превращения списка в кортеж достаточно передать его в качестве аргумента функции tuple(). Обратная операция также
# является корректной.

# a = ['cat', 'dog', 'horse', 'cow']
# print(tuple(['cat', 'dog', 'horse', 'cow']))
# print(type(tuple(a)))

# 3.4
# family_1 = tuple(input("please enter family members: ").split(','))
# family_2 = tuple(input("please enter family members: ").split(','))
# if len(family_1) == len(family_2):
#     print("Equal")
# elif len(family_1) > len(family_2):
#     print("Family 1")
# else:
#     print("Family 2")

# 3.5
# movie = dict(title='Forrest Gump',
#              director='Zemeckis', year='1994',
#              budget='$682.2 mil',
#              main_actor='Tom Hanks',
#              slogan='Life is like a box of chocolates, you never know what you are going to get'
#              )
# # print(movie)
# print(movie.keys())
# print(movie.values())
# print(movie.items())
# print(type(movie))

# 3.6
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# # or
#
# my_dictionary = {'num1': 375, 'num2': 222, 'num3': -37, 'num4': 21}
# result = 0
# for x in my_dictionary:
#     result += my_dictionary[x]
# print(result)

# 3.7 Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list))

# 3.8 Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set2.intersection(set1))
# print(set1.symmetric_difference(set2))
# print(set2.issubset(set1))

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
#
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])

# def greet(name):
#     return f'Hello, {name} how are you doing today?'
# name = greet('Julia')
# print(name)

#
