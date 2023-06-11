#dictionary = A chageable, unorderd collection of unique key:value pairs
#             This is fast because they use hashing, allow us to access value quickly

capitals= {
    'USA':"Washington DC",
    "India":"New Delhi",
    "China": 'Beijing',
    'Russia': 'Moscow'
}

print(capitals['India'])

#if we want that value that doesn't exist will give error by this way
#print(capitals['germany'])

print(capitals.get("Germany")) #This will not return error

print(capitals.keys()) #this will only print keys
print(capitals.values())


#updating a dictionary
capitals.update({'germany':'Berlin'}) #updating new key
capitals.update({'USA': 'las vegas'}) #updating existing key

for key,value in capitals.items():
    print(key, value)

capitals.pop('China')
capitals.clear()
