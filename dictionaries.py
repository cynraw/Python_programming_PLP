#Dictionaries
# In Python dictionaries are written with curly brackets, and they have keys and values pairs.
#A dictionary is a collection which is ordered*(you can refer to any item by an index), changeable and do not allow duplicates.

mydict = {
    "Ronoh" : "Gwagon",
    "Jack" : "v8",
    "Roine" : "Benz",
}
print(mydict)

#adding items
mydict["Cheptanui"] = "BMW"
print(mydict)

#changing items
mydict["Cheptanui"] = "Range Rover"
print(mydict)

#removing items
del mydict["Cheptanui"]
print(mydict)

mydict.pop("Roine")
print(mydict)

#accessing items
print(mydict["Ronoh"])


#Loop Through a Dictionary
for x in mydict:
    print(x)    #prints the keys

for x in mydict:
    print(mydict[x])    #prints the values

#Nested Dictionaries
myfamily = {
    "first born" : {
        "name" : "Ronoh",
        "age" : 23,
        "car" : "Gwagon"
    },
    "second born" : {
        "name" : "Jack",
        "age" : 21,
        "car" : "v8"
    }
}
print(myfamily)

#Create three dictionaries then create one dictionary that will contain the three dictionaries
child1 = {
    "name" : "Jack",
    "age" : 21,
    "car" : "v8"
}
child2 = {
    "name" : "Ronoh",
    "age" : 22,
    "car" : "benz"
}

myfahm = {
    "child1" : child1,
    "child2" : child2
}
print(myfahm)
#Access Items in Nested Dictionaries
print(myfahm["child1"]["name"])

#Using nested loops to access all the values in the nested dictionaries
for x in myfahm:
    print(x)
    for y in myfahm[x]:
        print(myfahm[x][y])





#Dictionary Membership Test
#You can test if a key is in a dictionary or not using the in keyword.
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)
print(55 in squares)

#membership test for keys only not values
print(81 in squares)

#Python has a set of built-in methods that you can use on dictionaries.

#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary



