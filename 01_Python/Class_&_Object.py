 #! Chapter 1 :- Class & Object 

#& Introduction :-

#~ Ab tak hum Python me Variables, Data Types, Operators, Loops aur Functions padh chuke hain. 
#~ In sab ka use karke hum chhote-chhote programs aasani se bana sakte hain.
#~ Lekin jab hume kisi bade project jaise College Management System, Bank Management System, Hospital Management System ya E-Commerce Website banana hota hai, 
#~ tab sirf variables aur functions ka use karna enough nahi hota. Code bahut bada, confusing aur difficult to manage ho jata hai.
#~ Isi problem ko solve karne ke liye Object-Oriented Programming (OOP) ka use kiya jata hai.



#& OOP Kya Hai?

#~ OOP (Object-Oriented Programming) ek programming paradigm (style) hai jisme hum program ko Objects ke around design karte hain.

#? Simple language me :-

#~ Real-world ki cheezon ko programming me represent karna hi OOP hai.
#~ Real life me har jagah objects hote hain, jaise:

#^ Student
#^ Car
#^ Mobile
#^ Laptop
#^ Employee
#^ Bank Account
#^ Book

#~ Programming me bhi in sab ko Object ke roop me represent kiya jata hai.




#& OOP Ki Need Kyu Padi?

#~ Maan lo tumhe ek college ka software banana hai.
#~ College me 5000 students hain.
#~ Agar tum bina OOP ke kaam karoge to har student ke liye alag-alag variables banane padenge.

#? Jaise:

#^ Student 1 ka naam
#^ Student 1 ki age
#^ Student 1 ke marks
#^ Student 2 ka naam
#^ Student 2 ki age
#^ Student 2 ke marks

#~ Aise hi hazaron variables ban jayenge.


#? Is tarah ka code:

#~ Bahut bada ho jayega.
#~ Manage karna mushkil hoga.
#~ Baar-baar repeat hoga.
#~ Errors aane ke chances badh jayenge.
#~ Isi liye OOP ka use kiya jata hai.



#& OOP Ka Main Idea

#~ Har Real-World Object ke paas do cheeze hoti hain.

#? 1. Properties (Data)

#~ Properties ka matlab object ki information.


#* Example:

#~ Agar object Mobile hai to uski properties ho sakti hain:

#^ Brand
#^ Model
#^ Color
#^ RAM
#^ Storage
#^ Price

#~ Programming me inhe Attributes ya Variables bhi bolte hain.



#? 2. Behaviour (Action)

#~ Behaviour ka matlab object kya-kya kaam kar sakta hai.

#* Example:

#~ Mobile ke behaviours:

#^ Call karna
#^ Camera open karna
#^ Music chalana
#^ Internet use karna
#^ SMS bhejna

#~ Programming me inhe Methods bola jata hai.



#& Class Kya Hoti Hai ?

#~ Class OOP ka sabse important concept hai.

#? Definition :-

#~ Class ek Blueprint, Design ya Template hoti hai jiske basis par Objects create kiye jate hain.

#? Simple Hinglish me:

#~ Class khud koi real object nahi hoti.
#~ Ye sirf ek design hoti hai jo batati hai ki object:

#^ Kaisa dikhega
#^ Uske paas kaunsi information hogi
#^ Wo kaun-kaun se kaam kar sakega
#^ Blueprint Example

#~ Jab koi engineer ghar banata hai to sabse pehle ghar ka design banata hai.
#~ Us design ko Blueprint kehte hain.
#~ Us ek Blueprint se bahut saare ghar banaye ja sakte hain.

#? Yaha:

#^ Blueprint = Class
#^ House = Object
#^ Matlab ek Class se bahut saare Objects ban sakte hain.



#& Object Kya Hota Hai?

#~ Object is an instance of a class.


#? Simple Hinglish me:

#~ Class sirf Design hoti hai.
#~ Jab us Design ke basis par koi actual cheez create hoti hai to usse Object kehte hain.

#? Example:

#~ Class ka naam hai Car.
#~ Us class ke Objects ho sakte hain:

#^ BMW
#^ Audi
#^ Tesla
#^ Mahindra

#~ Sab alag-alag Objects hain.



#& Instance Kya Hota Hai?

#~ Instance ka matlab hota hai:
#~ Jo Object kisi Class se create hua ho use Instance kehte hain.

#? Example:

