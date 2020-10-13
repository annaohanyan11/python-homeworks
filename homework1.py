class Circle:
	def __init__(self, radius):
		self.radius = radius
		pi = 3.14
		s = pi * pow(self.radius, 2)
		print(s)

	def perimeter(self, radius):
		self.radius = radius
		pi = 3.14
		p = 2 * pi * self.radius
		print(p)

a = Circle(2)
a.perimeter(3)		


class Target:
	def __init__(self):
		a = [10, 20, 10, 40, 50, 60, 70]
		target = 50
		for i in range(len(a)):
			for j in range(len(a)):
				b = a[j]
				if b + a[i] == target:
					print(i)
						

ls = Target()

class Person:
	def __init__(self):
		self.sex = input("enter male or female \n")

class Student(Person):
	def __init__(self, age, salary):
		Person.__init__(self)
		print(self.sex)
		self.age = age
		self.salary = salary

Simon = Student(19, 40000)	
print(Simon.salary)	



