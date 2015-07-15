import json


data = []
with open('testcases.json') as f:
    for line in f:
    	print line 
        data.append(json.loads(line))
        