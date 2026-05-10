import json

user_data ={
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
    "hobbies": input("Enter your hobbies (comma separated): ").split(",")
}

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)
print("User data has been saved to user_data.json")

with open("user_data.json", "r") as file:
    loaded_data = json.load(file)
print("Loaded user data:")
print(f"Name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")