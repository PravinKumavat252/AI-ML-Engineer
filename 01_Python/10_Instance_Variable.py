 #! Instance Variable

#& Instance Variable Kya Hai?

#~ Instance Variable wo variable hota hai jo **ek object ka data store karta hai.**
#~ Har object ke paas apna alag data hota hai.
#~ Isi data ko store karne ke liye Instance Variable use hota hai.
#~ Instance Variable hamesha :-

#^ self
#~ ke saath create hota hai.


#? Example

#^ self.name
#^ self.age
#^ self.salary
#^ self.price

#~ Ye sab Instance Variables hain.



#& Why?

#~ Socho tum Student class bana rahe ho.
#~ Class sirf ek blueprint hai.
#~ Real students to objects honge.


#? Example :-

#^ s1 = Student("Pravin",22)
#^ s2 = Student("Rahul",20)
#^ s3 = Student("Amit",21)

#~ Ab socho
#~ Agar teeno students ka name same hota
#~ Age same hoti
#~ To kya ye real life jaisa lagta?
#~ Nahi.
#~ Har student ka apna naam hota hai.
#~ Har student ki apni age hoti hai.
#~ Har student ke apne marks hote hain.
#~ Isi wajah se har object ke paas apna data hona chahiye.
#~ Ye data Instance Variable me store hota hai.



#& Syntax

#* self.variable_name = value


#? Example

#^ self.name = name
#^ self.age = age




#& Memory Representation


#? Student Class
#*         │
#*         ▼

#~ s1
#* │
#~ ├── name = Pravin
#~ └── age = 22


#~ s2
#* │
#~ ├── name = Rahul
#~ └── age = 20



#& Notice

#~ Dono objects ka data alag hai.
#~ Isi ko Instance Variable bolte hain.



#& Important Points

#~ Instance Variable object ka data store karta hai.
#~ Ye `self` ke through create hota hai.
#~ Har object ki apni alag copy hoti hai.
#~ Ek object ka data change karne se dusre object ka data change nahi hota.



#! self Keyword

#& self Keyword Kya Hai?

#~ `self` current object ko represent karta hai.
#~ Simple language me,
#~ Jis object ne method call kiya hai,
#~ `self` us object ki taraf point karta hai.



#& Why?

#~ Python ko kaise pata chalega ki value kis object me store karni hai?

#? Example

#^ s1 = Student("Pravin")
#^ s2 = Student("Rahul")


#~ Agar hum sirf
#~ name = name
#~ likhen
#~ To Python ko pata hi nahi chalega ki
#~ Ye value
#~ s1 ke andar store karni hai
#~ ya
#~ s2 ke andar.
#~ Isliye hum likhte hain
#~ self.name = name
#~ Ab Python samajh jata hai
#~ Current object me value store karni hai.


#?  Example

#* class Student:

#*     def __init__(self,name):

#*         self.name = name


#* Object

#* s1 = Student("Pravin")



#&  Important Points

#~ self current object ko represent karta hai.
#~ self koi keyword nahi, ek convention hai, lekin hamesha `self` hi likhna chahiye.
#~ self ke bina Instance Variable create nahi hota.



#! Instance Method

#& Instance Method Kya Hai?

#~ Jo method object ke data ke saath kaam karta hai usko Instance Method bolte hain.
#~ Har Instance Method ka first parameter
#~ self
#~ hota hai.



#& Why?

#~ Object ke paas sirf data hona enough nahi hai.
#~ Object ko kuch kaam bhi karna hota hai.


#? Example

#~ Ek Student
#~ Data :-

#^ Name
#^ Age

#~ Kaam :-

#^ Display Details
#^ Calculate Grade

#~ Ye kaam Instance Methods karte hain.



#& Example

#* class Student:

#*     def __init__(self,name):

#*         self.name = name

#*     def display(self):

#*         print(self.name)


#* s1 = Student("Pravin")

#* s1.display()



#& Important Points

#~ Instance Method object ke data par kaam karta hai.
#~ First parameter hamesha `self` hota hai.
#~ Instance Method Instance Variables ko access kar sakta hai.



#! Accessing Instance Variables

#&Accessing Instance Variables

#~ Do tarike hain.

#? 1. Inside Class

#* self.name

#& Example :-

#^ self.name



#? 2. Outside Class

#* object.variable

#& Example :-

#^ print(s1.name)



#! Modifying Instance Variables

