 #! Class Variables 

#& Introduction

#~ Ab tak humne jitne bhi programs banaye (Student, Mobile, Car, BankAccount, ATM...), unme humne **Instance Variables** use kiye.

#? Example:

#* class Student:

#*     def __init__(self, name, age):
#*         self.name = name
#*         self.age = age

#~ Yahan:

#* `name` → Instance Variable
#* `age` → Instance Variable



#& Kyun?

#~ Kyuki har student ka name aur age alag hota hai.

# ? Example:

#^ Student 1

#* Name = Pravin
#* Age = 22

#^ Student 2

#* Name = Rahul
#* Age = 21

#~ Dono ka data alag hai.
#~ Isliye ye **Instance Variables** hain.



#& Problem

#~ Ab ek situation socho.
#~ Ek college me 5000 students hain.
#~ Sabhi students ka college same hai.

#^ Monark University

#~ Agar hum har object me ye likhen:

#^ self.college = "Monark University"



#? To kya hoga?

#^ Student 1

#* College = Monark University


#^ Student 2

#* College = Monark University


#^ Student 3

#* College = Monark University


#^ Student 5000

#^ College = Monark University


#~ Ek hi information 5000 baar memory me store hogi.
#~ ❌ Ye memory waste hai.



#& Solution

#~ Is problem ka solution hai:


#!  Class Variable

#~ Agar koi data **sabhi objects ke liye same ho**, to use **Class Variable** banate hain.



#& Definition


#& Class Variable

#~ Jo variable class ke sabhi objects ke liye common (same) hota hai, use Class Variable kehte hain.



#^ Syntax

#* class Student:

#*     college = "Monark University"

#*     def __init__(self, name):
#*         self.name = name


#?  Yahan

#* college = "Monark University"

#~ Constructor ke bahar hai.
#~ Isliye ye **Class Variable** hai.



#& Memory Representation


#&                  Student Class
#*           -------------------------
#^           college = Monark University
#*           -------------------------
#~                /              \
#~               /                \
#^         Student 1          Student 2
#*         ---------          ---------
#^         Name=Pravin        Name=Rahul



#~ Observe:

#^ college

#* Sirf **ek baar** memory me bana.

#~ Lekin

#^ name

#* Har object ke andar alag bana.



#&Important Rule

#? Rule 1

#~ Jo data har object ka alag ho

#^ ➡ Instance Variable

#? Examples

#* Name
#* Age
#* Salary
#* Price
#* Balance



#? Rule 2

#~ Jo data sab objects ka same ho

#^ ➡ Class Variable

#? Examples

#* College Name
#* Country
#* Bank Name
#* Company Name
#* Vehicle Type
#* Number of Wheels



#& Instance Variable vs Class Variable

#^ | Instance Variable                | Class Variable                         |
#* | -------------------------------- | -------------------------------------- |
#~ | Har object ka alag data          | Sab objects ka same data               |
#~ | Constructor ke andar banta hai   | Constructor ke bahar banta hai         |
#~ | `self.variable`                  | Class ke andar direct declare hota hai |
#~ | Har object ki alag copy hoti hai | Sirf ek copy hoti hai                  |
#~ | Memory zyada use hoti hai        | Memory kam use hoti hai                |



#& Example 

#^ Instance Variables

#* Name
#* Age
#* Roll Number
#* CGPA

#~ Kyuki har student ka ye data alag hai.


#^ Class Variables

#* College Name
#* University
#* Country

#~ Kyuki ye sab students ke liye same hai.



#& Accessing Class Variable

#? Method 1 (Best Way)

#~ Using Class Name

#* Student.college



#? Method 2

#~ Using Object


#* s1.college

#~ Ye bhi sahi hai.



#? Method 3

#~ Inside Method

#* self.college

#~ Ye bhi valid hai.



#& Memory Trick

#~ Yaad rakhne ka easiest rule.
#~ Instance = Individual
#~ Har object ka apna.

#? Example


#^ Pravin
#* Age = 22


#^ Rahul
#* Age = 21

#~ Age alag hai.
#~ To Instance Variable.



#& Class = Common

#~ Sabka same.

#? Example


#? College

#* Monark University


#^ Pravin
#~ ↓
#* Monark University



#^ Rahul
#~ ↓
#* Monark University


#~ Same hai.
#~ To Class Variable.



#& Advantages

#? Memory Save

#~ Ek hi copy banti hai.
#~ Har object me duplicate data nahi banta.



#? Easy Maintenance

#~ Ek jagah change karo.
#~ Sab objects ke liye update ho jayega.



#? Common Data Store

#~ Jo information sabke liye same ho.
#~ Uske liye best hai.



