class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            self._age = age

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    
    def hobby(self):
        return "I love coding"
    
try:
    Person.age = -1
except ValueError as e:
    print(e)
    

person1 = Person("John", 25)
person2 = Person("Jane", 30)
print(person1.get_name())
print(person1.get_age())
print(person1.hobby())

    
    