person = {
    "name": "Bishal",
    "age": 25,
    "city": "Kathmandu",
    "hobbies": ["coding", "traveling", "cooking"],
    "is_student": True,
    "education": ("Bachelor's", "Master's"),
    "contact": ["bishal@example.com", "+977 9800000000"]
}

print(person)
print(type(person))

# Accessing values
print(person["name"])
print(person["hobbies"][1])
person["age"] = 26
print(person["age"])

# looping through dictionary
for key in person:
    print(f"{key}: {person[key]}")
    
for key, value in person.items():
    print(f"{key}: {value}")
    
# keys
print(person.keys())

# values
print(person.values())