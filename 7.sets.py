#set- sets are unordered and unindexed, elements inside sets are unique, a set can be modified but its elements are immutable

utensils = {"fork", "spoon", "knife"}
dishes = {"Bowl","plate", "cup"}

utensils.add("plate")
utensils.remove("fork")

print(utensils)
# utensils.clear()

utensils.update(dishes) 
print(utensils)
print(dishes)


dinner_table = utensils.union(dishes) #or dishes.union(utensils)
#this is union of two sets

print(utensils.difference(dishes)) #this will print what utensils have but dishes doesn't

print(dishes.intersection(utensils)) #this will give what is common between two sets