 #! ==========================================
#! super() Function
#! ==========================================


#? What is super()?

#~ super() is a built-in function in Python.

#~ Ye Child class ke andar Parent class ke
#~ constructor (__init__) ya methods ko
#~ call karne ke liye use hota hai.

#~ Simple Line:
#~ Child class se Parent class ko access karna.


#& ----------------------------------------
#& Why do we use super()?
#& ----------------------------------------

#~ Jab Parent class me pehle se code likha hua ho,
#~ aur Child class us code ko dobara use karna chahe,
#~ tab super() use kiya jata hai.

#~ Isse code duplicate nahi hota.


#& ----------------------------------------
#& Where is super() used?
#& ----------------------------------------

#? 1. Parent Constructor

#^ super().__init__()


#? 2. Parent Method

#^ super().display()

#^ super().show()

#^ super().start()


#& ----------------------------------------
#& Without super()
#& ----------------------------------------

#~ Parent ka code manually dobara likhna padega.
#~ Code duplication ho sakta hai.
#~ Maintenance difficult ho jati hai.


#& ----------------------------------------
#& With super()
#& ----------------------------------------

#~ Parent ka existing code directly use ho jata hai.
#~ Code Reuse hota hai.
#~ Program clean aur readable banta hai.


#& ----------------------------------------
#& Advantages of super()
#& ----------------------------------------

#~ ✔ Code Reuse
#~ ✔ Less Code
#~ ✔ Easy Maintenance
#~ ✔ Better Readability
#~ ✔ Parent class ka code easily access hota hai.


#& ----------------------------------------
#& Important Note
#& ----------------------------------------

#~ super() is NOT a type of Polymorphism.

#~ Ye Python ka built-in function hai,
#~ jo Inheritance aur Method Overriding ke
#~ saath use kiya jata hai.


#& ----------------------------------------
#& Interview Point
#& ----------------------------------------

#? What is super()?

#~ super() is a built-in Python function used
#~ to call the parent class constructor or methods
#~ from the child class.



#^ Assignment :

#& 🔴 Question 1 – Animal → Dog

#* Create a class named Animal.
#* Create a method:
#* sound()
#^    Print "Animal makes a sound".

#* Create a class named Dog that inherits from Animal.

#* Override the sound() method.
#^    First call the Parent method using super().sound().
#^    Then print "Dog Barks".

#* Create a Dog object and call sound().

class Animal:

    def sound(self):
        return("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print(f"{super().sound()}, Dog Barks.")


dog = Dog()

dog.sound()




#& 🔴 Question 2 – Employee → Manager

#* Create a class named Employee.
#* Create a method:
#* work()
#^    Print "Employee is Working".

#* Create a class named Manager that inherits from Employee.

#* Override the work() method.
#^    First call the Parent method using super().work().
#^    Then print "Manager is Managing the Team".

#* Create a Manager object and call work().

class Employee:

    def work(self):
        print("Employee is Working")

class Manager(Employee):

    def work(self):
        super().work()
        print("Manager is Managing the Team")

manager = Manager()

manager.work()


#& 🔴 Question 3 – Device → Laptop

#* Create a class named Device.
#* Create a method:
#* power_on()
#^    Print "Device Power ON".

#* Create a class named Laptop that inherits from Device.

#* Override the power_on() method.
#^    First call the Parent method using super().power_on().
#^    Then print "Laptop Booting Windows".

#* Create a Laptop object and call power_on().

class Device:

    def power_on(self):
        return("Device Power ON")

class Laptop(Device):

    def power_on(self):
        print(f"{super().power_on()}, Laptop Booting Windows")

acer = Laptop()

acer.power_on()


#& 🔴 Question 4 – BankAccount → SavingsAccount

#* Create a class named BankAccount.
#* Create a method:
#* account_info()
#^    Print "General Bank Account".

#* Create a class named SavingsAccount that inherits from BankAccount.

#* Override the account_info() method.
#^    First call the Parent method using super().account_info().
#^    Then print "Savings Account with Interest Facility".

#* Create a SavingsAccount object and call account_info().

class BankAccount:

    def account_info(self):
        print("General Bank Account")

class SavingsAccount(BankAccount):

    def account_info(self):
        super().account_info()
        print("Savings Account with Interest Facility")

saving_account = SavingsAccount()

saving_account.account_info()





#& 🔴 Question 5 – Shape → Rectangle

#* Create a class named Shape.
#* Create a method:
#* draw()
#^    Print "Drawing Shape".

#* Create a class named Rectangle that inherits from Shape.

#* Override the draw() method.
#^    First call the Parent method using super().draw().
#^    Then print "Drawing Rectangle".

#* Create a Rectangle object and call draw().


class Shape:

    def draw(self):
        return("Drawing Shape")

class Rectangle(Shape):

    def draw(self):
        print(f"{super().draw()}, Drawing Rectangle")

rectangle = Rectangle()

rectangle.draw()
