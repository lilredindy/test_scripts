import requests
import json




r = requests.get("http://www.pokeapi.co/api/v2/type/12/")

print(r.status_code)

blob = r.json()
print (blob)
print ("These are all " + blob["name"] + " type pokemons...")

print(blob["pokemon"])

for p in blob["pokemon"]:
	print(p["pokemon"]["name"])






#the `dumps' take a python data structure, and converts it back into json.
#the 'loads' function takes a json file and converts it into a dictionary 
#or list. 
# apparently the blob is not proper json b4 the dumps call

parsed_blob = json.loads(json.dumps(blob))  
print ("These are all " + parsed_blob["name"] + " type pokemons...")


