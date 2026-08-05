 #! ==========================================
#! Multiple Inheritance
#! ==========================================


#? What is Multiple Inheritance?

#~ Multiple Inheritance is a type of inheritance
#~ in which one Child class inherits from
#~ two or more Parent classes.

#~ Simple Line:
#~ Ek Child class ek se zyada Parent classes
#~ se inherit karti hai.


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ek Smartphone hai.

#^ Camera
#~ • Take Photo()

#^ MusicPlayer
#~ • Play Music()

#~ Smartphone ko dono features chahiye.

#~ Isliye Smartphone,
#~ Camera aur MusicPlayer dono ko inherit karta hai.


#? Diagram

#^ Camera         MusicPlayer
#*      \          /
#*       \        /
#*        \      /
#^       Smartphone


#& ----------------------------------------
#& Python Syntax
#& ----------------------------------------

#* class Parent1:
#*     pass

#* class Parent2:
#*     pass

#* class Child(Parent1, Parent2):
#*     pass

#~ Child class multiple Parent classes ko
#~ inherit karti hai.

#~ Parent class ke names brackets ()
#~ ke andar comma (,) se likhe jate hain.


#& ----------------------------------------
#& Method Resolution Order (MRO)
#& ----------------------------------------

#~ Agar same method multiple Parent classes me
#~ available ho,

#~ to Python ek fixed order me search karta hai.

#? Search Order

#^ Child

#*      │

#*      ▼

#^ Parent1

#*      │

#*      ▼

#^ Parent2

#*      │

#*      ▼

#^ object


#~ Isi search order ko
#~ Method Resolution Order (MRO) kehte hain.


#& ----------------------------------------
#& Same Method in Both Parents
#& ----------------------------------------

#* class A:
#*     def show(self):
#*         print("A")

#* class B:
#*     def show(self):
#*         print("B")

#* class C(A, B):
#*     pass

#* c = C()
#* c.show()

#~ Output:
#~ A

#~ Reason:
#~ Python pehle Parent1 (A) ko check karta hai.

#~ Method mil gaya,
#~ isliye Parent2 (B) ko check nahi karta.


#& ----------------------------------------
#& Constructor Behavior
#& ----------------------------------------

#~ Agar Child class me constructor nahi hai,

#~ aur dono Parent classes me __init__()
#~ method hai,

#~ to Python MRO ke according
#~ sirf pehle Parent ka constructor call karta hai.

#? Search Order

#^ Child

#*      │

#*      ▼

#^ Parent1 Constructor ✔

#*      │

#*      ▼

#^ Parent2 Constructor ✖


#~ Parent2 ka constructor automatically
#~ call nahi hota.

#~ Dono constructors chalane ke liye
#~ super() ka proper use karna padta hai.


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Code Reuse

#~ ✔ Multiple Parent classes ke features
#~ ek Child class me mil jate hain.

#~ ✔ Less Code

#~ ✔ Better Flexibility

#~ ✔ Easy Feature Combination


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Same method name hone par
#~ confusion ho sakti hai.

#~ ❌ MRO samajhna zaroori hota hai.

#~ ❌ Complex inheritance structure
#~ code ko difficult bana sakta hai.


#& ----------------------------------------
#& Important Keywords
#& ----------------------------------------

#^ Parent Classes

#~ Jitni classes se Child inherit karta hai.


#^ Child Class

#~ Jo sab Parent classes ke features use karti hai.


#^ MRO (Method Resolution Order)

#~ Python kis order me methods search karega.


#^ object

#~ Python ki sabhi classes ki
#~ default base class.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Multiple Inheritance?

#~ Multiple Inheritance is a type of inheritance
#~ where one child class inherits the properties
#~ and methods of two or more parent classes.



#^ Assignment :-



#& 🔴 Question 1 – Father and Mother

#* Create a class named `Father`.
#^    Create a method `house()`.
#^    Print `"Father owns a House"`.

