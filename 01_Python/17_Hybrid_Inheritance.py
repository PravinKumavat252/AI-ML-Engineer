 #! ==========================================
#! Hybrid Inheritance
#! ==========================================


#? What is Hybrid Inheritance?

#~ Hybrid Inheritance is a combination of
#~ two or more types of inheritance.

#~ Simple Line:
#~ Hybrid = Combination of Inheritance Types

#~ Example:
#~ Single + Multiple
#~ Multiple + Multilevel
#~ Hierarchical + Multiple

#~ Ye sab Hybrid Inheritance ke examples hain.


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ek company ka structure hai.

#^              Employee
#*             /        \
#^        Manager     Developer
#*             \        /
#^             TeamLead

#~ Manager aur Developer,
#~ Employee ko inherit karte hain.

#~ TeamLead,
#~ Manager aur Developer dono ko
#~ inherit karta hai.

#~ Yahan Hierarchical aur Multiple
#~ Inheritance dono ka combination hai.

#~ Isliye ye Hybrid Inheritance hai.


#& ----------------------------------------
#& Diagram
#& ----------------------------------------

#^              A
#*            /   \
#^           B     C
#*            \   /
#^             D


#~ A → B, C (Hierarchical)

#~ D → B, C (Multiple)

#~ Dono milkar
#~ Hybrid Inheritance banate hain.


#& ----------------------------------------
#& Python Syntax
#& ----------------------------------------

#* class A:
#*    pass

#* class B(A):
#*     pass

#* class C(A):
#*     pass

#* class D(B, C):
#*     pass

#~ B aur C,
#~ A ko inherit karte hain.

#~ D,
#~ B aur C dono ko inherit karta hai.

#~ Ye Hybrid Inheritance ka
#~ basic structure hai.


#& ----------------------------------------
#& Method Resolution Order (MRO)
#& ----------------------------------------

#~ Python methods ko random order me
#~ search nahi karta.

#~ Python MRO (Method Resolution Order)
#~ follow karta hai.

#? Search Order

#^ D

#*      │

#*      ▼

#^ B

#*      │

#*      ▼

#^ C

#*      │

#*      ▼

#^ A

#*      │

#*      ▼

#^ object

#~ MRO ka exact order Python automatically
#~ calculate karta hai.


#& ----------------------------------------
#& Diamond Problem
#& ----------------------------------------

#~ Hybrid Inheritance me
#~ Diamond Problem aa sakti hai.

#? Diagram

#^              A
#*            /   \
#^           B     C
#*            \   /
#^             D

#~ Agar B aur C dono me same method ho,

#~ To D ko decide karna hota hai
#~ ki kis method ko use kare.

#~ Python is problem ko
#~ MRO ke through solve karta hai.


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Multiple inheritance types ko
#~ combine kar sakte hain.

#~ ✔ Code Reuse

#~ ✔ Flexible Design

#~ ✔ Complex projects ke liye useful.

#~ ✔ Better Feature Combination


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Samajhna difficult ho sakta hai.

#~ ❌ Diamond Problem aa sakti hai.

#~ ❌ MRO samajhna zaroori hota hai.

#~ ❌ Bahut complex inheritance
#~ code ko maintain karna difficult bana sakti hai.


#& ----------------------------------------
#& Important Keywords
#& ----------------------------------------

#^ Hybrid Inheritance

#~ Do ya do se zyada inheritance
#~ types ka combination.


#^ Diamond Problem

#~ Jab ek class tak
#~ ek hi Parent ki multiple paths se
#~ access ho.


#^ MRO

#~ Python methods ko kis order me
#~ search karega.


#^ object

#~ Python ki default base class.


#& ----------------------------------------
#& Difference from Other Types
#& ----------------------------------------

#^ Single Inheritance

#~ One Parent → One Child


#^ Multiple Inheritance

#~ Multiple Parents → One Child


#^ Multilevel Inheritance

