 #! ==========================================
#! Hierarchical Inheritance
#! ==========================================


#? What is Hierarchical Inheritance?

#~ Hierarchical Inheritance is a type of
#~ inheritance in which one Parent class
#~ is inherited by two or more Child classes.

#~ Simple Line:
#~ One Parent → Multiple Child Classes


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ek Animal class hai.

#^ Animal
#~ • Eat()
#~ • Sleep()

#~ Dog aur Cat dono Animals hain.

#~ Isliye dono Animal class ko inherit karenge.

#~ Dog apne methods bhi add karega.

#~ Cat apne methods bhi add karegi.


#? Diagram

#^                Animal
#*             /     |     \
#*            /      |      \
#^         Dog      Cat     Cow


#~ Yahan

#^ Animal → Parent Class

#^ Dog, Cat, Cow → Child Classes


#& ----------------------------------------
#& Python Syntax
#& ----------------------------------------

#* class Parent:
#*     pass

#* class Child1(Parent):
#*     pass

#* class Child2(Parent):
#*     pass

#* class Child3(Parent):
#*     pass

#~ Ek Parent class ko
#~ multiple Child classes inherit karti hain.


#& ----------------------------------------
#& Example
#& ----------------------------------------

#* class Animal:

#*     def eat(self):
#*         print("Eating")


#* class Dog(Animal):

#*     def bark(self):
#*         print("Barking")


#* class Cat(Animal):

#*     def meow(self):
#*         print("Meowing")


#* d = Dog()
#* c = Cat()

#* d.eat()
#* d.bark()

#* c.eat()
#* c.meow()

#~ Dog object

#~ • eat()

#~ • bark()

#~ use kar sakta hai.


#~ Cat object

#~ • eat()

#~ • meow()

#~ use kar sakta hai.


#& ----------------------------------------
#& Method Resolution Order (MRO)
#& ----------------------------------------

#~ Har Child class apni
#~ inheritance chain follow karti hai.

#? Dog

#^ Dog

#*     │

#*     ▼

#^ Animal

#*     │

#*     ▼

#^ object


#? Cat

#^ Cat

#*     │

#*     ▼

#^ Animal

#*     │

#*     ▼

#^ object


#~ Python pehle Child class me search karta hai.

#~ Agar method nahi milta,

#~ to Parent class me search karta hai.

#~ Agar Parent me bhi nahi milta,

#~ to object class me search karta hai.


#& ----------------------------------------
#& Related Concepts
#& ----------------------------------------

#~ Hierarchical Inheritance ke saath
#~ constructor bhi use hote hain.

#? Agar Child class me constructor nahi hai

#~ Parent ka constructor automatically
#~ call ho jata hai.

#? Agar Child class ka apna constructor hai

#~ To Parent constructor automatically
#~ call nahi hota.

#? Parent constructor bhi chalana ho

#^ super().__init__()


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Code Reuse

#~ ✔ Less Code Duplication

#~ ✔ Easy Maintenance

#~ ✔ Better Code Organization

#~ ✔ Real-life Classification ko
#~ represent karta hai.


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Bahut zyada Child classes hone par
#~ project manage karna difficult ho sakta hai.

#~ ❌ Parent class me changes
#~ sabhi Child classes ko affect kar sakte hain.


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


#& ----------------------------------------
#& Important Keywords
#& ----------------------------------------

#^ Parent Class

#~ Jis class ko multiple Child classes
#~ inherit karti hain.


#^ Child Class

#~ Jo Parent class ke features use karti hai.


#^ MRO (Method Resolution Order)

#~ Python methods ko kis order me
#~ search karega.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Hierarchical Inheritance?

#~ Hierarchical Inheritance is a type of
#~ inheritance where one Parent class is
#~ inherited by two or more Child classes.



#^ Assignment :-



#& 🔴 Question 1 – Animal → Dog, Cat

#* Create a class named Animal.
#* Create a method named eat().
#^    Print "Animal is Eating".

#* Create a class named Dog that inherits from Animal.
#* Create a method named bark().
#^    Print "Dog is Barking".

#* Create a class named Cat that inherits from Animal.
#* Create a method named meow().
#^    Print "Cat is Meowing".

#* Create one object of Dog and one object of Cat, then call all available methods.

class Animal:

    def eat(self):
        print("Animal is Eating")

class Dog(Animal):

    def bark(self):
        print("Dog is Barking")