#~ Student ek Class hai.
#~ Pravin ek Student Object hai.
#~ Isliye hum bolenge:
#~ Pravin is an instance of Student class.
#~ Yani Object aur Instance ka meaning almost same hota hai.



#? Class Aur Object Me Difference

#~ Class ek Blueprint hoti hai.
#~ Object us Blueprint ka Real Version hota hai.
#~ Class ek Design hai.
#~ Object ek Actual Product hai.
#~ Class ek baar banayi jati hai.
#~ Usse bahut saare Objects create kiye ja sakte hain.
#~ Object Ke Do Main Parts
#~ Har Object ke paas do cheeze hoti hain.



#& Data (Attributes)

#~ Ye Object ki information hoti hai.

#? Example:

#~ Student ke Data:

#^ Name
#^ Age
#^ Course
#^ Marks

#~ Ye sab Attributes hain.



#& Behaviour (Methods)

#~ Ye Object ke Actions hote hain.

#? Example:

#~ Student kya kar sakta hai?

#^ Study
#^ Attend Class
#^ Give Exam
#^ Submit Assignment

#~ Programming me inhe Methods kehte hain.



#! Real Life Examples

#& Student

#* Student ke Attributes:

#^ Name
#^ Age
#^ Roll Number
#^ Course
#^ Marks

#* Student ke Methods:

#^ Study
#^ Attend Class
#^ Give Exam
#^ Submit Assignment

#& Car

#* Car ke Attributes:

#^ Brand
#^ Color
#^ Engine
#^ Price

#* Car ke Methods:

#^ Start
#^ Brake
#^ Stop
#^ Horn

#& Bank Account

#* Bank Account ke Attributes:

#^ Account Number
#^ Balance
#^ IFSC Code
#^ Customer Name

#* Bank Account ke Methods:

#^ Deposit
#^ Withdraw
#^ Transfer
#^ Check Balance



#& Class Kyu Use Karte Hain?

#~ Agar Class use nahi karenge to har Student ke liye alag Variables aur Functions likhne padenge.
#~ Ye bahut difficult ho jayega.
#~ Agar Class use karenge to sirf ek Student Class banegi aur usse jitne chahe Students create kar sakte hain.

#? Isse:

#^ Code Reusable ho jata hai.
#^ Code Organized rehta hai.
#^ Maintenance easy ho jati hai.
#^ Large Projects banana easy ho jata hai.
#^ Class Ke Advantages
#^ Code Reuse hota hai.
#^ Code Organized rehta hai.
#^ Code Maintain karna easy hota hai.
#^ Large Projects banana easy hota hai.
#^ Real-World Objects ko represent karna easy ho jata hai.
#^ Team me kaam karna easy hota hai.
#^ Important Terms



#! Syntax of Class & Object 

# class ClassName:

#     def method_name(self):
#         # Code


# object_name = ClassName()

# object_name.method_name()



#^ Assignment :-


#& 🟢 Question 1 – Student Class

#? Create a class named `Student`.

#* - Create one object of the class.
#* - Create a method named `display()`.
#* - The method should print:

# ```text
# Welcome to Python OOP
# ```

class Student:

    def display(self):
        print('Welcome to Python OOP')

s1 = Student()
s1.display()



#& 🟢 Question 2 – Car Class

#? Create a class named `Car`.

#* - Create two objects:
#*   - BMW
#*   - Audi
#* - Create a method named `start()`.
#* - The method should print:

# ```text
# Car Started
# ```

class Car:

    def start(self):
        print('Car Started')

BMW = Car()
Audi = Car()

BMW.start()
Audi.start()



#& 🟢 Question 3 – Mobile Class

#? Create a class named `Mobile`.

#* - Create three objects.
#* - Create one method named `call()`.
#* - The method should print:

# ```text
# Calling...
# ```

class Mobile:

    def call(self):
        print('Calling...')

mob1 = Mobile()
mob2 = Mobile()
mob3 = Mobile()

mob1.call()
mob2.call()
mob3.call()



#& 🟡 Question 4 – Calculator Class

#? Create a class named `Calculator`.

#* Create the following methods:
#* - `add()`
#* - `subtract()`
#* - `multiply()`

class Calculator:

    def add(self, a, b):
        print(f'Addition : {a + b}')

    def subtract(self, a, b):
        print(f'Subtraction : {a - b}')

    def multiply(self, a, b):
        print(f'Multiplication : {a * b}')

calc = Calculator()