#~ Grandparent → Parent → Child


#^ Hierarchical Inheritance

#~ One Parent → Multiple Child Classes


#^ Hybrid Inheritance

#~ Combination of two or more
#~ inheritance types.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Hybrid Inheritance?

#~ Hybrid Inheritance is a combination
#~ of two or more types of inheritance.
#~ In Python, it is commonly achieved by
#~ combining inheritance patterns such as
#~ Hierarchical and Multiple Inheritance.



#^ Assignment :-



#& 🔴 Question 1 – Person → Student, Teacher → TeachingAssistant

#* Create a class named Person.
#* Create a method named introduce().
#^    Print "I am a Person"

#* Create a class named Student that inherits from Person.
#* Create a method named study().
#^    Print "Student is Studying"

#* Create a class named Teacher that inherits from Person.
#* Create a method named teach().
#^    Print "Teacher is Teaching"

#* Create a class named TeachingAssistant that inherits from Student and Teacher.
#* Create a method named assist().
#^    Print "Teaching Assistant is Assisting"

#* Create one object of TeachingAssistant and call all methods.

# class Person:

#     def introduction(self):
#         print("I am a Person")

# class Student(Person):

#     def study(self):
#         print("Student is Studying")

# class Teacher(Person):

#     def teach(self):
#         print("Teacher is Teaching")

# class TeachingAssistant(Student, Teacher):

#     def assist(self):
#         print("Teaching Assistant is Assisting")

# rahul = TeachingAssistant()

# rahul.introduction()
# rahul.study()
# rahul.teach()
# rahul.assist()




# #& 🔴 Question 2 – Device → Mobile, Camera → Smartphone

# * Create a class named Device.
# * Create a constructor:
# ^    company

# * Create a method named display_device().

# * Create a class named Mobile that inherits from Device.
# * Create a constructor:
# ^    ram

# * Create a method named display_mobile().

# * Create a class named Camera that inherits from Device.
# * Create a constructor:
# ^    megapixel

# * Create a method named display_camera().

# * Create a class named Smartphone that inherits from Mobile and Camera.
# * Create a constructor:
# ^    storage

# * Create a method named display_smartphone().

# * Create one object of Smartphone and display all details.

# class Device:

#     def __init__(self, company):
#         self.company = company

#     def display_device(self):
#         return(f"Company Name : {self.company}")


# class Mobile(Device):

#     def __init__(self, company, ram):
#         Device.__init__(self, company)
#         self.ram = ram

#     def display_mobile(self):
#         return(f"RAM : {self.ram}")


# class Camera(Device):

#     def __init__(self, company, megapixel):
#         Device.__init__(self, company)
#         self.megapixel = megapixel

#     def display_camera(self):
#         return(f"Megapixel : {self.megapixel}")


# class Smartphone(Mobile, Camera):

#     def __init__(self, company, ram, megapixel, storage):
#         Device.__init__(self, company)
#         self.ram = ram
#         self.megapixel = megapixel
#         self.storage = storage

#     def display_smartphone(self):
#         print(f"{self.display_device()}, {self.display_mobile()}, {self.display_camera()}, Storage : {self.storage}")

    

# phone = Smartphone("Apple", "4GB", "12MP", "128GB")

# phone.display_smartphone()





# #& 🔴 Question 3 – Employee → Manager, Developer → TeamLead

# * Create a class named Employee.
# * Create a constructor:
# ^    name

# * Create a method named display_employee().

# * Create a class named Manager that inherits from Employee.
# * Create a constructor:
# ^    department

# * Create a method named display_manager().

# * Create a class named Developer that inherits from Employee.
# * Create a constructor:
# ^    programming_language

# * Create a method named display_developer().

# * Create a class named TeamLead that inherits from Manager and Developer.
# * Create a constructor:
# ^    project

# * Create a method named display_teamlead().

# * Create one object of TeamLead and display all details.

