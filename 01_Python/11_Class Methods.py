 #! Class Method (`@classmethod`)

#& Class Method kya hota hai?

#~ Class Method ek aisa method hota hai jo class ke data (class variables) ke saath kaam karta hai.
#~ Normal instance method me hum `self` use karte hain.
#~ Class method me hum `cls` use karte hain.

#^ Syntax:

#* class ClassName:

#*     class_variable = value

#*     @classmethod
#*     def method_name(cls):
#*         # class variable access
#*         pass



#& `self` vs `cls`

#^ Instance Method

#* def display(self):
#*     print(self.name)

#~ `self` current object ko represent karta hai.
#~ Instance variables ke liye use hota hai.

#? Example:

#* student.name
#* student.age



#^ Class Method

#* @classmethod
#* def change_college(cls):
#*     print(cls.college_name)

#~ `cls` current class ko represent karta hai.
#~ Class variables ke liye use hota hai.

#? Example:

#* Student.college_name



#& Basic Example

#* class Student:

#*     college_name = "Monark University"

#*     def __init__(self, name):
#*         self.name = name

#*     def display(self):
#*         return f"Name : {self.name}, College : {Student.college_name}"

#*     @classmethod
#*     def change_college(cls, new_name):
#*         cls.college_name = new_name


#* s1 = Student("Pravin")
#* print(s1.display())

#* Student.change_college("Gujarat University")
#* print(s1.display())



#& Yaha kya hua?

#^ Initially:

#* college_name = "Monark University"

#^ Memory:

#* Student Class
#~ |
#* └── college_name = "Monark University"



#& Class method call:

#* Student.change_college("Gujarat University")

#^ Inside:

#* cls.college_name = new_name

#^ Change:

#* Student Class
#~ |
#* └── college_name = "Gujarat University"

#~ Ab sabhi objects ko new value milegi.


#& Class Method ka use kab hota hai?

#^ Class Variable change karne ke liye

#? Example:

#* Student.change_college("ABC University")



#^ Alternative Constructor banane ke liye

#? Example:

#* class Student:

#*     def __init__(self, name, age):
#*         self.name = name
#*         self.age = age


#*     @classmethod
#*     def from_string(cls, data):
#*         name, age = data.split("-")
#*         return cls(name, int(age))


#* s1 = Student.from_string("Pravin-22")

#* print(s1.name)
#* print(s1.age)



#& Important Rules

#^ Class Method:

#? ✅ Decorator:

#* @classmethod



#? ✅ First parameter:

#* cls



#? ✅ Access:

#* cls.class_variable



#? ✅ Call:

#* ClassName.method()



#& self vs cls Comparison

#^ | Feature         | Instance Method    | Class Method     |
#* | --------------- | ------------------ | ---------------- |
#~ | Decorator       | None               | `@classmethod`   |
#~ | First Parameter | `self`             | `cls`            |
#~ | Works With      | Object             | Class            |
#~ | Access          | Instance Variables | Class Variables  |
#~ | Call            | `object.method()`  | `Class.method()` |



#^ Assignment :- 



#& 🔴 Question 1 – Student Class

#? Create a class named Student.

#* Create a class variable college_name = "Monark University".
#* Create a constructor with:
#~    name
#~    age
#* Create an instance method display_details() that returns the student's details.
#* Create a class method change_college(new_name) that changes the college name.
#* Create two student objects.
#* Display both students.
#* Change the college name to "Gujarat University" using the class method.
#* Display both students again.

class Student:
     
    college_name = "Monark University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    def display_details(self):
        return f"College Name : {Student.college_name}, Student Name : {self.name}, Age : {self.age}"

s1 = Student("Pravin", 22)
s2 = Student("Rahul", 21)

print(s1.display_details())
print(s2.display_details())

Student.change_college("Gujarat University")

print(s1.display_details())
print(s2.display_details())



# &🔴 Question 2 – Employee Class

#? Create a class named Employee.

#* Class variable: company_name = "TCS"
#* Constructor:
#~    name
#~    salary

#* Instance method:
#~    display_employee()

#* Class method:
#~    change_company(new_company)

#* Create two employee objects.
#* Display details.
#* Change company to "Infosys".
#* Display details again.

class Employee:

    company_name = "TCS"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        return f"Company Name : {Employee.company_name}, Employee Name : {self.name}, Salary : {self.salary}"

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

e1 = Employee('Pravin', 45000)
e2 = Employee('Rahul', 38000)

print(e1.display_employee())
print(e2.display_employee())

Employee.change_company("Infosys")

print(e1.display_employee())
print(e2.display_employee())



#& 🔴 Question 3 – Car Class

#? Create a class named Car.

#* Class variable: wheels = 4
#* Constructor:
#~    company
#~    model

#* Instance method:
#~    display_car()

#* Class method:
#~    change_wheels(new_wheels)

#* Create two car objects.
#* Display details.
#* Change wheels to 6.
#* Display details again.

class Car:

    wheels = 4

    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display_car(self):
        return f"Company Name : {self.company}, Model : {self.model}, Wheels : {Car.wheels}"

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels

c1 = Car('BMW', 'X5')
c2 = Car('Audi', 'A6')

print(c1.display_car())
print(c2.display_car())

Car.change_wheels(6)

print(c1.display_car())
print(c2.display_car())




#& 🔴 Question 4 – BankAccount Class

#? Create a class named BankAccount.

#* Class variable: bank_name = "State Bank of India"
#* Constructor:
#~ account_holder
#~ balance

#* Instance method:
#~ display_account()

#* Class method:
#~ change_bank(new_bank)

#* Create two account objects.
#* Display details.
#* Change bank to "HDFC Bank".
#* Display details again.

