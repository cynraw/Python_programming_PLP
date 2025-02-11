#Tuples
#Tuples are similar to lists, but they are immutable which means that the values inside a tuple cannot be changed. Also, tuples are defined using parentheses, ().
hey = ("hello",)
print(hey)
print(type(hey))


#accesing elements - tuples are also indexed
letters = ("a", "b", "c", "d")
print(letters[0])
print(letters[-1])

#tuple methods
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))

print(len(my_tuple))

#Change Tuple Values - Change the tuple into a list so that you can be able to change the values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


#Python has two built-in methods that you can use on tuples.
#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found