calc.add(2, 5)
calc.subtract(4, 6)
calc.multiply(4, 7)



#& 🟡 Question 5 – Bank Class

#? Create a class named `Bank`.

#* - Create one object.
#* - Create the following methods:
#* - `deposit()`
#* - `withdraw()`
#* - `check_balance()`
#* - Each method should print a suitable message.

class Bank:
    balance = 500

    def deposit(self, n):
        self.balance = self.balance + n
        print(f"{n} Amount Deposited")

    def withdraw(self, n):
        if self.balance > n:    
            self.balance = self.balance - n
            print(f"{n}Amount Withdrawn")

        else:
            print('Insufficient balance')
   
    def check_balance(self):
        print("Balance:", self.balance)

b = Bank()

b.deposit(500)
b.check_balance()

b.withdraw(8000)
b.check_balance()



#& 🟡 Question 6 – Animal Class

#? Create a class named `Animal`.

#* - Create two objects:
#*   - Dog
#*   - Cat
#* - Create the following methods:
#*   - `eat()`
#*   - `sleep()`
#*   - `sound()`
#* - Call all methods using both objects.

class Animal:

    def eat(self):
        print('Eatting...')

    def sleep(self):
        print('Sleeping...')

    def sound(self):
        print('Sounding...')

dog = Animal()
cat = Animal()

dog.eat()
dog.sleep()
dog.sound()

print()

cat.eat()
cat.sleep()
cat.sound()



#& 🟠 Question 7 – College Class

#? Create a class named `College`.

#* Create the following methods:
#* - `admission()`
#* - `exam()`
#* - `result()`
#* - `certificate()`

#* Create two objects and call all methods using both objects.

class College:

    def admission(self):
        print("Admission Completed")

    def exam(self):
        print("Exam Started")

    def result(self):
        print("Result Declared")

    def certificate(self):
        print("Certificate Issued")

c = College()

c.admission()
c.exam()
c.result()
c.certificate()



#& 🟠 Question 8 – Laptop Class

#? Create a class named `Laptop`.

#* - Create three objects.
#* - Create the following methods:
#*   - `power_on()`
#*   - `coding()`
#*   - `shutdown()`
#*   - `restart()`
#* - Call every method using every object.

class Laptop:

    def power_on(self):
        print("Laptop Powered On")

    def coding(self):
        print("Coding Started")

    def shutdown(self):
        print("Laptop Shut Down")

    def restart(self):
        print("Laptop Restarted")

l1 = Laptop()
l2 = Laptop()
l3 = Laptop()

print()

l1.power_on()
l1.coding()
l1.shutdown()
l1.restart()

print()

l2.power_on()
l2.coding()
l2.shutdown()
l2.restart()

print()

l3.power_on()
l3.coding()
l3.shutdown()
l3.restart()



#& 🔴 Question 9 – ATM Class

#* Create a class named `ATM`.

#* Create the following methods:
#* - `insert_card()`
#* - `enter_pin()`
#* - `withdraw_cash()`
#* - `print_receipt()`

#* Create two ATM user objects.

class ATM:

    def insert_card(self):
        print("Card Inserted")

    def enter_pin(self):
        print("PIN Entered")

    def withdraw_cash(self):
        print("Cash Withdrawn")

    def print_receipt(self):
        print("Receipt Printed")

a = ATM()
b = ATM()

a.insert_card()
a.enter_pin()
a.withdraw_cash()
a.print_receipt()

print()

b.insert_card
b.enter_pin()
b.withdraw_cash()
b.print_receipt()



#& 🔴 Question 10 – Hospital Class

#? Create a class named `Hospital`.

#* Create the following methods:
#* - `registration()`
#* - `doctor_checkup()`
#* - `medicine()`
#* - `payment()`
#* - `discharge()`

#* Create three patient objects.

class Hospital:
    
    def registration(self):
        print("Patient Registered")

    def doctor_checkup(self):
        print("Doctor Checkup Completed")

    def medicine(self):
        print("Medicine Provided")

    def payment(self):
        print("Payment Completed")

    def discharge(self):
        print("Patient Discharged")

a = Hospital()
b = Hospital()
c = Hospital()

a.registration()
a.doctor_checkup()
a.medicine()
a.payment()
a.discharge()

print()

b.registration()
b.doctor_checkup()
b.medicine()
b.payment()
b.discharge()

print()

c.registration()
c.doctor_checkup()
c.medicine()
c.payment()
c.discharge()
