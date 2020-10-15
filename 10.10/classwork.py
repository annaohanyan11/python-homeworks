class Text:

	def __init__(self, age):
		self.name = input("tell something \n")
		self.age = age

	def printing(self):
		print(self.name)
		print(self.age)


my_obj = Text(19)
my_obj2 = Text(20)

my_obj.printing()	
my_obj2.printing()		


class Rectangle:
	def __init__(self):
		self.a = int(input("enter a number"))
		self.b = int(input("enter a number"))
		self.c = int(input("enter a number"))

	def p(self):
		p = self.a + self.b + self.c
		print(p)

m = Rectangle()	
m.p()		


class Vehicle:
	def __init__(self, seats):
		self.seats = seats

class Car(Vehicle):
	def __init__(self, name, colour, seats):
		self.name = name
		self.colour = colour
		Vehicle.__init__(self, seats)
		self.real_seats = self.seats - 1


class Bicycle(Vehicle):
	def __init__(self, colour, seats):
		self.colour = colour
		Vehicle.__init__(self, seats)

bike = Bicycle("Red", 2)
lexus = Car("Lexus", "White", 5)

print(lexus.name, lexus.colour, lexus.seats, lexus.real_seats)	
print(bike.colour, bike.seats)	

print(lexus.__dict__)





