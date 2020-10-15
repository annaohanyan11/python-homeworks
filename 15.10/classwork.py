class Store:
	def __init__(self, text):
		self.text = text
	def presentation(self):
		return "This store sells equipments"


class NewStore(Store):
	def __init__(self, text, type_):
		super().__init__(text)
		self.type_ = type_

	def presentation(self):
		presentation = F"{super().presentation()} and its type is {self.type_}"	
		return presentation

little_store = NewStore("Hi. We are Saturn, we sell cellphones", "phone seller")		

print(little_store.presentation())


class ClothesStore:
	def presentation(self):
		return "This store sells clothes"

class Shoes(ClothesStore):
	def presentation(self):
		b = super().presentation()
		return "This shoes are for kids", b


shoes1 = Shoes()
print(shoes1.presentation())				

a = Store("sddf")
b = ClothesStore()
print(a.presentation())
print(b.presentation())				