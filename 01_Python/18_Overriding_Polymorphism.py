 #! ============================
#! Chapter 8 – Polymorphism
#! ============================


#? What is Polymorphism?

#^ Poly     = Many (Bahut)
#^ Morphism = Forms (Roop)

#~ Polymorphism ka matlab hai:
#~ Ek hi method ya operation different objects ke liye
#~ different behavior dikhaye.

#~ Yaad rakhne wali line:
#~ "One Interface, Many Forms."


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ek Remote Control hai.

#^ Power Button
#*      │
#*      ▼
#^ TV  → ON
#^ AC  → ON
#^ Fan → ON

#~ Button same hai.
#~ Result alag hai.
#~ Ye hi Polymorphism hai.


#& ----------------------------------------
#& Why do we use Polymorphism?
#& ----------------------------------------

#? Without Polymorphism

#^ student_display()
#^ teacher_display()
#^ employee_display()
#^ manager_display()

#~ Har class ka method alag hoga.
#~ Code bada aur difficult ho jayega.


#? With Polymorphism

#^ display()

#~ Sab classes me same method hoga.
#~ Har class apna output degi.
#~ Code simple aur reusable ban jayega.


#& ----------------------------------------
#& Benefits of Polymorphism
#& ----------------------------------------

#~ ✅ Code Reuse
#~ ✅ Less Code
#~ ✅ Easy Maintenance
#~ ✅ Flexible Program
#~ ✅ Easy to Read
#~ ✅ Easy to Extend


#& ----------------------------------------
#& Concepts Covered in this Chapter
#& ----------------------------------------

#^ Chapter 8 – Polymorphism

#^ ├── 1. Method Overriding
#^ ├── 2. super() Function
#^ ├── 3. Duck Typing
#^ └── 4. Operator Overloading

#~ Note:
#~ super() is NOT a type of polymorphism.
#~ It is a built-in function used with
#~ inheritance and method overriding.


#& ----------------------------------------
#& Method Overriding (Introduction)
#& ----------------------------------------

#~ Definition:
#~ Jab Parent aur Child class dono me same method ho
#~ aur Child class Parent ke method ki apni implementation
#~ de, usse Method Overriding kehte hain.


#? Diagram

#^ Animal
#*    │
#^ sound()
#*    │
#*    ▼
#^ Dog
#^ sound()

#~ Child class Parent ke method ko
#~ apni requirement ke hisaab se modify karti hai.


#& Rules

#~ ✔ Parent aur Child me same method name hona chahiye.
#~ ✔ Child class Parent ko inherit kare.
#~ ✔ Child apni implementation likhe.
#~ ✔ Same parameters rakhna best practice hai.


#& Advantage

#~ Child class apna behavior define kar sakti hai.
#~ Isi wajah se program flexible banta hai.


#& ----------------------------------------
#& Inheritance vs Polymorphism
#& ----------------------------------------

#^ Inheritance
#~ • Parent se Child properties lena.
#~ • Code Reuse.
#~ • Relationship create karta hai.


#^ Polymorphism
#~ • Same method different behavior.
#~ • Flexibility provide karta hai.
#~ • Runtime me behavior change karta hai.


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Beginners ke liye confusing ho sakta hai.
#~ ❌ Debugging thodi difficult ho sakti hai.


#& ----------------------------------------
#& Chapter Flow
#& ----------------------------------------

#^ Polymorphism
#*      │
#*      ├── Method Overriding
#*      ├── super() Function
#*      ├── Duck Typing
#*      └── Operator Overloading



#^ Assignment:

#& 🔴 Question 1 – Person → Student

#* Create a class named Person.
#* Create a method:
#* introduce()
#^    Print "I am a Person".

#* Create a class named Student that inherits from Person.
#* Override the introduce() method.
#^    Print "I am a Student".

#* Create a Student object and call introduce().

class Person:

    def introduce(self):
        print("I am a Person")

class Student(Person):

    def introduce(self):
        print("I am a Student")

student = Student()

student.introduce()  




#& 🔴 Question 2 – Bird → Parrot

#* Create a class named Bird.
#* Create a method:
#* fly()
#^    Print "Bird can fly".

#* Create a class named Parrot that inherits from Bird.
#* Override the fly() method.
#^    Print "Parrot flies and talks".

#* Create a Parrot object and call fly().

class Bird:

    def fly(self):
        print("Bird can Fly")

class Parrot(Bird):

    def fly(self):
        print("Parrot flies and talks")

parrot = Parrot()

parrot.fly()




#& 🔴 Question 3 – Mobile → Smartphone

#* Create a class named Mobile.
#* Create a method:
#* features()
#^    Print "Mobile can make calls".

#* Create a class named Smartphone that inherits from Mobile.
#* Override the features() method.
#^    Print "Smartphone can make calls, browse the internet, and use apps".

#* Create a Smartphone object and call features().

class Mobile:

    def features(self):
        print("Mobile can make calls")

class Smartphone(Mobile):

    def features(self):
        print("Smartphone can make calls, browse the internet, and use apps")

moto = Smartphone()

moto.features()




#& 🔴 Question 4 – Payment → CreditCardPayment

#* Create a class named Payment.
#* Create a method:
#* pay()
#^    Print "Payment Processing".

#* Create a class named CreditCardPayment that inherits from Payment.
#* Override the pay() method.
#^    Print "Payment Done using Credit Card".

#* Create a CreditCardPayment object and call pay().

class Payment:

    def pay(self):
        print("Payment Processing")

class CreditCardPayment(Payment):

    def pay(self):
        print("Payment Done using Credit Card")

ccp = CreditCardPayment()

ccp.pay()




#& 🔴 Question 5 – Animal → Lion

#* Create a class named Animal.
#* Create a method:
#* sound()
#^    Print "Animal makes a sound".

#* Create a class named Lion that inherits from Animal.
#* Override the sound() method.
#^    Print "Lion Roars".

#* Create a Lion object and call sound().

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Lion(Animal):

    def sound(self):
        print("Lion Roars")

lion = Lion()

lion.sound()