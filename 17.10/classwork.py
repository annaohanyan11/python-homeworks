class Student(object):
	def __init__(self, grade):
		self.__grade = grade

	def get_grade(self):
		return self.__grade

	def set_grade(self, new_grade):
		self.__grade = new_grade


a = Student(10)
print(a.get_grade())
a.__grade = 5
print(a.get_grade())
a.set_grade(9)
print(a.get_grade())				