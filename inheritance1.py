'''task 1:-- single inheritance'''
# class Person:
#     def __init__(self, name,age):
#         self.name= name
#         self.age = age
#     def d_person(self):
#         print('name :',self.name)
#         print("age :",self.age)
# class Student(Person):
#     def __init__(self,name,age,course,marks):
#         super().__init__(name,age)
#         self.course = course
#         self.marks = marks
#     def d_student(self):
#         print("name :",self.name)
#         print("age :",self.age)
#         print("course :",self.course)
#         print("marks :",self.marks)
# s = Student("sunil",22,"python",90)
# s.d_student()

'''task 2:-- multi - level inheritance'''
# class Animal:
#     def eat(self):
#         print("eating...")
# class dog(Animal):
#     def bark(self):
#         print("barking...")
# class Puppy(dog):
#     def play(self):
#         print("playing...")
# p = Puppy()
# p.eat()
# p.bark()
# p.play()
'''hierarchical inheritance'''
# class Vehicle:
#     def start(self):
#         print("vehicle is startinig")
# class Car(Vehicle):
#     def driver(self):
#         print("car is driving by a person")
# class Bike(Vehicle):
#     def ride(self):
#         print("bike is riding by a person")
# c = Car()
# c.start()
# c.driver()
# b = Bike()
# b.start()
# b.ride()
'''task 4:-- multiple inheritance + mro'''
# class Father:
#     def show(self):
#         print("father class method")
# class Mother:
#     def show(self):
#         print("mother class method")
# class child(Father,Mother):
#     pass 
# print(child.mro())
'''task 5 -- hybrid inheritace + mro'''
class person:
    def name(self,name):
        print("person name :",name)
class student(person):
    def course(self,course):
        print("student course :",course)
class employee(person):
    def salary(self,salary):
        print("employe salary:",salary)
class intern(student,employee):
    pass
print(intern.mro())