#& Real-Life Analogy

#? Classroom Example

#~ Ek classroom me 50 students hain.
#~ Har student ka:


#* Name
#* Age
#* Roll Number

#~ Alag hai.

#~ Ye **Instance Variables** hain.

#^ Lekin

#~ Sabhi ka

#* School = ABC School

#~ Same hai.
#~ Ye **Class Variable** hai.




#! Quick Revision

#& Instance Variable

#~ ✔ Har object ka alag data
#~ ✔ Constructor ke andar
#~ ✔ self.variable
#~ ✔ Har object ki alag copy

#? Examples

#* Name
#* Age
#* Salary
#* Balance
#* Price



#& Class Variable

#~ ✔ Sab objects ka same data
#~ ✔ Constructor ke bahar
#~ ✔ Sirf ek copy
#~ ✔ Sab objects share karte hain

#? Examples

#* College Name
#* Country
#* Bank Name
#* Company Name
#* Number of Wheels



#^ Assignment :-


#& 🔴 Question 1 – Student Class

#? Create a class named `Student`.

#* Create a class variable:
#~   `college_name = "Monark University"`

#* Constructor should take:
#~  `name`
#~  `age`

#* Create an instance method:
#~  `display_details()`
#~   Display:
#^         Name
#^         Age
#^         College Name

#* Create **2 Student objects**.
#* Call the `display_details()` method for both objects.


class Student:

    college_name = "Monark University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"College Name : {Student.college_name}, Student Name : {self.name}, Age : {self.age}")

s1 = Student('Pravin', 22)
s2 = Student('Rahul', 21)

s1.display_details()
s2.display_details()



#& 🔴 Question 2 – Employee Class

#? Create a class named `Employee`.

#* Create a class variable:
#~   `company_name = "TCS"`

#* Constructor should take:
#~   `name`
#~   `salary`

# * Create an instance method:
#~    display_employee()
#~    Display:
#^           Employee Name
#^           Salary
#^           Company Name

# * Create **2 Employee objects**.
# * Call the `display_employee()` method for both objects.

class Employee:

    company_name = "TCS"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(f"Company Name : {Employee.company_name}, Employee Name : {self.name}, Salary : {self.salary}")

e1 = Employee('Pravin', 45000)
e2 = Employee('Rahul', 38000)

e1.display_employee()
e2.display_employee()



#& 🔴 Question 3 – Car Class

#? Create a class named `Car`.

#* Create a class variable:
#~    `wheels = 4`

#* Constructor should take:
#~    `company`
#~    `model`
#~    `price`

#* Create an instance method:

#~    `display_car()`
#~    Display:
#^           Company
#^           Model
#^           Price
#^           Number of Wheels

# * Create **2 Car objects**.
# * Call the `display_car()` method for both objects.

class Car:

    wheels = 4

    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_car(self):
        print(f"Company Name : {self.company}, Model : {self.model}, Price : {self.price}, Number of Wheels : {Car.wheels}")


c1 = Car("BMW", "X5", 9500000)
c2 = Car("Audi", "A6", 7000000)

c1.display_car()
c2.display_car()



#& 🔴 Question 4 – Mobile Class

#? Create a class named `Mobile`.

#* Create a class variable:
#~    `category = "Smartphone"`

#* Constructor should take:
#~    `company`
#~    `ram`
#~    `storage`

#* Create an instance method:

#~    `display_mobile()`
#~     Display:
#^            Company
#^            RAM
#^            Storage
#^            Category

# * Create **2 Mobile objects**.
# * Call the `display_mobile()` method for both objects.

class Mobile:

    category = "Smartphone"

    def __init__(self, company, ram, storage):
        self.company = company
        self.ram = ram
        self.storage = storage

    def display_mobile(self):
        print(f"Company Name : {self.company}, Ram : {self.ram}, Storage : {self.storage}, Category : {Mobile.category}")

m1 = Mobile("Samsung", 8, 128)
m2 = Mobile("Apple", 6, 256)

m1.display_mobile()
m2.display_mobile()



#& 🔴 Question 5 – BankAccount Class

#? Create a class named `BankAccount`.

#* Create a class variable:
#~    `bank_name = "State Bank of India"`

#* Constructor should take:
#~    `account_holder`
#~    `balance`

#* Create an instance method:
#~    `display_account()`
#~    Display:
#^           Account Holder
#^           Balance
#^           Bank Name

# * Create **2 BankAccount objects**.
# * Call the `display_account()` method for both objects.

class BankAccount:

    bank_name = "State Bank of India"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_account(self):
        print(f"Bank Name : {BankAccount.bank_name}, Account Holder : {self.account_holder}, Balance : {self.balance}")


