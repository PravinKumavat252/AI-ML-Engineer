 #! Chapter 2 :- Constructor (`__init__`) 

#& What is a Constructor?

#~ Constructor ek special method hota hai jo Object create hote hi automatically execute (call) ho jata hai.
#~ Iska main kaam Object ko initialize (starting values dena) hota hai.



#& Constructor Ki Need Kyu Hoti Hai?

#~ Maan lo hum ek Student Object banate hain.
#~ Har Student ke paas kuch basic information hogi.

#^ Name
#^ Age
#^ Course

#~ Agar Constructor na ho to hume har Object ke liye alag method call karke values set karni padengi.

#& Example:

#^ Student Create
#* ↓
#^ Name Set
#* ↓
#^ Age Set
#* ↓
#^ Course Set

#~ Ye process har object ke liye repeat hogi.
#~ Constructor ye kaam automatically kar deta hai.
#~ Isliye Constructor ka use kiya jata hai.



#& Constructor Ka Main Work

#~ Constructor ka sirf ek hi kaam hai.
#~ Object ko initialize karna.

#^ Initialization ka matlab:

#~ Object ko uski starting values dena.


#? Example:

#~ Ek Student Object bana.
#~ Constructor automatically uski initial information set kar dega.
#~ Uske baad Object use karne ke liye ready ho jata hai.



#& Python Me Constructor Ka Naam

#~ Python me Constructor ka naam fixed hota hai.

#*  __init__

#~ Ye naam Python ne pehle se define kiya hua hai.
#~ Hum Constructor ka naam change nahi kar sakte.



#& Constructor Kab Execute Hota Hai?

#~ Constructor ko hume call nahi karna padta.
#~ Jab bhi Object create hota hai,
#~ Python automatically Constructor ko execute kar deta hai.

# Flow:

#^ Class Create
#*       │
#*       ▼
#^ Object Create
#*       │
#*       ▼
#^ Constructor Automatically Execute
#*       │
#*       ▼
#^ Object Ready

#~ Ye process har naye Object ke liye hoti hai.



#& Constructor Automatically Kyu Chalta Hai?

#~ Constructor ka purpose hi initialization hai.
#~ Python chahta hai ki Object bante hi ready ho jaye.
#~ Isliye Python Constructor ko automatically call karta hai.
#~ Agar Constructor manually call hota, to programmer har baar usse call karna bhool sakta tha.
#~ Automatic execution se ye problem nahi aati.



#& Constructor Ko Manually Call Karna Padta Hai?

#~ Normal situation me **Nahi**.
#~ Jab tum Object create karte ho,
#~ Python khud Constructor ko call kar deta hai.
#~ Isliye Constructor ko manually call karne ki zarurat nahi hoti.



#& Constructor Aur Normal Method Me Difference

#? Constructor

#^ Ek Special Method hota hai.
#^ Automatically execute hota hai.
#^ Object create hote hi call hota hai.
#^ Initialization ke liye use hota hai.
#^ Naam hamesha `__init__` hota hai.


#? Normal Method

#^ Normal Method ek function ki tarah hota hai.
#^ Automatically execute nahi hota.
#^ Hume manually call karna padta hai.
#^ Alag-alag kaam perform karta hai.
#^ Naam kuch bhi ho sakta hai.



#& Constructor Ke Types

#~ Python me generally do common forms use hote hain.

#? 1. Default Constructor

#~ Jisme koi extra values pass nahi ki jati.

#~ Sirf Object initialize hota hai.



#? 2. Parameterized Constructor

#~ Jisme Object create karte time values bhi di jati hain.

#~ Jaise:
#^ Name
#^ Age
#^ Salary

#~ Ye values Constructor receive karta hai aur Object ko initialize karta hai.



#& Kya Ek Class Me Multiple Constructors Ho Sakte Hain?

#~ Nahi.
#~ Python me ek Class ke andar sirf **ek hi `__init__` method** hota hai.
#~ Agar tum do Constructors banaoge,
#~ to Python sirf last wale Constructor ko consider karega.
#~ Isliye Python me Constructor Overloading direct support nahi hoti.

 

#& Har Object Ke Liye Constructor Chalega?

#~ Haan.
#~ Jitne Objects create honge,
#~ utni baar Constructor execute hoga.


#? Example:

#~ Agar tum 5 Objects create karte ho,
#~ to Constructor bhi 5 baar execute hoga.



#& Constructor Value Return Karta Hai?

#~ Nahi.
#~ Constructor ka kaam sirf Object ko initialize karna hota hai.
#~ Ye koi value return nahi karta.



#& Constructor Ke Advantages

