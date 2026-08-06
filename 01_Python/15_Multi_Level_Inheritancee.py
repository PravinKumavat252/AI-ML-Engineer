 #! ==========================================
#! Multilevel Inheritance
#! ==========================================


#? What is Multilevel Inheritance?

#~ Multilevel Inheritance is a type of inheritance
#~ in which one Child class inherits from another
#~ Child class, creating a chain of inheritance.

#~ Simple Line:
#~ Grandparent → Parent → Child


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ek Animal class hai.

#^ Animal
#~ • Eat()

#~ Dog, Animal ko inherit karta hai.

#^ Dog
#~ • Bark()

#~ Puppy, Dog ko inherit karta hai.

#^ Puppy
#~ • Play()

#~ Isliye Puppy ko
#~ Animal aur Dog dono ke features mil jate hain.


#? Diagram

#^ Animal
#*      │
#*      ▼
#^ Dog
#*      │
#*      ▼
#^ Puppy


#~ Yahan

#^ Animal → Grandparent Class

#^ Dog → Parent Class

#^ Puppy → Child Class


#& ----------------------------------------
#& Python Syntax
#& ----------------------------------------

#* class A:
#*     pass

#* class B(A):
#*     pass

#* class C(B):
#*     pass

#~ B class, A ko inherit karti hai.

#~ C class, B ko inherit karti hai.

#~ Is tarah inheritance ki ek chain
#~ create ho jati hai.


#& ----------------------------------------
#& Method Resolution Order (MRO)
#& ----------------------------------------

#~ Jab Child class me method nahi milta,

#~ To Python Parent class me search karta hai.

#~ Agar Parent me bhi nahi milta,

#~ To Grandparent class me search karta hai.

#? Search Order

#^ Child (C)

#*      │

#*      ▼

#^ Parent (B)

#*      │

#*      ▼

#^ Grandparent (A)

#*      │

#*      ▼

#^ object


#& ----------------------------------------
#& Example
#& ----------------------------------------

#* class Animal:

#*     def eat(self):
#*         print("Eating")


#* class Dog(Animal):

#*     def bark(self):
#*         print("Barking")


#* class Puppy(Dog):

#*     def play(self):
#*         print("Playing")


#* p = Puppy()

#* p.eat()
#* p.bark()
#* p.play()

#~ Puppy object Animal, Dog aur Puppy
#~ tino classes ke methods use kar sakta hai.


#& ----------------------------------------
#& Constructor Flow
#& ----------------------------------------

#~ Agar har class me __init__() ho

#~ aur sab classes me super() ka use kiya gaya ho,

#~ To constructors MRO ke according execute honge.

#? Execution Order

#^ Animal Constructor

#*      │

#*      ▼

#^ Dog Constructor

#*      │

#*      ▼

#^ Puppy Constructor


#~ Isse Parent classes ka initialization
#~ automatically complete ho jata hai.


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Code Reuse

#~ ✔ Less Code

#~ ✔ Easy Extension

#~ ✔ Better Code Organization

#~ ✔ Real-life Hierarchy ko represent karta hai.


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Bahut lambi inheritance chain
#~ code ko difficult bana sakti hai.

#~ ❌ Debugging thodi difficult ho sakti hai.

#~ ❌ Parent class me changes
#~ niche wali classes ko affect kar sakte hain.


#& ----------------------------------------
#& Difference from Single Inheritance
#& ----------------------------------------

#^ Single Inheritance

#~ Parent → Child


#^ Multilevel Inheritance

#~ Grandparent → Parent → Child


#^ Single Inheritance

#~ Sirf ek Parent aur ek Child hota hai.


#^ Multilevel Inheritance

#~ Teen ya usse zyada levels ki
#~ inheritance chain hoti hai.


#& ----------------------------------------
#& Important Keywords
#& ----------------------------------------

#^ Grandparent Class

#~ Sabse upar wali class.


#^ Parent Class

#~ Jo Grandparent ko inherit karti hai.


#^ Child Class

#~ Jo Parent class ko inherit karti hai.


#^ Inheritance Chain

#~ Grandparent → Parent → Child


#^ MRO

#~ Python methods ko kis order me
#~ search karega.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Multilevel Inheritance?

#~ Multilevel Inheritance is a type of inheritance
#~ where one child class inherits from another
#~ child class, forming an inheritance chain.



#^ Assignment :-



#& 🔴 Question 1 – Animal → Mammal → Dog

#* Create a class named Animal.
#* Create a method eat().
#^    Print "Animal is Eating".

#* Create a class named Mammal that inherits from Animal.
#* Create a method walk().
#^    Print "Mammal is Walking".

