# --------------------------------------- CLASS -----------------------
# class Dog:
#     biology_class = 'Animal'
#     def __init__(self, name, weight, color):
#         self.name = name
#         self.weight = weight
#         self.color = color
#
#
#     def run(self):
#         return 'I can run!'
#
#
#     def get_name(self):
#         return f'Hello! My name is {self.name}'
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#
# dog1 = Dog('Brownie!', 3, 'My color is brown, but tail is white, WTF?')
# print(dog1.get_name())
# print(dog1.color)
# print(dog1.biology_class)
#
# dog2 = Dog('Markus', 11, 'Black')
# print(dog2.__dict__)
# print(dog2.color)
# print(dog2.get_name())
# dog2.name = 'Snoopy'
# print(dog2.get_name())
# print(dog2.__dict__)
#
#
# # ----------------------------- NASLEDOVANIE ---------------------------
# class Pitbull(Dog):
#     def __init__(self, name, weight, color, passport):
#         super().__init__(name, weight, color)
#         self.passport = passport
#
#     def give_a_paw(self):
#         return 'I can give a paw!'
#
#     def run(self):
#         return 'I can run fast!!!'
#
# dog3 = Pitbull('Carlos!', 23, 'white', 'Type 1')
# print(dog3.passport)
# print(dog3.get_name())

# ----------------------------- POLYMORPHISM ---------------------------
# (same method with different implementations)
# print(dog2.run())
# print(dog3.run())

# ----------------------------- ABSTRAKCIA ------------------------------
# ----------------------------- ENCAPSULATION (DATA + CODE) ---------------------------
#  ._ = PROTECTED,  .__ PRIVATE
# def set_name(self):

# -------------------------- GIT -----------------------
# File modification history control!!!!!!!!!!!

# def add(a, b):
#     return a + b
#
# def mult(a, b):
#     return a*b

# --------------- homework -----------

class Car:
    t_class = 'Transport'
    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model


    def run(self):
        return 'I can run for 5000 miles with one oil fill!'


    def get_name(self):
        return f'Hello! My owner calls me {self.name}'

    def set_name(self, new_name):
        self.name = new_name

car1 = Car('Leopard', 'Honda', 'Grey')
print(car1.get_name())
print(car1.make)
print(car1.t_class)

car2 = Car('"Runner"', 'Toyota', 'Camry')
print(car2.__dict__)
print(car2.make)
car2.name = '"Fast Runner"'
print(car2.get_name())



