''' task 1. basic inheritance'''
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def d_person(self):
        print(" Name : ",self.name)
        print(" age : ",self.age)
class Student(Person):
    pass
s = Student("sunil",22)
s.d_person()
s1 = Student("bhanu",23)
s1.d_person()
''' task 2 . inheritance & specific method'''
class Animal:
    def eat(self):
        print("eating")
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def bark(self):
        print("dog barks")
d = Dog()
d.eat()
d.sleep()
d.bark()
'''task 3.method overloading'''
class Vehicle:
    def start(self):
        print("vehicle is starting")
class Car(Vehicle):
    def start(self):
        print("car is starting with a key")
c = Car()
c.start()