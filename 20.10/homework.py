import os

os.chdir('/Users/annaohanyan/Desktop/python/python-homeworks/')

os.mkdir("Dir1")
print(os.getcwd())
os.chdir("/Users/annaohanyan/Desktop/python/python-homeworks/Dir1")
os.mkdir("Dir2")
os.makedirs("Dir3/Dir4")
print(os.getcwd())
question = input("Do you want to delete the folders?yes/no \n")

if question == "yes": 
	os.chdir("/Users/annaohanyan/Desktop/python/python-homeworks/Dir1/Dir3")
	os.rmdir("Dir4")
	os.chdir("/Users/annaohanyan/Desktop/python/python-homeworks/Dir1")
	os.rmdir("Dir3")
	os.rmdir("Dir2")
	os.chdir("/Users/annaohanyan/Desktop/python/python-homeworks")
	os.rmdir("Dir1")
else:
	pass






