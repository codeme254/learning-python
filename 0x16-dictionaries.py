#!/usr/bin/python3

# a dictionary is a changeable, unordered collection of unique key:value pairs. They are fast because they use hashing thus allow us to access a value quickly

capitals = {
'USA': 'Washington DC',
'India': 'New Delhi',
'China': 'Beijing',
'Russia': 'Moscow'
}

# accessing elements in the dictionary
# accessing russia capital city
print(capitals['Russia'])

# what if the key does not exist?
# use the get() method, it is safer, it returns None if there is not.
print(capitals.get('Germany'))

# Print only the keys
print(capitals.keys())
# print only the values
print(capitals.values())
# print both keys and values
print(capitals.items())

for key, value in capitals.items():
    print("{} is the capital city of {}".format(value, key))

# update method
capitals.update({'Germany': 'Berlin'})
# we can also update existing key value pairs.
capitals.update({'USA': 'Las Vegas'})
print(capitals.items())

# we can use the pop method to remove key value pair.
capitals.pop('China')
print(capitals.items())

# capitals.clear() will remove everythin in the dictionary.
