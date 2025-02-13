#Write a program that uses a dictionary to store information 
# about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
person = input("Enter your name: ")
age = input("Enter your age: ") 
color = input("Enter your favorite color: ")    

myperson = {
    "name" : person,
    "age" : age,
    "color" : color
}
print(myperson)


#Create a tuple containing the names of five of your favorite books.
#  Then, use a for loop to print each book name on a separate line.
books = ("reb", "defin", "nomber", "kilgo", "noty")
for book in books:
    print(book)


#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

numbers = input("Enter a list of numbers separated by commas: ")

list_numbers = [int(x.strip()) for x in numbers.split(",")]

print(sum(list_numbers))    

