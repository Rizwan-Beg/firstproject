# class Dog:
#     # Class variable
#     species = "Canine"

#     def __init__(self, name, age):
#         # Instance variables
#         self.name = name
#         self.age = age

# # Create objects
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# # Access class and instance variables
# print(dog1.species)  # (Class variable)
# print(dog1.name)     # (Instance variable)
# print(dog2.name)     # (Instance variable)

# # Modify instance variables
# dog1.name = "Max"
# print(dog1.name)     # (Updated instance variable)

# # Modify class variable
# Dog.species = "Feline"
# print(dog1.species)  # (Updated class variable)
# print(dog2.species)
print(25*"-")
# # Single Inheritance
# class Dog:
#     def __init__(self, name):
#         self.name = name
        
#     def display_name(self):
#         print(f"Dog's Name: {self.name}")

# class Labrador(Dog):  # Single Inheritance
#     def sound(self):
#         print("Labrador woofs")

# # Multilevel Inheritance
# class GuideDog(Labrador):  # Multilevel Inheritance
#     def guide(self):
#         print(f"{self.name}Guides the way!")

# # Multiple Inheritance
# class Friendly:
#     def greet(self):
#         print("Friendly!")

# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# # Example Usage
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()

# guide_dog = GuideDog("Max")
# guide_dog.display_name()
# guide_dog.guide()
# #guide_dog.sound()


# retriever = GoldenRetriever("Charlie")
# retriever.display_name()
# retriever.greet()
# retriever.sound()
# Parent Class
# class Dog:
#     def sound(self):
#         print("dog sound")  # Default implementation

# # Run-Time Polymorphism: Method Overriding
# class Labrador(Dog):
#     def sound(self):
#         print("Labrador woofs")  # Overriding parent method

# class Beagle(Dog):
#     def sound(self):
#         print("Beagle Barks")  # Overriding parent method

# # Compile-Time Polymorphism: Method Overloading Mimic
# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c  # Supports multiple ways to call add()

# # Run-Time Polymorphism
# dogs = [Dog(), Labrador(), Beagle()]
# for dog in dogs:
#     dog.sound()  # Calls the appropriate method based on the object type


# # Compile-Time Polymorphism (Mimicked using default arguments)
# calc = Calculator()
# print(calc.add(5, 10))  # Two arguments
# print(calc.add(5, 10, 15))  # Three arguments
class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())