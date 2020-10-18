class Hotel:
	def __init__(self, name, place, rooms, luxe_rooms, rooms_price, luxe_rooms_price):
		self.name = name
		self.place = place
		self.rooms = rooms
		self.rooms_price = rooms_price
		self.luxe_rooms = luxe_rooms
		self.luxe_rooms_price = luxe_rooms_price

	def presentation(self, name, place, rooms, rooms_price, luxe_rooms, luxe_rooms_price):
		print(F"Welcome to {self.name} hotel, which is located in {self.place}. We offer our guests {self.rooms} from casual rooms and {self.luxe_rooms} from luxe rooms. {self.rooms} price is {self.rooms_price} per night and {self.luxe_rooms} price is {self.luxe_rooms_price} per night.")

	def room_check(self, name, rooms, luxe_rooms):
		self.name = name
		self.rooms = rooms
		self.luxe_rooms = luxe_rooms
		# checking_room = input("enter a room, which you want to check(room1, room2 etc.) \n")
		# if self.name.rooms[checking_room] == "free":
		# 	print("Available")
		# else:
		# 	print("This room is busy")		

	def booking(self, name, rooms, luxe_rooms):
		self.name = name
		self.rooms = rooms
		self.luxe_rooms = luxe_rooms
		a.room = input("enter a room which you want to book \n ")
		self.rooms[a.room] = "busy"
			

Hilton = Hotel("Hilton", "Yerevan", {"room1": "free", "room2": "free"}, {"room3": "free", "room4": "free"}, 20, 150)

Hilton.presentation("Hilton", "Yerevan", "single room", "president room", 20, 150)	

Hilton.rooms["room1"] = "busy"
print(Hilton.rooms["room1"])
Hilton.room_check("Hilton", {"room1": "free", "room2": "busy"}, {"room3": "busy", "room4": "busy"} )


class Taxi:
	def __init__(self, name, car_type, price_for_tour):
		self.name = name
		self.car_type = car_type
		self.price_for_tour = price_for_tour

	def presentation(self, name, car_type, price_for_tour):
		print(F"Welcome to {self.name} Taxi Service. We offer our clients rides with {self.car_type} cars. The price is {self.price_for_tour}")

	def discount(self, name, surname, discount1, price_for_tour):
		self.name = name
		self.surname = surname
		self.discount1 = discount1
		self.price_for_tour = price_for_tour

		self.price_for_tour = self.price_for_tour - (self.price_for_tour * self.discount1)/100
		return self.price_for_tour


class Tour(Hotel, Taxi):
	def __init__(self, name, price_lux, price_mid):
		self.name = name
		self.price_lux = price_lux
		self.price_mid = price_mid

	def presentation(self, name, price_lux, price_mid):
		self.name = name
		self.price_lux = price_lux
		self.price_mid = price_mid

	
	def presentation(self, name, price_lux, price_mid):
		self.name = name
		self.price_lux = price_lux
		self.price_mid = price_mid
		Hotel.presentation(name, place, rooms, rooms_price, luxe_rooms, luxe_rooms_price)	
		Taxi.presentation(name, car_type, price_for_tour)		

			



	

















