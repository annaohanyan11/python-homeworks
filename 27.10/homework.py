import threading
import requests
import datetime
import json
import time



def function_1():
	number = 1
	with open('2homework8.json', 'r') as file:
		data = json.load(file)

		for link in data['items']:
			a = link['url']
			r = requests.get(a)
			for i in a:
				k = str(number) + '.png'
				with open(k, 'wb') as f1:
					f1.write(r.content)
				break
			number = number + 1	


if __name__ == '__main__':
	starting_time = datetime.datetime.today()

	thread_list = []
	for i in range(10):
		x = threading.Thread(target=function_1)
		thread_list.append(x)
		x.start()

	
