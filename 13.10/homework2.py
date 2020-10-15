class Country:
	def __init__(self, name, continent):
		self.name = name
		self.continent = continent

	def t(self, name, continent):
		self.name = name
		self.continent = continent
		return self.name, self.continent


class Brand:
	def __init__(self, name, date):
		self.name = name
		self.date = date

	def presentation(self, name, date):
		return F"Our brand is called {self.name}, it was designed in {self.date}"


class Season:
	def __init__(self, name, temp):
		self.name = name
		self.temp = temp

	def presentation2(self, name, temp):
		return F"It's {self.name}. The average temperature is {self.temp}"


class Product(Country, Brand, Season):
	def __init__(self, name, type0, price, quantity):
		self.name = name
		self.type0 = type0
		self.price = price
		self.quantity = quantity

	def presentation3(self, name, type1, price, quantity):
		self.name = name
		self.type1 = type1
		self.price = price
		self.quantity = quantity

		print(F"This is {self.name}. It is {self.type1}. It costs {self.price}. We have {self.quantity} examples")


	def discount(self, price):
		self.price = price
		disc = int(input("enter the discount persentage \n"))
		newprice = price - (price * disc)/100
		print(newprice)

	def quantity(self, quantity):
		self.quantity = quantity
		newquantity = int(input("Enter the quantity of new examples"))
		print(quantity + newquantity)


shoes = Product("shoes", "sneakers", 67, 3)
shoes.presentation3("shoes", "sneakers", 67, 3)
shoes.discount(67)










			