#* Create a class named Dog that inherits from Mammal.
#* Create a method bark().
#^    Print "Dog is Barking".

#* Create one object of Dog and call all three methods.

# class Animal:

#     def eat(self):
#         print("Animal is Eating")

# class Mammal(Animal):

#     def walk(self):
#         print("Mammal is Walking")

# class Dog(Mammal):

#     def bark(self):
#         print("Dog is Barking")

# dog = Dog()

# dog.eat()
# dog.walk()
# dog.bark()




#& 🔴 Question 2 – Person → Employee → Manager

#* Create a class named Person.
#* Constructor:
#^    name

#* Method:
#^    display_person()

#* Create a class named Employee that inherits from Person.
#* Constructor:
#^    salary

#* Method:
#^    display_employee()

#* Create a class named Manager that inherits from Employee.
#* Constructor:
#^    department

#* Method:
#^    display_manager()

#* Create one object and display:

# class Person:

#     def __init__(self, name):
#         self.name = name

#     def display_person(self):
#         return(f"Person Name : {self.name}")

# class Employee(Person):

#     def __init__(self, name, salary):
#         Person.__init__(self, name)
#         self.salary = salary

#     def display_employee(self):
#         return(f"Salary : {self.salary}")

# class Manager(Employee):

#     def __init__(self, name, salary, department):
#         Employee.__init__(self, name, salary)
#         self.department = department

#     def display_manager(self):
#         print(f"{self.display_person()}, {self.display_employee()}, Department : {self.department}")

# manager = Manager("Hiren", 58000, "IT")
# manager.display_manager()




#& 🔴 Question 3 – Vehicle → Car → ElectricCar

#* Create a class named Vehicle.
#* Create a method start().
#^    Print "Vehicle Started".

#* Create a class named Car that inherits from Vehicle.
#* Create a method drive().
#^    Print "Car is Driving".

#* Create a class named ElectricCar that inherits from Car.
#* Create a method charge().
#^    Print "Charging Battery".

#* Create one object and call all three methods.

# class Vehicle:

#     def start(self):
#         print("Vehicle Started")

# class Car(Vehicle):

#     def drive(self):
#         print("Car is Driving")

# class ElectricCar(Car):

#     def charge(self):
#         print("Charging Battery")

# electric = ElectricCar()

# electric.start()
# electric.drive()
# electric.charge()



#& 🔴 Question 4 – School → College → University

#* Create a class named School.
#* Constructor:
#^    school_name

#* Method:
#^    display_school()

#* Create a class named College that inherits from School.
#* Constructor:
#^    college_name

#* Method:
#^    display_college()

#* Create a class named University that inherits from College.
#* Constructor:
#^    university_name

#* Method:
#^    display_university()

#* Create one object and display:

# class School:

#     def __init__(self, school_name):
#         self.school_name = school_name

#     def display_school(self):
#         return(f"School Name : {self.school_name}")

# class College(School):

#     def __init__(self, school_name, college_name):
#         School.__init__(self, school_name)
#         self.college_name = college_name

#     def display_college(self):
#         return(f"College Name : {self.college_name}")

# class University(College):

#     def __init__(self, school_name, college_name, university_name):
#         College.__init__(self, school_name, college_name)
#         self.university_name = university_name

#     def display_university(self):
#         print(f"{self.display_school()}, {self.display_college()}, University Name : {self.university_name}")

# university = University("C.P.E.S", "R.G.C.O.C.A", "Monark University")

# university.display_university()



#& 🔴 Question 5 – Device → Mobile → SmartPhone

#* Create a class named Device.
#* Constructor:
#^    company

#* Method:
#^    display_device()

#* Create a class named Mobile that inherits from Device.
#* Constructor:
#^    model

#* Method:
#^    display_mobile()

#* Create a class named SmartPhone that inherits from Mobile.
#* Constructor:
#^    ram

#* Method:
#^    display_smartphone()

#* Create one object and display:

# class Device:

#     def __init__(self, company):
#         self.company = company

#     def display_device(self):
#         return(f"Company Name : {self.company}")

# class Mobile(Device):

#     def __init__(self, company, model):
#         Device.__init__(self, company)
#         self.model = model

#     def display_mobile(self):
#         return(f"Model : {self.model}")

# class SmartPhone(Mobile):

#     def __init__(self, company, model, ram):
#         Mobile.__init__(self, company, model)
#         self.ram = ram

#     def display_smartphone(self):
#         print(f"{self.display_device()}, {self.display_mobile()}, RAM : {self.ram}")

# smartphone = SmartPhone("Apple", "iPhone 15", "6GB")

# smartphone.display_smartphone()
