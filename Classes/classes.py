class Car:
	# Takes 3 parameters; "Self" means it is the current objext of the class we are working on. "Self" must always be included other wise it will not catch the properties of the object
	def __init__(self,make,model):
		self.make = make
		self.model = model
		self.noOfCylinders = 4

	def start(self): # Make a habit of creating "Self" functions inside of class
		print("Starting Car")

# self means the current objext that you are trying to create. self relates to the current object that you are creating.
# object is bmw which has a type Car.
bmw = Car('BMW','Series 3')
print(bmw.make)
print(bmw.model)
bmw.start() # Calls an unassigned function
print(bmw.noOfCylinders)

print("-" * 50)

toyota = Car('Toyota','Camry')
print(toyota.make)
print(toyota.model)

print("-" * 50)

class Person:
	# The middleName is empty because we don't don't know what the name is yet.
	def __init__(self,firstName,lastName,middleName = ""):
		self.firstName = firstName
		self.lastName = lastName
	def walk(self):
		print("Person is walking")
	def talk(self):
		print("Person is talking")
	# def sing(self, songName):
	# 	print("Person is singing" + songName)

person1 = Person('John','Doe')
person1.age = 23
person1.weight = 190
person1.walk()
person1.talk()

print("-" * 40)

# Class - Restaurant
# Attributes = Title, Description
# function = print description will include title + description

class Restaurant:
	def __init__(self,title,description):
		self.title = title
		self.description = description
		self.itemsOrdered = 0

	def print_description(self):
		print(self.title + self.description)

	def orderItem(self):
		self.itemsOrdered += 1

	def displayOrderStatus(self):
		print("We ordered" + str(self.itemsOrdered) + "And item was " + self.title)

rest1 = Restaurant('Olive Garden','Italian')
print(rest1.title)
print(rest1.description)
print(rest1.title + " contains " + rest1.description)
print(rest1.displayOrderStatus)

rest2 = Restaurant('McDonalds','junk food')
print(rest2.title)
print(rest2.description)
print(rest2.title + " contains " + rest2.description)
print(rest2.print_description)


print("-" * 40)

class Animal(object):
	def __init__(self,name,species):
		self.name = name
		self.species = species
	def walk(self):
		print("I am walking!")
	def run(self):
		print("I am running!")
	def eat(self):
		print("I am eatin!")

cat = Animal('Tom','Felion')
cat.eat()
cat.walk()

print("-" * 40)

# You are linking the characteristic of class "Animal" to the "Cheetah" class. The parent class is alive before you work on the parent class. "Super" means parent. Always call the parent(super) class first.
class Cheetah(Animal):
	def __init__(self):
		# Calling the "Anime" class initializer/constructor"
		super(Cheetah,self).__init__('Cheetah','Cats')
		self.name = ""

	def run(self):
		print("Cheetah is running super fast!")

ch = Cheetah()
ch.run()
ch.walk()
ch.eat()











