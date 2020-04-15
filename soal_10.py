import json

file_json = open('data.json')

data = json.loads(file_json.read())
print(data)
