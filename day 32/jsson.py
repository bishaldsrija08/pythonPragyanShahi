import json

data ={
    "name": "Bishal Rijal",
    "age": 25,
    "city": "Kathmandu",
    "hobbies": ["coding", "traveling", "cooking"]
}

# with open('data.json', 'a') as file:
#     json.dump(data, file, indent=4)

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)