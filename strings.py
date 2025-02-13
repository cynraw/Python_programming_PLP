#Access String Characters in Python
##Indexing: One way is to treat strings as a list and use index values.
##Similar to a list, Python allows negative indexing for its strings.
greet = "Hello"
print(greet[1])

print(greet[-3])

##Slicing: To slice a string, you use the square brackets and the colon :.
print(greet[1:4])

##Python Strings are immutable
greet[1] = "x"
print(greet) #TypeError: 'str' object does not support item assignment  

## Python Multiline String
song = """
Nyanya wa kambo si nyanyaaa,
Nyanya wa kambo si nyanyaaa,
Nyanya wa kambo si nyanyaaa,"""
print(song)

##Python String Operations
## Compare Two Strings
srt1 = "Hello, world"
str2 = "Python Programming"
str3 = "Hello, world"

print(srt1 == str2)
print(srt1 == str3)

## String Concatenation
t = "Hello, "
name = "Ronoh"
print(t + name)

##Iterate Through a Python String
for x in "Ronoh":
    print(x)

##Python String Length
print(len("Ronoh"))

#String Membership Test
print("Ron" in "Ronoh")

#Escape Sequences in Python
#The escape sequence is used to escape some of the characters present inside a string.