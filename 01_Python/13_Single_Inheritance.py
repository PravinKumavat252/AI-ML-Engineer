 #! ==========================================
#! Single Inheritance
#! ==========================================


#? What is Single Inheritance?

#~ Single Inheritance is a type of inheritance
#~ in which one Child class inherits from only
#~ one Parent class.

#~ Simple Line:
#~ Ek Child class sirf ek hi Parent class se
#~ inherit karti hai.


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ek Animal class hai.

#^ Animal
#~ • Eat()
#~ • Sleep()
#~ • Walk()

#~ Dog bhi ek Animal hai.

#~ Isliye Dog class ko ye methods dobara
#~ likhne ki zarurat nahi.

#~ Wo Animal class ko inherit kar legi.


#? Diagram

#^        Animal
#*           │
#*           ▼
#^          Dog


#~ Yahan

#^ Animal → Parent Class (Base Class)

#^ Dog → Child Class (Derived Class)


#& ----------------------------------------
#& Python Syntax
#& ----------------------------------------


#* class Parent:
#*     pass

#* class Child(Parent):
#*     pass

#~ Child class Parent class ko inherit karti hai.

#~ Parent class ka naam brackets () ke andar
#~ likha jata hai.


#& ----------------------------------------
#& How Single Inheritance Works
#& ----------------------------------------

#~ Jab Child class ka object banta hai,

#~ Python pehle Child class me search karta hai.

#~ Agar method ya variable Child me nahi milta,

#~ To Parent class me search karta hai.

#~ Agar Parent me bhi nahi mila,

#~ To AttributeError deta hai.


#? Search Order

#^ Child Class

#*      │

#*      ▼

#^ Parent Class

#*      │

#*      ▼

#^ AttributeError


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Code Reuse

#~ ✔ Less Code

#~ ✔ Easy Maintenance

#~ ✔ Better Code Organization

#~ ✔ Easy to Learn

#~ ✔ Reduces Code Duplication


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Tight dependency between Parent and Child.

#~ ❌ Changes in Parent class can affect Child class.

#~ ❌ Large Parent classes become difficult to maintain.


#& ----------------------------------------
#& Important Keywords
#& ----------------------------------------

#^ Parent Class (Base Class)

#~ Jis class se inherit kiya jata hai.


#^ Child Class (Derived Class)

#~ Jo Parent class ke features inherit karti hai.


#^ Inheritance

#~ Parent class ke variables aur methods ko
#~ Child class me use karna.


#& ----------------------------------------
#& Related Concepts
#& ----------------------------------------

#~ Single Inheritance ke saath hum ye concepts
#~ bhi use karte hain:

#~ • Parent Constructor

#~ • Child Constructor

#~ • super() Function

#~ • Method Overriding

#~ In sab topics ko alag-alag detail me
#~ padhte hain.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Single Inheritance?

#~ Single Inheritance is a type of inheritance
#~ where one child class inherits the properties
#~ and methods of only one parent class.


#^ Assignment :-

#& 🔴 Question 1 – Animal and Dog

#? Create a class named Animal.

#* Create a method eat().
#~ Print "Animal is Eating".

#* Create another class named Dog that inherits from Animal.

#~ Create a method bark().
#~ Print "Dog is Barking".

#* Create one object of Dog and call both methods.

# class Animal:

#     def eat(self):
#         print("Animal is Eating")

# class Dog(Animal):

#     def bark(self):
#         print("Dog is Barking")

# dog = Dog()

# dog.eat()
# dog.bark()



#& 🔴 Question 2 – Vehicle and Car

#? Create a class named Vehicle.

#* Create a method start_engine().  
#* Create another class named Car that inherits from Vehicle.
#* Create a method drive().
#* Create one object of Car and call both methods.

# class Vehicle:

#     def start_engine(self):
#         print("Engine Starting...")

# class Car(Vehicle):

#     def drive(self):
#         print("Driving...")

# car = Car()

# car.start_engine()
# car.drive()



#& 🔴 Question 3 – Person and Student

#? Create a class named Person.

#~ Constructor:
#^    name
#^    age

#~ Create a method display_person().
#~ Create another class named Student that inherits from Person.
#~ Constructor:
#^    course

#~ Create a method display_student().
#~ Create one object and display all details.

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_person(self):
#         print(f"Student Name : {self.name}, Age : {self.age}")

# class Student(Person):

#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course

#     def display_student(self):
#         print(f"Student Name : {self.name}, Age : {self.age}, Course : {self.course}")

# pravin = Student("Pravin", 22, "M.sc")

# pravin.display_person()
# pravin.display_student()



#& 🔴 Question 4 – Employee and Manager

#? Create a class named Employee.

#* Constructor:
#^    name
#^    salary

#* Create a method display_employee().
#* Create another class named Manager that inherits from Employee.
#* Constructor:
#^    department

#* Create a method display_manager().
#* Display all information.

# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_employee(self):
#         print(f"Employee Name : {self.name}, Salary : {self.salary}")

# class Manager(Employee):