b1 = BankAccount("Pravin", 50000)
b2 = BankAccount("Rahul", 35000)

b1.display_account()
b2.display_account()



#& 🔴 Question 6 – Laptop Class

#? Create a class named `Laptop`.

#* Create a class variable:
#~    `brand_type = "Business Laptop"`

#* Constructor should take:
#~    `brand`
#~    `processor`
#~    `ram`

#* Create an instance method:
#~    `display_specs()`
#~     Display:
#^            Brand
#^            Processor
#^            RAM
#^            Brand Type

# * Create **2 Laptop objects**.
# * Call the `display_specs()` method for both objects.

class Laptop:

    brand_type = "Business Laptop"

    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    def display_specs(self):
        print(f"Brand Name : {self.brand}, Brand Type : {Laptop.brand_type}, Processor : {self.processor}, RAM : {self.ram}")

l1 = Laptop("Dell", "Intel i5", 8)
l2 = Laptop("HP", "Intel i7", 16)

l1.display_specs()
l2.display_specs()



#& 🔴 Question 7 – Book Class

#? Create a class named `Book`.

#* Create a class variable:
#~    `language = "English"`

#* Constructor should take:
#~    `title`
#~    `author`
#~    `price`

#* Create an instance method:
#~    `display_book()`
#~     Display:
#^             Title
#^             Author
#^             Price
#^             Language

# * Create **2 Book objects**.
# * Call the `display_book()` method for both objects.

class Book:

    language = "English"

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print(f"Title of Book {self.title}, Name of Author : {self.author}, Price : {self.price}, Language : {Book.language}")
    
b1 = Book("Python Basics", "Guido van Rossum", 800)
b2 = Book("Data Science", "Andrew Ng", 1200)

b1.display_book()
b2.display_book()



#& 🔴 Question 8 – Patient Class

#? Create a class named `Patient`.

#* Create a class variable:
#~    `hospital_name = "City Hospital"`

#* Constructor should take:
#~    `patient_name`
#~    `age`
#~    `disease`

#* Create an instance method:

#~    `display_patient()`
#~    Display:
#^            Patient Name
#^            Age
#^            Disease
#^            Hospital Name

# * Create **2 Patient objects**.
# * Call the `display_patient()` method for both objects.

class Patient:

    hospital_name = "City Hospital"

    def __init__(self, patient_name, age, disease):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease

    def display_patient(self):
        print(f"Hospital Name : {Patient.hospital_name}, Patient Name : {self.patient_name}, Age : {self.age}, Disease : {self.disease}")


p1 = Patient("Pravin", 22, "Fever")
p2 = Patient("Rahul", 25, "Cold")

p1.display_patient()
p2.display_patient()



#& 🔴 Question 9 – ATM Class

#? Create a class named `ATM`.

#* Create a class variable:
#~    `bank_name = "HDFC Bank"`

#* Constructor should take:
#~    `account_holder`
#~    `balance`

#* Create the following instance methods:
#~    `deposit(amount)`
#~    `withdraw(amount)`
#~    `display_balance()`
#~     Display:
#^             Account Holder
#^             Balance
#^             Bank Name

# * Create **2 ATM objects**.
# * Call all methods for both objects.

class ATM:

    bank_name = "HDFC Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposit successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdraw successfully.")
        else:
            print('Insufficient Balace')

    def display_balance(self):
        print(f"{self.account_holder}'s balance is ₹{self.balance}")

a1 = ATM("Pravin", 40000)
a2 = ATM("Rahul", 30000)

a1.deposit(5000)
a2.deposit(10000)

a1.withdraw(7000)
a2.withdraw(5000)

a1.display_balance()
a2.display_balance()



#& 🔴 Question 10 – CollegeStudent Class

#? Create a class named `CollegeStudent`.

#* Create a class variable:
#~    `university = "Monark University"`

#* Constructor should take:
#~    `name`
#~    `roll_no`
#~    `semester`

#* Create an instance method:
#~    `display_student()`
#~     Display:
#^             Name
#^             Roll Number
#^             Semester
#^             University Name

# * Create **2 CollegeStudent objects**.
# * Call the `display_student()` method for both objects.

class CollegeStudent:

    university = "Monark University"

    def __init__(self, name, roll_no, semester):
        self.name = name
        self.roll_no = roll_no
        self.semester = semester

    def display_student(self):
        print(f"university Name : {CollegeStudent.university}, Srudent Name : {self.name}, Roll No. : {self.roll_no}, Semester : {self.semester}")

c1 = CollegeStudent("Pravin", 101, 3)
c2 = CollegeStudent("Rahul", 102, 5)

c1.display_student()
c2.display_student()
