# Class & Objects in python
# Class - Attributes and Behaviour

# Person -> Object Vani, Karan, vikram

# class person:
#     pass      #Empty class
#
# shreeram = person()  # object is created when you type class name with square braces
# shreeram


# 2nd method
# class Person:
#
# # Attribute -> Data members
# name = ram
# age = 26
# address = noida
# id = kg123
#
#
# # Behaviour -> Methods (not the functions)
# def talk(self):  # self: first argument of every function within the class
#     print(" can Talk")
#
#
# def walk(self):
#     print("I can walk faster")



# 3rd method --> correct method

class Person:
    def __init__(self, name, age, address, id):
        # Instance attributes
        self.name = name
        self.age = age
        self.address = address
        self.id = id

    # Methods
    def talk(self):
        print(f"{self.name} can talk.")

    def walk(self):
        print(f"{self.name} can walk faster.")

# Creating an instance of the Person class
ram = Person(name="Ram", age=26, address="Noida", id="kg123")

# Now you can call the methods on the instance
ram.talk()
ram.walk()