#& Modifying Instance Variables

#~ Object banne ke baad bhi uska data change kar sakte hain.


#? Example

#* class Student:

#*     def __init__(self,name):

#*         self.name = name


#* s1 = Student("Pravin")

#* print(s1.name)

#* s1.name = "Rahul"

#* print(s1.name)



#& Why?

#~ Real life me data change hota rehta hai.
#~ Jaise

#^ Student address change
#^ Employee salary increase
#^ Product price update

#~ Isliye Instance Variable ko modify kar sakte hain.



#! Instance Variable vs Local Variable

#^ | Instance Variable                  | Local Variable                            |
#* | ---------------------------------- | ----------------------------------------- |
#~ | Object ka data store karta hai     | Sirf method ke andar use hota hai         |
#~ | self se banta hai                  | Normally banta hai                        |
#~ | Sab methods me access ho sakta hai | Sirf usi method me use hota hai           |
#~ | Object ke saath exist karta hai    | Method khatam hote hi destroy ho jata hai |


#^ Assignment :-

#& 🔴 Question 1 – Student Class

#? Create a class named Student.

#* Constructor should take:
#* name
#* age
#* course
#* Create an instance method:
#* display_info()
#* It should print all student details.
#* Create 2 student objects and call the method.

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f'Name : {self.name}, Age : {self.age}, Course : {self.course}')

s1 = Student("Pravin", 22, "BCA")
s2 = Student("Rahul", 21, "B.Tech")

s1.display()
s2.display()



#& 🔴 Question 2 – Mobile Class

#? Create a class named Mobile.

#* Constructor should take:
#* company
#* ram
#* storage
#* battery
#* Create instance methods:
#* display_mobile()
#* charge()

#* charge() should print:
#* Battery is charging...
#* Create 2 mobile objects.

class Mobile:

    def __init__(self, company, ram, storage, battery):
        self.company = company
        self.ram = ram
        self.storage = storage
        self.battery = battery

    def display_mobile(self):
        print(f'Company : {self.company}, Ram = {self.ram}, Storage : {self.storage}')

    def charge(self):
        print(f'{self.company} Mobile is Charging ({self.battery} mAh Battery)')

m1 = Mobile("Samsung", 8, 128, 5000)
m2 = Mobile("Apple", 6, 256, 4500)

m1.display_mobile()
m2.display_mobile()

m1.charge()
m2.charge()



#& 🔴 Question 3 – Car Class

#? Create a class named Car.

#* Constructor should take:
#* company
#* model
#* color
#* price
#* Create instance methods:
#* display()
#* start()
#* stop()
#* Create 2 car objects.

class Car:

    def __init__(self, company, model, color, price):
        self.company = company
        self.model = model
        self.color = color
        self.price = price

    def display(self):
        print(f'Company Name : {self.company}, Model : {self.model}, Colour : {self.color}, Price : {self.price}')

    def start(self):
        print(f"{self.company} {self.model} is Starting...")

    def stop(self):
        print(f"{self.company} {self.model} is Stopped.")

c1 = Car("BMW", "X5", "Black", 9500000)
c2 = Car("Audi", "A6", "White", 7000000)

c1.display()
c2.display()

c1.start()
c2.start()

c1.stop()
c2.stop()



#& 🔴 Question 4 – Employee Class

#? Create a class named Employee.

#* Constructor should take:
#* name
#* department
#* salary
#* Create instance methods:
#* display_details()
#* increase_salary()
#* Inside increase_salary(), increase salary by ₹5000 and display the updated salary.
#* Create 2 employee objects.

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Name : {self.name}, Department : {self.department}, Salary : {self.salary}")

    def increase_salary(self):
        self.salary += 5000
        print(f"{self.name}'s updated salary is {self.salary}")

e1 = Employee("Pravin", "IT", 40000)
e2 = Employee("Rahul", "HR", 35000)

e1.display_details()
e2.display_details()

e1.increase_salary()
e2.increase_salary()



#& 🔴 Question 5 – BankAccount Class

#? Create a class named BankAccount.

#* Constructor should take:
#* account_holder
#* account_number
#* balance
#* Create instance methods:
#* deposit(amount)
#* withdraw(amount)
#* display_balance()
#* Deposit and withdraw money using methods.

class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdraw successfully.")
        else:
            print('Insufficient Balace')

    def display_balance(self):
        print(f"{self.account_holder}'s Balance : ₹{self.balance}")

