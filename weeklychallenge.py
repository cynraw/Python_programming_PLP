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