# class Employee:

#     def __init__(self, name):
#         self.name = name 

#     def display_employee(self):
#         return(f"Name : {self.name}")

# class Manager(Employee):

#     def __init__(self, name, department):
#         Employee.__init__(self, name)
#         self.department = department

#     def display_manager(self):
#         return(f"Department : {self.department}")

# class Developer(Employee):

#     def __init__(self, name, programming_language):
#         Employee.__init__(self, name)
#         self.programming_language = programming_language

#     def display_developer(self):
#         return(f"Programming Language : {self.programming_language}")

# class TeamLead(Manager, Developer):

#     def __init__(self, name, department, programming_language, project):
#         Manager.__init__(self, name, department)
#         Developer.__init__(self, name,programming_language)
#         self.project = project

#     def display_teamlead(self):
#         print(f"{self.display_employee()}, {self.display_manager()}, {self.display_developer()}, Project : {self.project}")

# team_lead = TeamLead("Rahul", "IT", "Python", "Employee Management System")
# team_lead.display_teamlead()




# #& 🔴 Question 4 – Animal → Bird, Fish → Duck

# * Create a class named Animal.
# * Create a method named eat().
# ^    Print "Animal is Eating"

# * Create a class named Bird that inherits from Animal.
# * Create a method named fly().
# ^    Print "Bird is Flying"

# * Create a class named Fish that inherits from Animal.
# * Create a method named swim().
# ^    Print "Fish is Swimming"

# * Create a class named Duck that inherits from Bird and Fish.
# * Create a method named sound().
# ^    Print "Duck says Quack"

# * Create one object of Duck and call all methods.

# class Animal:

#     def eat(self):
#         print("Animal is Eating")

# class Bird(Animal):

#     def fly(self):
#         print("Bird is Flying")

# class Fish(Animal): 

#     def swim(self):
#         print("Fish is Swimming")

# class Duck(Bird, Fish):

#     def sound(self):
#         print("Duck says Quack")

# duck = Duck()
# duck.eat()
# duck.fly()
# duck.swim()
# duck.sound()


# #& 🔴 Question 5 – Vehicle → Car, Bike → ElectricVehicle

# * Create a class named Vehicle.
# * Create a constructor:
# ^    company

# * Create a method named display_vehicle().

# * Create a class named Car that inherits from Vehicle.
# * Create a constructor:
# ^    model

# * Create a method named display_car().

# * Create a class named Bike that inherits from Vehicle.
# * Create a constructor:
# ^    engine_cc

# * Create a method named display_bike().

# * Create a class named ElectricVehicle that inherits from Car and Bike.
# * Create a constructor:
# ^    battery_capacity

# * Create a method named display_electric_vehicle().

# * Create one object of ElectricVehicle and display all details.

class Vehicle:

    def __init__(self, company):
        self.company = company

    def display_vehicle(self):
        return(f"Company Name : {self.company}")

class Car(Vehicle):

    def __init__(self, company, model):
        Vehicle.__init__(self, company)
        self.model = model

    def display_car(self):
        return(f"Model : {self.model}")

class Bike(Vehicle):

    def __init__(self, company, engine_cc):
        Vehicle.__init__(self,company)
        self.engine_cc = engine_cc

    def display_bike(self):
        return(f"Engine : {self.engine_cc}")

class ElectricVehicle(Car, Bike):

    def __init__(self, company, model, engine_cc, battery_capacity):
        Car.__init__(self, company, model)
        Bike.__init__(self, company, engine_cc)
        self.battery_capacity = battery_capacity

    def display_electric_vehicle(self):
        print(f"{self.display_vehicle()}, {self.display_car()}, {self.display_bike()}, Battery Capacity : {self.battery_capacity}")

electric_vehicle = ElectricVehicle("Tesla", "Model 3", "500 CC", "75 kWh")
electric_vehicle.display_electric_vehicle()