import json

with open('wordDictionary.json') as json_data:
    d = json.load(json_data)
    print(len(d))
    print(type(d))