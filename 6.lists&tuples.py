#list = used to store multiple items in a single variable

car = ["maruti", "ferrari", "alto", "skoda","alto", "mercedes"]
print(car[0])
print()
#iteration of car list where i represent car at index i

for i in car:
    print(i)

#list is mutable and can be changed after declaration
car[0]="Maruti Suzuki" #modifying car at 0th index

print(car[0])

car.append("fortuner") #this car will add to end of list
car.remove("alto") #this will remove that alto which occurs first in list
car.pop() #this will remove  the last element form list
car.insert(1,"fortuner") #insert at index 1 of car

print(car)

car.sort() #this will sort list alphabetically

print(car)

car.clear() #clears all the elements of list
print(car)

#----2D list in Python-------

drinks=["coffee", "soda", "tea"]
dinner=["pizza", "hamburger", "hotdog"]
dessert=["cake", "sweets", "iceCream"]

food = [drinks, dinner, dessert]

print(food[0][0])
print(food[0])
print(food)

#------Tuples--------
#tuples are ordered and immutable(lists are mutable) used to group together related data

myself=("Vikas", 19, "male", "IIT-G")

for x in myself:
    print(x)

if "Vikas" in myself:
    print("Vikas is here in myself")