b1 = BankAccount("Pravin", 1234567890, 50000)
b2 = BankAccount("Rahul", 9876543210, 30000)

b1.deposit(10000)
b1.withdraw(5000)

b2.deposit(7000)
b2.withdraw(2000)

b1.display_balance()
b2.display_balance()



#& 🔴 Question 6 – Laptop Class

#? Create a class named Laptop.

#* Constructor should take:
#* brand
#* processor
#* ram
#* price
#* Create instance methods:
#* display_specs()
#* upgrade_ram()
#* Increase RAM by 8 GB.
#* Create 2 laptop objects.

class Laptop:

    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price

    def display_specs(self):
        print(f"{self.brand} Laptop ({self.processor}) has {self.ram} GB RAM")

    def upgrade_ram(self, upgrade_ram):
        self.ram += upgrade_ram
        print(f"{self.brand} RAM upgraded to {self.ram} GB")

l1 = Laptop("Dell", "Intel i5", 8, 55000)
l2 = Laptop("HP", "Intel i7", 16, 75000)

l1.display_specs()
l2.display_specs()

l1.upgrade_ram(2)
l2.upgrade_ram(2)



#& 🔴 Question 7 – Book Class

#? Create a class named Book.

#* Constructor should take:
#* title
#* author
#* price
#* Create instance methods:
#* display_book()
#* discount()
#* Reduce the book price by 10% and print the new price.
#* Create 2 book objects.

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print(f"Title of Book : {self.title}, Name of Author : {self.author}, Price : {self.price}")

    def discount(self):
        self.price = self.price - self.price // 10
        print(f"Discount of the book {self.title} is {self.price}")

b1 = Book("Python Basics", "Guido", 800)
b2 = Book("Data Science", "Andrew", 1200)

b1.display_book()
b2.display_book()

b1.discount()
b2.discount()



#& 🔴 Question 8 – Hospital Class

#? Create a class named Patient.

#* Constructor should take:
#* patient_name
#* age
#* disease
#* Create instance methods:
#* display_patient()
#* consult_doctor()
#* consult_doctor() should print:
#* Patient is consulting the doctor.
#* Create 2 patient objects.

class Patient:

    def __init__(self, patient_name, age, disease):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease

    def display_patient(self):
        print(f" Name of Patient : {self.patient_name}, Age : {self.age}, Disease : {self.disease}")

    def consult_doctor(self):
        print(f"{self.patient_name} is consulting the doctor.")

p1 = Patient("Pravin", 22, "Fever")
p2 = Patient("Rahul", 25, "Cold")

p1.display_patient()
p2.display_patient()

p1.consult_doctor()
p2.consult_doctor()



#& 🔴 Question 9 – ATM Class

#? Create a class named ATM.

#* Constructor should take:
#* account_holder
#* balance
#* Create instance methods:
#* withdraw(amount)
#* deposit(amount)
#* check_balance()
#* Update the balance after each transaction.

class ATM:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdraw successfully.")
        else:
            print('Insufficient Balace')

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposit successfully.")

    def check_balance(self):
        print(f"{self.account_holder}'s balance is ₹{self.balance}")

a1 = ATM("Pravin", 40000)
a2 = ATM("Rahul", 25000)

a1.deposit(5000)
a1.withdraw(7000)

a2.deposit(10000)
a2.withdraw(3000)

a1.check_balance()
a2.check_balance()



#& 🔴 Question 10 – College Class

#? Create a class named CollegeStudent.

#* Constructor should take:
#* name
#* roll_no
#* semester
#* cgpa
#* Create instance methods:
#* display_details()
#* promote_semester()
#* Increase the semester by 1 and display the updated semester.
#* Create 2 student objects.

class CollegeStudent:

    def __init__(self, name, roll_no, semester, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.semester = semester
        self.cgpa = cgpa

    def display_details(self):
        print(f"Student Name : {self.name}, Roll No. : {self.roll_no}, Semester : {self.semester}, CGPA : {self.cgpa}")

    def promote_semester(self):
        self.semester += 1
        print(f"{self.name} has been promoted to Semester {self.semester}.")

cs1 = CollegeStudent("Pravin", 101, 3, 8.2)
cs2 = CollegeStudent("Rahul", 102, 5, 7.8)

cs1.display_details()
cs2.display_details()

cs1.promote_semester()
cs2.promote_semester()