#~ Object automatically initialize ho jata hai.
#~ Code repeat nahi hota.
#~ Code clean aur readable hota hai.
#~ Har Object same initialization process follow karta hai.
#~ Programmer ka time bachta hai.



#& Constructor Ke Disadvantages

#~ Beginners ke liye starting me thoda confusing ho sakta hai.
#~ Har Class ko Constructor ki zarurat nahi hoti.
#~ Agar Constructor me mistake ho to sabhi Objects par effect pad sakta hai.



#? Important Points

#~ Constructor ek **Special Method** hai.
#~ Python me Constructor ka naam **`__init__`** hota hai.
#~ Constructor automatically execute hota hai.
#~ Constructor ka main kaam Object ko initialize karna hai.
#~ Constructor manually call nahi karna padta.
#~ Ek Class me sirf ek `__init__` method hota hai.
#~ Har Object ke liye Constructor dobara execute hota hai.



#! Syntax of Constructor in Python

# class ClassName:

#     def __init__(self, variable1, variable2):
#         self.variable1 = variable1
#         self.variable2 = variable2


# obj = ClassName(value1, value2)



#^ Assignment :-

#& Question 1 – Student Class

#? Create a class named Student.

#* Constructor should take:
#* name
#* age
#* Create two student objects.
#* Print both students' details.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Pravin", 22)
s2 = Student("Hiren", 20)

print(s1.name, s1.age)
print(s2.name, s2.age)



#& Question 2 – Car Class

#? Create a class named Car.

#* Constructor should take:
#* brand
#* model
#* price
#* Create three car objects and print all their details.

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

c1 = Car('Tata', 'Nexon', 1200000)
c2 = Car('Hyundai', 'Creta', 1800000)
c3 = Car('Mahindra', 'Scorpio', 2200000)

print(c1.brand, c1.model, c1.price)
print(c2.brand, c2.model, c2.price)
print(c3.brand, c3.model, c3.price)



#& Question 3 – Mobile Class

#? Create a class named Mobile.

#* Constructor should take:
#* company
#* ram
#* storage
#* battery
#* Create two mobile objects and print all information.

class Mobile:

    def __init__(self, company, ram, storage, battery):
        self.company = company
        self.ram = ram
        self.storage = storage
        self.battery = battery

m1 = Mobile('Samsung', '8 GB', '128 GB', '5000 mAh')
m2 = Mobile('OnePlus', '12 GB', '256 GB', '5500 mAh')

print(f'Company : {m1.company}, Ram : {m1.ram}, Storage : {m1.storage}, Battery : {m1.battery}')
print(f'Company : {m2.company}, Ram : {m2.ram}, Storage : {m2.storage}, Battery : {m2.battery}')



#& Question 4 – Book Class

#? Create a class named Book.

#* Constructor should take:
#* title
#* author
#* pages
#* price
#* Create three book objects and display their details.

class Book:

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

b1 = Book('Python Basics', 'Ravi Kumar', 350, 499)
b2 = Book('Data Science Handbook', 'nkit Sharma', 520, 799)
b3 = Book('AI with Python', 'Priya Patel', 410, 650)


print(f'Title : {b1.title}, Author : {b1.author}, Pages : {b1.pages}, Price : {b1.price}')
print(f'Title : {b2.title}, Author : {b2.author}, Pages : {b2.pages}, Price : {b2.price}')
print(f'Title : {b3.title}, Author : {b3.author}, Pages : {b3.pages}, Price : {b3.price}')



#& Question 5 – Employee Class

#? Create a class named Employee.

#* Constructor should take:
#* employee_id
#* name
#* department
#* salary
#* Create two employee objects and print all details.

class Employee:

    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

e1 = Employee('E101', 'Rahul', 'HR', 35000)
e2 = Employee('E102', 'Sneha', 'IT', 60000)

print(f'Employee ID : {e1.employee_id}, Name : {e1.name}, Department : {e1.department}, Salary : {e1.salary}')
print(f'Employee ID : {e2.employee_id}, Name : {e2.name}, Department : {e2.department}, Salary : {e2.salary}')



#& Question 6 – Laptop Class

#? Create a class named Laptop.

#* Constructor should take:
#* brand
#* processor
#* ram
#* storage
#* price
#* Create three laptop objects and display all details.

class Laptop:

    def __init__(self, brand, processor, ram, storage, price):
        self.brand = brand
        self.processor  = processor
        self.ram = ram
        self.storage = storage
        self.price = price

l1 = Laptop('Dell', 'Intel i5', '8 GB', '512 GB SSD', 55000)
l2 = Laptop('HP', 'Intel i7', '16 GB', '1 TB SSD', 82000)
l3 = Laptop('Lenovo', 'AMD Ryzen 7', '16 GB', '512 GB SSD', 70000)

