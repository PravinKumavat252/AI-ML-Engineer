#! ==========================================
#! Duck Typing
#! ==========================================


#? What is Duck Typing?

#~ Duck Typing is a feature of Python.

#~ Python object ka type check nahi karta.
#~ Python sirf ye dekhta hai ki object ke paas
#~ required method ya behavior hai ya nahi.

#~ Simple Line:
#~ "Behavior is more important than Type."


#& ----------------------------------------
#& Famous Rule
#& ----------------------------------------

#~ "If it walks like a duck and quacks like a duck,
#~ then it is a duck."

#~ Meaning:
#~ Agar object required behavior dikhata hai,
#~ to Python uska actual type check nahi karta.


#& ----------------------------------------
#& Example
#& ----------------------------------------

#* Dog

#^ speak()


#* Cat

#^ speak()


#* Human

#^ speak()


#~ Python ko farak nahi padta object Dog,
#~ Cat ya Human hai.

#~ Bas object ke paas
#~ speak() method hona chahiye.


#& ----------------------------------------
#& Why do we use Duck Typing?
#& ----------------------------------------

#~ Different classes ek hi method provide kar sakti hain.

#~ Python un sab objects ke saath
#~ same code ko use kar sakta hai.

#~ Isse code flexible aur reusable ban jata hai.


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Flexible Programming
#~ ✔ Code Reuse
#~ ✔ Less Dependency on Object Type
#~ ✔ Easy to Extend
#~ ✔ Pythonic Coding Style


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Agar required method nahi hoga,
#~ to Runtime Error aa sakta hai.

#~ ❌ Beginners ke liye confusing ho sakta hai.


#& ----------------------------------------
#& Important Note
#& ----------------------------------------

#~ Duck Typing me object ka type important nahi hota.

#~ Object ka behavior (methods) important hota hai.


#& ----------------------------------------
#& Interview Point
#& ----------------------------------------

#? What is Duck Typing?

#~ Duck Typing is a Python concept where
#~ an object's behavior is more important
#~ than its actual type.



#^ Assignment :



#& 🔴 Question 1 – Dog & Cat

#* Create a class named Dog.
#* Create a method:
#* speak()
#^    Print "Dog Barks".

#* Create another class named Cat.
#* Create a method:
#* speak()
#^    Print "Cat Meows".

#* Create a function named make_sound(animal).
#^    Call animal.speak().

#* Create Dog and Cat objects.
#* Pass both objects to make_sound().

class Dog:

    def speak(self):
        print("Dog Barks")

class Cat:

    def speak(self):
        print("Cat Meows")

def make_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)



#& 🔴 Question 2 – Car & Bike

#* Create a class named Car.
#* Create a method:
#* start()
#^    Print "Car Started".

#* Create another class named Bike.
#* Create a method:
#* start()
#^    Print "Bike Started".

#* Create a function named start_vehicle(vehicle).
#^    Call vehicle.start().

#* Create Car and Bike objects.
#* Pass both objects to start_vehicle().

class Car:

    def start(self):
        print("Car Started")

class Bike:

    def start(self):
        print("Bike Started")

def start_vehicle(vehicle):
    vehicle.start()

car = Car()
bike = Bike()

start_vehicle(car)
start_vehicle(bike)



#& 🔴 Question 3 – Student & Teacher

#* Create a class named Student.
#* Create a method:
#* introduce()
#^    Print "I am a Student".

#* Create another class named Teacher.
#* Create a method:
#* introduce()
#^    Print "I am a Teacher".

#* Create a function named show_person(person).
#^    Call person.introduce().

#* Create Student and Teacher objects.
#* Pass both objects to show_person().

class Student:

    def introduce(self):
        print("I am a Student")

class Teacher:

    def introduce(self):
        print("I am a Teacher")

def show_person(person):
    person.introduce()

student = Student()
teacher = Teacher()

show_person(student)
show_person(teacher)



#& 🔴 Question 4 – PDF & Word

#* Create a class named PDF.
#* Create a method:
#* open()
#^    Print "Opening PDF File".

#* Create another class named Word.
#* Create a method:
#* open()
#^    Print "Opening Word File".

#* Create a function named open_file(file).
#^    Call file.open().

#* Create PDF and Word objects.
#* Pass both objects to open_file().

class PDF:

    def open(self):
        print("Opening PDF File")

class Word:

    def open(self):
        print("Opening Word File")

def open_file(file):
    file.open()

pdf = PDF()
word = Word()

open_file(pdf)
open_file(word)



#& 🔴 Question 5 – Email & SMS

#* Create a class named Email.
#* Create a method:
#* send()
#^    Print "Email Sent".

#* Create another class named SMS.
#* Create a method:
#* send()
#^    Print "SMS Sent".

#* Create a function named send_message(message).
#^    Call message.send().

#* Create Email and SMS objects.
#* Pass both objects to send_message().

class Email:

    def send(self):
        print("Email Sent")

class SMS:

    def send(self):
        print("SMS Sent")

def send_message(message):
    message.send()

email = Email()
sms = SMS()

send_message(email)
send_message(sms)
