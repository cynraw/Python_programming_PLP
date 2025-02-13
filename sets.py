#A set is an unordered collection with no duplicate elements.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # duplicates will be removed

# fast membership testing
print('orange' in basket)  # True
print('cam' in basket) # False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)  # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b

# set comprehension 
a = {x for x in 'abracadabra' if x not in 'abc'}  # unique letters in a but not in b
print(a)  # {'r', 'd'}
