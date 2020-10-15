class Fruit:
	def __init__(self, name, color, price):
		self.name = name
		self.color = color
		self.price_kg = price
		self.kg = 0

	def presentation(self):
		text = "this fruit is {} it's colour is {} and price for kg is {}".format(self.name, self.color, self.price_kg)
		print(text)	

	def set_kg(self, kg):
		if kg > 0:
			self.kg = kg
		else:
			print("Wrong kg, kg remains {}".format(self.kg))		

Orange = Fruit("Orange", "orange", "500")
pomergranate = Fruit("Nur", "red", 1000)

print(Orange.price_kg)		
print(pomergranate.price_kg)
# pomergranate.kg = 500
# print(pomergranate.kg)
pomergranate.set_kg(-100)

Orange.presentation()
pomergranate.presentation()



class Car:
	def __init__(self, brand, model, year, colour):
		self.brand = brand
		self.model = model
		self.year = year
		self.colour = colour

	def presentation1(self):
		text  = "This is {} and its model is {}. It was made in {}. Its colour is {}".format(self.brand, self.model, self.year, self.colour)
		print(text)

Lexus = Car("Lexus", "RX", 2018, "White")	

Lexus.presentation1()	


			
