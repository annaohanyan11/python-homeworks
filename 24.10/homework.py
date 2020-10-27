import requests

number = 1
with open('image.txt', 'r') as file:
	for line in file:
		a = line
		r = requests.get(a)
		for i in line:
			k = str(number) + ".png"
			with open(k, 'wb') as f1:
				f1.write(r.content)
			break
		number = number + 1
			
				
		
				