class BankAccount:

    bank_name = "State Bank of India"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_account(self):
        return f"Bank Name : {BankAccount.bank_name}, Name : {self.account_holder}, Balance : {self.balance}" 

    @classmethod
    def change_bank(cls, new_bank):
        cls.bank_name = new_bank

b1 = BankAccount('Pravin', 50000)
b2 = BankAccount('Rahul', 35000)

print(b1.display_account())
print(b2.display_account())

BankAccount.change_bank("HDFC Bank")

print(b1.display_account())
print(b2.display_account())




#& 🔴 Question 5 – Laptop Class

#? Create a class named Laptop.

#* Class variable: brand_type = "Business Laptop"
#* Constructor:
#~    brand
#~    processor

#* Instance method:
#~    display_specs()

#* Class method:
#~    change_brand_type(new_type)

#* Create two laptop objects.
#* Display details.
#* Change brand type to "Gaming Laptop".
#* Display details again.

class Laptop:

    brand_type = "Business Laptop"

    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

    def display_specs(self):
        return f"Laptop Name : {self.brand}, Processor : {self.processor}, Brand Type : {Laptop.brand_type}"

    @classmethod
    def change_brand_type(cls, new_type):
        cls.brand_type = new_type

l1 = Laptop('Dell', 'Intel i5')
l2 = Laptop('HP', 'Intel i7')

print(l1.display_specs())
print(l2.display_specs())

Laptop.change_brand_type('Gaming Laptop')

print(l1.display_specs())
print(l2.display_specs())



#& 🔴 Question 6 – Book Class

#? Create a class named Book.

#* Class variable: language = "English"
#* Constructor:
#~    title
#~    author

#* Instance method:
#~    display_book()

#* Class method:
#~    change_language(new_language)

#* Create two book objects.
#* Display details.
#* Change language to "Hindi".
#* Display details again.

class Book:

    language = "English"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        return f"Book Title : {self.title}, Name of Author : {self.author}, Language : {Book.language}"

    @classmethod
    def change_language(cls, new_language):
        cls.language = new_language

b1 = Book('Python Basics', 'Guido van Rossum')
b2 = Book('Data Science', 'Andrew Ng')

print(b1.display_book())
print(b2.display_book())

Book.change_language('Hindi')

print(b1.display_book())
print(b2.display_book())



#& 🔴 Question 7 – Hospital Class

#? Create a class named Patient.

#* Class variable: hospital_name = "City Hospital"
#* Constructor:
#~ patient_name
#~ age

#* Instance method:
#~ display_patient()

#* Class method:
#~ change_hospital(new_name)

#* Create two patient objects.
#* Display details.
#* Change hospital name to "Apollo Hospital".
#* Display details again.

class Patient:

    hospital_name = "City Hospital"

    def __init__(self, patient_name, age):
        self.patient_name = patient_name
        self.age = age

    def display_patient(self):
        return f"Hospital Name = {Patient.hospital_name}, Patient Name : {self.patient_name}, Age : {self.age}"

    @classmethod
    def change_hospital(cls, new_name):
        cls.hospital_name = new_name

p1 = Patient('Pravin', 22)
p2 = Patient('Rahul', 21)

print(p1.display_patient())
print(p2.display_patient())

Patient.change_hospital('Apollo Hospital')

print(p1.display_patient())
print(p2.display_patient())



#& 🔴 Question 8 – ATM Class

#? Create a class named ATM.

#* Class variable: bank_name = "HDFC Bank"
#* Constructor:
#~ account_holder
#~ balance

#* Instance method:
#~ display_balance()

#* Class method:
#~ change_bank(new_bank)

#* Create two ATM account objects.
#* Display balances.
#* Change bank to "ICICI Bank".
#* Display balances again.

class ATM:

    bank_name = "HDFC Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        return f"Bank Name : {ATM.bank_name}, Name : {self.account_holder}, Balance : {self.balance}"

    @classmethod
    def change_bank(cls, new_bank):
        cls.bank_name = new_bank

a1 = ATM('Pravin', 40000)
a2 = ATM('Rahul', 30000)

print(a1.display_balance())
print(a2.display_balance())

ATM.change_bank('ICICI Bank')

print(a1.display_balance())
print(a2.display_balance())



#& 🔴 Question 9 – CollegeStudent Class

#? Create a class named CollegeStudent.

#* Class variable: university = "Monark University"
#* Constructor:
#~ name
#~ roll_no

#* Instance method:
#~ display_student()

#* Class method:
#~ change_university(new_university)

#* Create two student objects.
#* Display details.
#* Change university to "GTU".
#* Display details again.

class CollegeStudent:

    university = "Monark University"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_student(self):
        return f"University Name : {CollegeStudent.university}, STUDENT Name : {self.name}, Roll No. : {self.roll_no}"

    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

c1 = CollegeStudent('Pravin', 101)
c2 = CollegeStudent('Rahul', 102)

print(c1.display_student())
print(c2.display_student())

CollegeStudent.change_university('GTU')

print(c1.display_student())
print(c2.display_student())



#& 🔴 Question 10 – Mobile Class

#? Create a class named Mobile.

#* Class variable: country = "India"
#* Constructor:
#~ company
#~ model

#* Instance method:
#~ display_mobile()

#* Class method:
#~ change_country(new_country)

#* Create two mobile objects.
#* Display details.
#* Change country to "Japan".
#* Display details again.

class Mobile:

    country = "India"

    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display_mobile(self):
        return f"Country {Mobile.country}, Company Name : {self.company}, Model : {self.model}"

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

m1 = Mobile('Samsung', 'Galaxy S25')
m2 = Mobile('Apple', 'iPhone 17')

print(m1.display_mobile())
print(m2.display_mobile())

Mobile.change_country("Japan")

print(m1.display_mobile())
print(m2.display_mobile())
