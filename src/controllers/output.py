import json

data = {
    "title": "mamaguevoo",
    "wwe":"bby"
}

with open('src/resources/data.json','w') as json_file:
    json.dump(data, json_file)
