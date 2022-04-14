import json 
import requests 

r = requests.get('http://localhost:3000/')

data = r.json()

#print(str(data['name'] and data['color']))
for k in data:
	print (k["name"] + " is " + k["color"])