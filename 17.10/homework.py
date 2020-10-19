class Temperature():
	def __init__(self, curr_temp, goal_temp):
		self.__curr_temp = curr_temp
		self.goal_temp = goal_temp

	def get_temp(self):
		return self.__curr_temp

	def set_temp(self, new_temp):
		self.__curr_temp = new_temp

	def check(self):
		if self.__curr_temp == self.goal_temp:
			return True 
		else:
			return False



a = Temperature(27, 27)
print(a.get_temp())
a.set_temp(29)
print(a.get_temp())	
print(a.check())


b = Temperature(26, 26)
c = Temperature(23, 25)
d = Temperature(22, 21)
# s = 0

# def check1(self):
# 	if self.__curr_temp == self.goal_temp:
# 		s = s + 1

# 	return s			
 
# print(a.check1())
# print(b.check1())
# print(c.check1())

	






