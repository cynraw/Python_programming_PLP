# Python_programming_PLP
# Weekly Code Challenge! 🐍
## Personalized Greeting App 👋
Create a program that asks for the user’s name and favorite color,then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome”
## Simple Quiz Game 
Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again.

## Weekly Code Challenge!
Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.


Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.


Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then print the dictionary to the console.


Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.


Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

# File Handling and Exception handling
File Handling in Python is the ability to perform various operations on files, like reading from and writing to them. Files are used to store data permanently.

File handling in Python allows you to:

Open files in different modes (e.g., read-only or write mode).

Read and write data in a variety of formats.

Close files to free up system resources.

## File Operations in Python
### Opening Files 🔓
Use Python’s open() function to access a file.

Syntax: open(filename, mode), where:

filename: The name of the file you want to work with.

mode: The mode you want to open the file in.

Modes include:

'r': Read mode, used for reading files.

'w': Write mode, creates a new file or overwrites an existing one.

'a': Append mode, adds new content without deleting existing data.

'rb', 'wb': Binary modes for non-text files, like images.

### Reading Files 📜

Python provides multiple ways to read file contents:

.read(): Reads the entire file.

.readline(): Reads a single line at a time.

.readlines(): Reads all lines and returns a list.

### Writing & Appending to Files ✍️

Writing is essential for saving data, like storing a user’s progress or keeping a record.

write(): Overwrites content, while append() allowing adding without deleting.

## Exception Handling
Basic Structure of try-except Blocks ⚙️

try: Runs code that might throw an error.

except: Catches the error, allowing you to respond without crashing.

finally: Runs no matter what, often used to clean up (like closing a file).

## Best Practices 📏
- Use with for file handling: Auto-close files, preventing potential leaks.
- Check file existence before reading/writing, to avoid crashes.
- Handle specific exceptions over general ones (e.g., FileNotFoundError instead of Exception).
- Document error messages clearly for easier debugging and user support.

## Introduction to OOP
Object-oriented programming (OOP) is a style of programming that heavily relies on objects. 

These objects can have attributes and methods. While attributes store data, methods define behavior.

Object-oriented programming (OOP) offers several benefits when organizing and managing code. By grouping related data and functions into logical classes, OOP promotes code structure and simplifies maintenance, especially as programs grow in size and complexity. The modular approach makes it easier to understand, modify, and reuse code, thereby reducing development time.

Another benefit of OOP is its ability to provide a clear and relatable programming style, which can be more helpful for developers. The use of objects and the relationships between them mirror real-world concepts. This makes it easier to reason about code and design complex systems.

Finally, OOP's concepts such as encapsulation and inheritance, contribute to code robustness by promoting data protection and code reusability.

### What is a Class in Python?
Is a blueprint that is used to create objects.

To define a class, you have to use the class keyword, provided by Python, then followed by the name of the class and a colon:

## Class and Instance Attributes
While class attributes are common to all instances created from your class, instance attributes are unique to each instance.

Class attributes are variables that belong to the class itself, rather than to individual instances of the class. The effect of class attributes is that all instances you create from your class will inherit and share that class attribute and its value. 

## Encapsulation in Python
It refers to the bundling of data (attributes) and methods within a class. Encapsulation provides data protection and control over how the code interacts with an object's internal state.

You can achieve encapsulation in Python by defining private attributes and methods within a class. By convention, private attributes and methods are prefixed with a single underscore (_). While Python does not have strict private modifiers like some other languages, the underscore prefix serves as a warning to other developers not to access or modify the attributes and methods directly from outside the class.

Accessing private attributes through getter methods (or properties) is a best practice in OOP because it promotes encapsulation, ensures data integrity, and provides flexibility and maintainability in your code. It also allows you to add additional logic, such as validation or computation, when accessing or modifying attributes.

Getter methods are used to retrieve the value of a private attribute.
Setter methods are used to modify the value of a private attribute, often with validation or additional logic.
Together, they ensure encapsulation, data integrity, and flexibility in your code.

## Inheritance in Python
It allows classes to inherit attributes and methods from other classes. The new class inherits attributes and methods from the existing class, known as the parent or base class. The new class is called the child or derived class.

Inheritance promotes code reuse by allowing the child class to inherit and extend the functionality of the parent class. This helps in creating hierarchical relationships between classes and organizing code in a more structured and logical manner.