#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display_manager(self):
#         print(f"Employee Name : {self.name}, Salary : {self.salary}, Department : {self.department}")

# emp = Manager('Pravin', 38000, 'IT')

# emp.display_employee()
# emp.display_manager()



#& 🔴 Question 5 – Mobile and Smartphone

#? Create a class named Mobile.

#* Method:
#^    call()

#* Create another class named SmartPhone that inherits from Mobile.
#* Methods:
#^    camera()
#^    internet()

#* Create one object and call all methods.

# class Mobile:

#     def call(self):
#         print("Calling...")

# class Smartphone(Mobile):

#     def camera(self):
#         print("Camera has 50px")

#     def internet(self):
#         print("Supports 5G Internet")

# samsung = Smartphone()

# samsung.call()
# samsung.camera()
# samsung.internet()



#& 🔴 Question 6 – BankAccount and SavingsAccount

#? Create a class named BankAccount.

#* Constructor:
#^    account_holder
#^    balance

#* Create a method show_balance().
#* Create another class named SavingsAccount that inherits from BankAccount.
#* Constructor:
#^    interest_rate

#* Create a method show_interest().
#* Display all details.

# class BankAccount:

#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def show_balance(self):
#         print(f"Account Holder Name : {self.account_holder}, Balance : {self.balance}")

# class SavingsAccount(BankAccount):

#     def __init__(self, account_holder, balance, interest_rate):
#         super().__init__(account_holder, balance)
#         self.interest_rate = interest_rate

#     def show_interest(self):
#         self.show_balance()
#         print(f"Interest Rate : {self.interest_rate}%")

# saving = SavingsAccount('Pravin', 35000, 12)

# saving.show_balance()
# saving.show_interest()




#& 🔴 Question 7 – College and EngineeringCollege

#? Create a class named College.

#* Constructor:
#^    college_name
#^    city

#* Create a method display_college().
#* Create another class named EngineeringCollege that inherits from College.
#* Constructor:
#^    branch

#* Create a method display_branch().
#* Display all information.

# class College:

#     def __init__(self, college_name, city):
#         self.college_name = college_name
#         self.city = city

#     def display_college(self):
#         print(f"College Name : {self.college_name}, City : {self.city}")

# class EngineeringCollege(College):

#     def __init__(self, college_name, city, branch):
#         super().__init__(college_name, city)
#         self.branch = branch

#     def display_branch(self):
#         self.display_college()
#         print(f"Branch : {self.branch}")

# cs = EngineeringCollege('Monark University', 'Ahmedabad', 'M.sc')

# cs.display_branch()




#& 🔴 Question 8 – Shape and Rectangle

#? Create a class named Shape.

#* Method:
#^    show_shape()

#* Create another class named Rectangle that inherits from Shape.
#* Constructor:
#^    length
#^    width

#* Create a method calculate_area().
#* Display the shape and area.

# class Shape:

#     def show_shape(self):
#         print("This is shape")

# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def show_shape(self):
#         super().show_shape()                     
#         print(f"Rectangle: length = {self.length}, width = {self.width}")
#         print(f"Area = {self.calculate_area()}")

# rec = Rectangle(12, 10)

# rec.show_shape()



#& 🔴 Question 9 – Book and Ebook

#? Create a class named Book.

#* Constructor:
#^    title
#^    author

#* Create a method display_book().
#* Create another class named Ebook that inherits from Book.
#* Constructor:
#^    file_size

#* Create a method display_file_size().
#* Display all information.

# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display_book(self):
#         print(f"Book Title : {self.title}, Author Name : {self.author}")

# class Ebook(Book):

#     def __init__(self, title, author, file_size):
#         super().__init__(title, author)
#         self.file_size = file_size

#     def display_file_size(self):
#         self.display_book()
#         print(f"Ebook File Size : {self.file_size} MB")

# book = Ebook("Python Basics", "Guido van Rossum", 136)

# book.display_file_size()




#& 🔴 Question 10 – Hospital and Doctor

#? Create a class named Hospital.

#* Constructor:
#^    hospital_name
#^    location

#* Create a method display_hospital().
#* Create another class named Doctor that inherits from Hospital.
#* Constructor:
#^    doctor_name
#^    specialization

#* Create a method display_doctor().
#* Display all information.

# class Hospital:

#     def __init__(self, hospital_name, location):
#         self.hospital_name = hospital_name
#         self.location = location

#     def display_hospital(self):
#         print(f"Hospital Name : {self.hospital_name}, Location : {self.location}")

# class Doctor(Hospital):

#     def __init__(self, hospital_name, location, doctor_name, specialization):
#         super().__init__(hospital_name, location)
#         self.doctor_name = doctor_name
#         self.specialization = specialization

#     def display_doctor(self):
#         self.display_hospital()
#         print(f"Doctor Name : {self.doctor_name}, Specialization in : {self.specialization}")


# doctor = Doctor("Apollo Hospital", "Ahmedabad", "Dr. Raj Patel", "Cardiologist")

# doctor.display_doctor()