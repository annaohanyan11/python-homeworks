class Dictionary:
	def __init__(self,text):
		
		self.dict0 = {}
		k = 0
		for i in text:
			self.dict0[i] = k + 1 
			k = k + 1
		print(self.dict0)	

	def dublicate(self,text):
		a = [] 
		b = dict() 
		for key, val in dict0.items(): 
			if val not in a: 
				a.append(val) 
				b[key] = val 
		print(a)			




word = Dictionary('python')
word.dublicate('python')


			