#* Create another class named `Mother`.
#^     Create a method `car()`.
#^     Print `"Mother owns a Car"`.

#* Create a class named `Child` that inherits from both classes.
#* Create one object and call both methods.

# class Father:

#     def house(self):
#         print("Father owns a House")

# class Mother:

#     def car(self):
#         print("Mother owns a Car")

# class Child(Father, Mother):
#     pass

# child = Child()

# child.house()
# child.car()

# print(Child.mro())




#& 🔴 Question 2 – Camera and Music

#* Create a class named `Camera`.
#* Method:
#^     `take_photo()`

#* Create another class named `MusicPlayer`.
#* Method:
#^     `play_music()`

#* Create a class named `SmartPhone` that inherits from both classes.
#* Create another method:
#^     `make_call()`

#* Call all three methods.

# class Camera:

#     def take_photo(self):
#         print("Taking Photos")

# class MusicPlayer:

#     def play_music(self):
#         print("Playing Music")

# class SmartPhone(Camera, MusicPlayer):

#     def make_call(self):
#         print("Calling...")

# samsung = SmartPhone()

# samsung.take_photo()
# samsung.play_music()
# samsung.make_call()

# print(SmartPhone.mro())



#& 🔴 Question 3 – Teacher and SportsCoach

#* Create a class named `Teacher`.
#* Constructor:
#^     teacher_name

#* Method:
#^     `display_teacher()`

#* Create another class named `SportsCoach`.
#* Constructor:
#^     sport_name

#* Method:
#^     `display_sport()`

#* Create a class named `SchoolStaff` that inherits from both classes.
#* Display all information.

# class Teacher:

#     def __init__(self, teacher_name):
#         self.teacher_name = teacher_name

#     def display_teacher(self):
#         print(f"Teacher Name : {self.teacher_name}")

# class SportsCoach:

#     def __init__(self, sport_name):
#         self.sport_name = sport_name

#     def display_sport(self):
#         print(f"Sport Name : {self.sport_name}")


# class SchoolStaff(Teacher, SportsCoach):

#     def __init__(self, teacher_name, sport_name):
#         Teacher.__init__(self, teacher_name)
#         SportsCoach.__init__(self, sport_name)

#     def display_schoolstaff(self):
#         self.display_teacher()
#         self.display_sport()

# school = SchoolStaff('Himanshu', 'Kho-Kho')

# school.display_schoolstaff()

# print(SchoolStaff.mro())




#& 🔴 Question 4 – Laptop and Printer

#* Create a class named `Laptop`.
#* Constructor:
#^     laptop_brand

#* Method:
#^     `display_laptop()`

#* Create another class named `Printer`.
#* Constructor:
#^     printer_brand

#* Method:
#^     `display_printer()`

#* Create a class named `OfficeSetup` that inherits from both classes.
#* Display all information.

# class Laptop:

#     def __init__(self, laptop_brand):
#         self.laptop_brand = laptop_brand

#     def display_laptop(self):
#         print(f"Laptop Brand : {self.laptop_brand}")

# class Printer:

#     def __init__(self, printer_brand):
#         self.printer_brand = printer_brand

#     def display_printer(self):
#         print(f"Printer Brand : {self.printer_brand}")

# class OfficeSetup(Laptop, Printer):

#     def __init__(self, laptop_brand, printer_brand):
#         Laptop.__init__(self, laptop_brand)
#         Printer.__init__(self, printer_brand)

#     def display_OfficeSetup(self):
#         self.display_laptop()
#         self.display_printer()

# office = OfficeSetup('Acer', 'HP')

# office.display_OfficeSetup()
# print(OfficeSetup.mro())

    


#& 🔴 Question 5 – Student and Employee

#* Create a class named `Student`.
#* Constructor:
#^     student_name
#^     course

#* Method:
#^     `display_student()`

#* Create another class named `Employee`.
#* Constructor:
#^     company_name
#^     salary

#* Method:
#^     `display_employee()`

#* Create a class named `Intern` that inherits from both classes.
#* Display all details.

