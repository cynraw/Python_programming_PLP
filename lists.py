#LISTS
list_a = [1,2,3,4,5]
print(list_a)

#accessing elements
print(list_a[0])
for i in list_a:
    print(i)

#slicing lists - returns a new list with the specified range
print(list_a[1:3])
print(list_a[:3])
print(list_a[2:])
print(list_a[:])

#updating lists
list_a[2] = 10
print(list_a)

list_a.append(32)
print(list_a)

list_b = [11,12,13]
list_a.extend(list_b)
print(list_a)

#deleting elements
del list_a[2]
print(list_a)

list_a.remove(32)
print(list_a)

list_a.pop(2)
print(list_a)

#counting elements
print(list_a.count(1))


#sorting lists
list_a.sort()
print(list_a)

#Lists comprehension
list_c = [x for x in range(10)]
print(list_c)
list_d = [x * x for x in range(10)]
print(list_d)

languages = ["Python", "Java", "C++"]
for language in languages:
    print(language) 


#Lists methods
#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
