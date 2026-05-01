# fruit1= "apple"
# fruit2= "banana"
# fruit3= "cherry"
# fruit4 = "grape"


fruits = ["apple", "banana", "cherry", "grape"]
ages = [25, 30, 35, 40]
lists = ["apple", 25, "banana", 30, "cherry", 35, "grape", 40, True, False, "apple", 25]
print(lists[1])
lists.append("orange")
print(lists)
print(len(lists))
name1= "Bishal"
name2= "Sita"
names = [name1, name2] # names = ["Bishal", "Sita"]
# print(fruits)
# print(ages)
# print(lists)


integers = [1, 2, 3, 4, 5]
print(type(integers))

# list() constructor
thislist= list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)