print(f'Brand : {l1.brand}, Processor : {l1.processor}, Ram : {l2.ram}, Storage : {l1.storage}, Price : {l1.price}')
print(f'Brand : {l2.brand}, Processor : {l2.processor}, Ram : {l2.ram}, Storage : {l2.storage}, Price : {l2.price}')
print(f'Brand : {l3.brand}, Processor : {l3.processor}, Ram : {l3.ram}, Storage : {l3.storage}, Price : {l3.price}')



#& Question 7 – BankAccount Class

#? Create a class named BankAccount.

#* Constructor should take:
#* account_holder
#* account_number
#* bank_name
#* balance
#* Create two bank account objects and print all account details.

class BankAccount:

    def __init__(self, account_holder, account_number, bank_name, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.bank_name = bank_name
        self.balance = balance

b1 = BankAccount('Pravin Kumavat', 1234567890, 'SBI', 50000)
b2 = BankAccount('Hiren Nai', 9876543210, 'HDFC', 75000)

print(f'Account Holder : {b1.account_holder}, Bank Name  : {b1.bank_name}, Account Number : {b1.account_number}, Balance : {b1.balance}')
print(f'Account Holder : {b2.account_holder}, Bank Name  : {b2.bank_name}, Account Number : {b2.account_number}, Balance : {b2.balance}')



#& Question 8 – Movie Class

#? Create a class named Movie.

#* Constructor should take:
#* movie_name
#* hero
#* heroine
#* rating
#* release_year
#* Create three movie objects and display all information.

class Movie:

    def __init__(self, movie_name, hero, heroine, rating, release_year):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating
        self.release_year = release_year

m1 = Movie('3 Idiots', 'Aamir Khan', 'Kareena Kapoor', 9.2, 2009)
m2 = Movie('Pushpa', 'Allu Arjun', 'Rashmika Mandanna', 8.1, 2021)
m3 = Movie('KGF Chapter 2', 'Yash', 'Srinidhi Shetty', 8.4, 2022)

print(f'Movie Name : {m1.movie_name}, Hero : {m1.hero}, Heroine : {m1.heroine}, Rating : {m1.rating}, Release Year : {m1.release_year}')
print(f'Movie Name : {m2.movie_name}, Hero : {m2.hero}, Heroine : {m2.heroine}, Rating : {m2.rating}, Release Year : {m2.release_year}')
print(f'Movie Name : {m3.movie_name}, Hero : {m3.hero}, Heroine : {m3.heroine}, Rating : {m3.rating}, Release Year : {m3.release_year}')



#& Question 9 – Hospital Class

#? Create a class named Hospital.

#* Constructor should take:
#* patient_name
#* age
#* disease
#* doctor_name
#* room_number
#* Create two patient objects and print all details.

class Hospital:

    def __init__(self, patient_name, age, disease, doctor_name, room_number):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name
        self.room_number = room_number

h1 = Hospital('Rohan', 35, 'Dengue', "Dr. Mehta", 205)
h2 = Hospital('Neha', 28, 'Typhoid', 'Dr. Shah', 112)

print(f'Patient Name : {h1.patient_name}, Age : {h1.age}, Disease : {h1.disease}, Doctor Name : {h1.doctor_name}, Room Number : {h1.room_number}')
print(f'Patient Name : {h2.patient_name}, Age : {h2.age}, Disease : {h2.disease}, Doctor Name : {h2.doctor_name}, Room Number : {h2.room_number}')



#& Question 10 – ATM Class

#? Create a class named ATM.

#* Constructor should take:
#* account_holder
#* account_number
#* pin
#* balance
#* Create three ATM user objects and print all account information.

class ATM:

    def __init__(self, account_holder, account_number, pin, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def display(self):
        print(f'Account Holder : {self.account_holder}, Account Number : {self.account_number}, Pin : {self.pin}, Balance : {self.balance}')

a1 = ATM('Pravin Kumavat', 1234567890, 1234, 50000)
a2 = ATM('Hiren Nai', 9876543210, 5678, 75000)
a3 = ATM('Riya Sharma', 4567891230, 4321, 1200000)

a1.display()
a2.display()
a3.display()


print(f'Account Holder : {a1.account_holder}, Account Number : {a1.account_number}, Pin : {a1.pin}, Balance : {a1.balance}')
print(f'Account Holder : {a2.account_holder}, Account Number : {a2.account_number}, Pin : {a2.pin}, Balance : {a2.balance}')
print(f'Account Holder : {a3.account_holder}, Account Number : {a3.account_number}, Pin : {a3.pin}, Balance : {a3.balance}')