# class Student:

#     def __init__(self, student_name, course):
#         self.student_name = student_name
#         self.course = course

#     def display_student(self):
#         print(f"Student Name : {self.student_name}, Course : {self.course}")

# class Employee:

#     def __init__(self, company_name, salary):
#         self.company_name = company_name
#         self.salary = salary

#     def display_employee(self):
#         print(f"Company Name : {self.company_name}, Salary : {self.salary}")

# class Intern(Student, Employee):

#     def __init__(self, student_name, course, company_name, salary):
#         Student.__init__(self, student_name, course)
#         Employee.__init__(self, company_name, salary)

#     def display_intern(self):
#         self.display_student()
#         self.display_employee()

# scholar = Intern('Pravin', "M.sc", "Communication Craft", 30000)

# scholar.display_intern()
# print(Intern.mro())




#& 🔴 Question 6 – Engine and GPS

#* Create a class named `Engine`.
#* Method:
#^     `start_engine()`

#* Create another class named `GPS`.
#* Method:
#^     `show_location()`

#* Create a class named `Car` that inherits from both classes.
#* Create another method:
#^     `drive()`

#* Call all methods.

# class Engine:

#     def start_engine(self):
#         print("Start Engine")

# class GPS:

#     def show_location(self):
#         print("Locating...")

# class Car(Engine, GPS):

#     def drive(self):
#         print("Car is Driving")

#     def display_car(self):
#         self.drive()
#         self.start_engine()
#         self.show_location()

# honda = Car()

# honda.display_car()
# print(Car.mro())



#& 🔴 Question 7 – Bank and Insurance

#* Create a class named `Bank`.
#* Constructor:
#^     bank_name

#* Method:
#^     `display_bank()`

#* Create another class named `Insurance`.
#* Constructor:
#^     insurance_company

#* Method:
#^     `display_insurance()`

#* Create a class named `Customer` that inherits from both classes.
#* Display all information.

# class Bank:

#     def __init__(self, bank_name):
#         self.bank_name = bank_name

#     def display_bank(self):
#         print(f"Bank Name : {self.bank_name}")

# class Insurance:

#     def __init__(self, insurance_company):
#         self.insurance_company = insurance_company

#     def display_insurance(self):
#         print(f"Insurance Company Name : {self.insurance_company}")

# class Customer(Bank, Insurance):

#     def __init__(self, bank_name, insurance_company):
#         Bank.__init__(self, bank_name)
#         Insurance.__init__(self, insurance_company)

#     def display_customer(self):
#         self.display_bank()
#         self.display_insurance()

# pravin = Customer('IOB', 'LIC')

# pravin.display_customer()
# print(Customer.mro())




#& 🔴 Question 8 – University and Hostel (Interview Level ⭐)

#* Create a class named `University`.
#* Constructor:
#^     university_name

#* Method:
#^     `display_university()`

#* Create another class named `Hostel`.
#* Constructor:
#^  hostel_name

#* Method:
#^  `display_hostel()`

#* Create a class named `Student` that inherits from both classes.
#* Constructor:
#^     student_name

#* Method:
#^     `display_student()`

#* Display:
#^     University Name
#^     Hostel Name
#^     Student Name

class University:

    def __init__(self, university_name):
        self.university_name = university_name

    def display_university(self):
        print(f"University Name : {self.university_name}")

class Hostel:

    def __init__(self, hostel_name):
        self.hostel_name = hostel_name

    def display_hostel(self):
        print(f"Hostel Name : {self.hostel_name}")

class Student(University, Hostel):

    def __init__(self, university_name, hostel_name, student_name):
        University.__init__(self, university_name)
        Hostel.__init__(self, hostel_name)
        self.student_name = student_name

    def display_student(self):
        self.display_university()
        self.display_hostel()
        print(f"Student Name : {self.student_name}")

pravin = Student("Monark University", "Prem Boys Hostel", 'Pravin')

pravin.display_student()
print(Student.mro())