class Arm_kitch:
	def __init__(self, dish_1, dish_2):
		self.dish_1 = dish_1
		self.dish_2 = dish_2

	def presentation(self):
		print(F"we have \n {self.dish_1} \n {self.dish_2}")	

class Georg_kitch:
	def __init__(self, dish_1, dish_2):
		self.dish1 = dish_1
		self.dish2 = dish_2	

	def presentation_georg(self):
		print(F"We have \n{self.dish1} \n {self.dish2}")


class Mixed_kitch(Arm_kitch, Georg_kitch):
	def __init__(self, dish_1, dish_2, dish1, dish2):
		Arm_kitch.__init__(self, dish_1, dish_2)
		Georg_kitch.__init__(self, dish1, dish2)

	def mixed_presentation(self):
		self.presentation()
		self.presentation_georg()


mixed_menu = Mixed_kitch("xorovac", "xash", "xinkali", "ajarakan")	
mixed_menu.mixed_presentation()				