class Cat(Animal):

    def meow(self):
        print("Cat is Meowing")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()




#& 🔴 Question 2 – Vehicle → Car, Bike

#* Create a class named Vehicle.
#* Create a constructor:
#^    company

#* Create a method named display_vehicle().


#* Create a class named Car that inherits from Vehicle.
#* Create a constructor:
#^    model

#* Create a method named display_car().


#* Create a class named Bike that inherits from Vehicle.
#* Create a constructor:
#^    engine_cc

#* Create a method named display_bike().

#* Create one object of Car and one object of Bike, then display all details.

class Vehicle:

    def __init__(self, company):
        self.company = company

    def display_vehicle(self):
        return(f"Company Name : {self.company}")

class Car(Vehicle):

    def __init__(self, company, model):
        super().__init__(company)
        self.model = model

    def display_car(self):
        return(f"{self.display_vehicle()}, Car Model : {self.model}")

class Bike(Vehicle):

    def __init__(self, company, engine_cc):
        super().__init__(company)
        self.engine_cc = engine_cc

    def display_bike(self):
        return(f"{self.display_vehicle()}, Bike Engine : {self.engine_cc}")


car = Car("Toyota", "Fortuner")
bike = Bike("Honda", "150cc")

print(car.display_car())
print(bike.display_bike())




#& 🔴 Question 3 – Person → Student, Teacher

#* Create a class named Person.
#* Create a constructor:
#^    name

#* Create a method named display_person().


#* Create a class named Student that inherits from Person.
#* Create a constructor:
#^    course

#* Create a method named display_student().


#* Create a class named Teacher that inherits from Person.
#* Create a constructor:
#^    subject

#* Create a method named display_teacher().


#* Create one object of Student and one object of Teacher, then display all details.

class Person:

    def __init__(self, name):
        self.name = name

    def display_person(self):
        return(f"Person Name : {self.name}")

class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display_student(self):
        return(f"{self.display_person()}, Course : {self.course}")

class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display_teacher(self):
        return(f"{self.display_person()}, Subject : {self.subject}")


student = Student("Amit", "AI/ML")
teacher = Teacher("Shobhit", "Python")

print(student.display_student())
print(teacher.display_teacher())




#& 🔴 Question 4 – Employee → Manager, Developer

#* Create a class named Employee.
#* Create a constructor:
#^    name

#* Create a method named display_employee().


#* Create a class named Manager that inherits from Employee.
#* Create a constructor:
#^    department

#* Create a method named display_manager().


#* Create a class named Developer that inherits from Employee.
#* Create a constructor:
#^    programming_language

#* Create a method named display_developer().


#* Create one object of Manager and one object of Developer, then display all details.

class Employee:

    def __init__(self, name):
        self.name = name

    def display_employee(self):
        return(f"Employee Name :{self.name}")

class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display_manager(self):
        return(f"{self.display_employee()}, Department : {self.department}")

class Developer(Employee):

    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language

    def display_developer(self):
        return(f"{self.display_employee()}, Programming Language : {self.programming_language}")

manager = Manager("Rahul", "IT")
developer = Developer("Amit", "Python")

print(manager.display_manager())
print(developer.display_developer())




#& 🔴 Question 5 – Device → Mobile, Laptop

#* Create a class named Device.
#* Create a constructor:
#^    company

#* Create a method named display_device().


#* Create a class named Mobile that inherits from Device.
#* Create a constructor:
#^    ram

#* Create a method named display_mobile().


#* Create a class named Laptop that inherits from Device.
#* Create a constructor:
#^    processor

#* Create a method named display_laptop().


#* Create one object of Mobile and one object of Laptop, then display all details.

class Device:

    def __init__(self, company):
        self.company = company

    def display_device(self):
        return(f"Company Name : {self.company}")

class Mobile(Device):

    def __init__(self, company, ram):
        super().__init__(company)
        self.ram = ram

    def display_mobile(self):
        return(f"{self.display_device()}, RAM : {self.ram}")

class Laptop(Device):

    def __init__(self, company, processor):
        super().__init__(company)
        self.processor = processor

    def display_laptop(self):
        return(f"{self.display_device()}, Processor : {self.processor}")

mobile = Mobile("Samsung", "8 GB")
laptop = Laptop("Dell", "Intel Core i7")

print(mobile.display_mobile())
print(laptop.display_laptop())

