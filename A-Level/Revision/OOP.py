# This is how you create a class and constructor. 

# Class is a blueprint for an object 

# Construtor is the behaviour to create an object. 

class dog:
    def __init__(self, name, breed):
        self.__id = 12 # id set to private
        self.name = name
        self.breed = breed
        self.DOB = ""
        self.age = 0
    # Getters to fetch info
    def getName(self):
        return self.name
    def getBreed(self):
        return self.breed
    def getDOB(self):
        return self.DOB
    def getAge(self):
        return self.age
    def getAttributes(self, attr):
        if attr == 'name':
            return self.name
        if attr == 'breed':
            return self.breed
        if attr == 'DOB':
            return self.DOB
        if attr == 'age':
            return self.age
    def getAll(self):
        return self.name, self.breed, self.DOB, self.age
    #  Setter method. 
    def setDOB(self, DOB):
        self.DOB = DOB
    def setAge(self, Age):
        self.age = Age
    def modAttriburtes(self, attr, data):
        if attr == 'name':
            self.name = data
        if attr == 'breed':
            self.breed = data
        if attr == 'DOB':
            self.DOB = data
        if attr == 'age':
            self.age = data

    def bark(self, n):
        for i in range (n):
            print("Bark")
# This is inheritance (puppy uses dog + other attr)
class puppy(dog):
    def __init__(self, name, breed, mother):
        super().__init__(name, breed)
        self.mother = mother
    def getMum(self):
        return self.mother
    def bark(self, n):
        for i in range (n*2):
            print("Bark")


dog1 = dog("Joey", "Labrador") # Instantiated (created) an object
# Set attr
dog1.setDOB("21st Jan")
dog1.setAge(12)
# Print attr
print(dog1.getDOB())
print(dog1.getAge())
# Set puppy
puppy1 = puppy("Fred", "Spaniel", "Bonnie")
print(puppy1.getName())
print(puppy1.getMum())
# outoput bark from puppy as pup1 is of type puppy
puppy1.bark(2)