 #! Abstraction


#& What is Abstraction?

#~ Abstraction ka matlab hai **sirf important information dikhana aur unnecessary implementation details ko hide karna**.

#~ User ko sirf **"kya karna hai"** pata hota hai.
#~ **"Kaise ho raha hai"** ye hidden rehta hai.



#? Real Life Example

#~ Socho tum TV ka Remote use karte ho.

#^ Power Button
#^ Volume Button
#^ Channel Button

#~ Tum sirf buttons press karte ho.
#~ TV ke andar signal kaise process hota hai,
#~ wo tumhe jaanne ki zarurat nahi.

#~ Ye hi Abstraction hai.



#& Why use Abstraction?

#? Without Abstraction

#~ User ko implementation details bhi samajhni padengi.
#~ Program complex ho jayega.



#? With Abstraction

#~ User sirf required methods use karta hai.
#~ Internal implementation hidden rehti hai.
#~ Program simple aur easy to use ban jata hai.



#& Abstract Class

#~ Abstract Class ek aisi class hoti hai
#~ jiska object directly create nahi kiya ja sakta.

#~ Ye sirf dusri classes ke liye blueprint ka kaam karti hai.

#~ Abstract Class ke andar:

#^ Abstract Methods
#^ Normal Methods
#^ Constructor

#~ tino ho sakte hain.



#& Abstract Method

#~ Abstract Method ek aisa method hota hai
#~ jiska sirf declaration hota hai.

#~ Uski implementation Child Class me likhni padti hai.

#~ Agar Child Class implementation nahi degi,
#~ to uska object create nahi hoga.



#& ABC Module

#~ Python me Abstract Class banane ke liye
#~ `abc` module use hota hai.

#~ Is module se do important cheeze use karte hain:

#^ ABC
#^ @abstractmethod



#& Syntax

#* from abc import ABC, abstractmethod

#* class Shape(ABC):

#*     @abstractmethod
#*     def area(self):
#*         pass



#& Child Class

#* class Rectangle(Shape):

#*     def area(self):
#*         print("Rectangle Area")



#& Rules of Abstraction

#? 1. Abstract Class ka object create nahi kar sakte.

#? 2. Child Class ko sabhi Abstract Methods implement karne padte hain.

#? 3. Abstract Class me normal methods bhi ho sakte hain.

#? 4. Abstract Class me constructor bhi ho sakta hai.



#& Constructor in Abstract Class

#~ Abstract Class me constructor banana allowed hai.

#~ Jab Child Class ka object create hota hai,
#~ to Parent (Abstract Class) ka constructor bhi execute hota hai
#~ agar `super()` use kiya ho.



#& Method Search Order

#~ Python pehle Child Class me method dekhta hai.

#~ Agar Child ne Abstract Method implement kiya hai,
#~ to wahi execute hota hai.



#& Advantages

#? 1. Data Hiding

#~ Internal implementation hidden rehti hai.


#? 2. Better Code Structure

#~ Program clean aur organized rehta hai.


#? 3. Standard Interface

#~ Sabhi Child Classes same methods follow karti hain.


#? 4. Easy Maintenance

#~ Code maintain aur update karna easy hota hai.


#? 5. Code Reusability

#~ Common functionality Parent Class me likh sakte hain.



#& Disadvantages

#~ Thoda extra code likhna padta hai.

#~ Beginners ko pehle confusing lag sakta hai.

#~ Small projects me hamesha zaruri nahi hota.



#& Difference Between Normal Class and Abstract Class

#^ | Normal Class                     | Abstract Class                              |
#* | -------------------------------- | ------------------------------------------- |
#~ | Object create kar sakte hain     | Direct object create nahi kar sakte         |
#~ | Complete methods hote hain       | Abstract + Normal methods dono ho sakte hain|
#~ | Directly use hoti hai            | Blueprint ki tarah use hoti hai             |



#& Important Keywords

#^ | Keyword          | Meaning                                              |
#* | ---------------- | ---------------------------------------------------- |
#~ | Abstraction      | Important details dikhana, implementation hide karna |
#~ | Abstract Class   | Blueprint class, object create nahi kar sakte        |
#~ | Abstract Method  | Sirf declaration, implementation Child me hoti hai   |
#~ | ABC              | Abstract Base Class                                  |
#~ | @abstractmethod  | Method ko Abstract banata hai                        |



#^ Assignment :

#& 🔴 Question 1 – Animal Sound

#* Create an abstract class named `Animal`.

#* Import:

#^    `ABC`

#^    `abstractmethod`

#* Create an abstract method:

#* `sound()`

#^    Do not write any implementation inside the abstract method.

#* Create a child class named `Dog`.

#* Override the `sound()` method.

#^    Print `"Dog barks"`.

#* Create an object of `Dog`.

#* Call the `sound()` method.

#^    Expected Output → `Dog barks`


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        # print("Animal make noise")
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog = Dog()

dog.sound()


#& 🔴 Question 2 – Vehicle

#* Create an abstract class named `Vehicle`.

#* Create an abstract method:

#* `start()`

#* Create a child class named `Car`.

#* Override the `start()` method.

#^    Print `"Car Started"`.

#* Create an object of `Car`.

#* Call the `start()` method.

#^    Expected Output → `Car Started`

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

car = Car()

car.start()



#& 🔴 Question 3 – Shape

#* Create an abstract class named `Shape`.

#* Create an abstract method:

#* `area()`

#* Create a child class named `Rectangle`.

#* Create a constructor:

#^    `length`

#^    `width`

#* Override the `area()` method.

#^    Calculate and print the area of the rectangle.

#* Create an object of `Rectangle`.

#* Call the `area()` method.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of rectangle : {self.length * self.width}")

rectangle = Rectangle(45, 30)

rectangle.area()



#& 🔴 Question 4 – Abstract Class Object

#* Create an abstract class named `Employee`.

#* Create an abstract method:

#* `work()`

#* Create a child class named `Developer`.

#* Override the `work()` method.

#^    Print `"Developer writes code"`.

#* Try to create an object of the abstract class `Employee`.

#* Observe what happens.

#* Create an object of `Developer`.

#* Call the `work()` method.

#* Identify:

#^    `Employee` → Abstract Class

#^    `work()` → Abstract Method

#^    `Developer` → Concrete Class

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Developer writes code")

developer = Developer()

developer.work()



#& 🔴 Question 5 – Payment System

#* Create an abstract class named `Payment`.

#* Create an abstract method:

#* `pay()`

#* Create two child classes:

#^    `CreditCard`

#^    `UPI`

#* Override the `pay()` method in both classes.

#^    `CreditCard` → Print `"Payment using Credit Card"`

#^    `UPI` → Print `"Payment using UPI"`

#* Create objects of both child classes.

#* Call the `pay()` method.


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Payment using Credit Card")

class UPI(Payment):

    def pay(self):
        print("Payment using UPI")

creditcard = CreditCard()
creditcard.pay()

print()

upi = UPI()
upi.pay()



#& 🔴 Question 6 – Multiple Abstract Methods

#* Create an abstract class named `BankAccount`.

#* Create two abstract methods:

#^    `deposit()`

#^    `withdraw()`

#* Create a child class named `SavingsAccount`.

#* Implement both abstract methods.

#^    `deposit()` → Print `"Amount Deposited"`

#^    `withdraw()` → Print `"Amount Withdrawn"`

#* Create an object of `SavingsAccount`.

#* Call both methods.

#* Identify:

#^    Abstract Class

#^    Abstract Methods

#^    Concrete Class


from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):

    def deposit(self):
        print("Amount Deposited")

    def withdraw(self):
        print("Amount Withdrawn")

saving = SavingsAccount()

saving.deposit()
saving.withdraw()



#& 🔴 Question 7 – Employee Work

#* Create an abstract class named `Employee`.

#* Create a constructor:

#^    `name`

#* Create an abstract method:

#* `work()`

#* Create two child classes:

#^    `Developer`

#^    `Manager`

#* Override `work()` in both classes.

#^    `Developer` → Print `"Developer writes code"`

#^    `Manager` → Print `"Manager manages the team"`

#* Create objects of both classes.

#* Call the `work()` method.

#* Print the employee name along with their work.

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print(f"{self.name} is a Developer and writes code")

class Manager(Employee):

    def work(self):
        print(f"{self.name} is a Manager and manages the team")

developer = Developer("Pravin")
developer.work()

print()

manager = Manager("Pravin")
manager.work()



#& 🔴 Question 8 – Vehicle System

#* Create an abstract class named `Vehicle`.

#* Create two abstract methods:

#^    `start()`

#^    `stop()`

#* Create two child classes:

#^    `Car`

#^    `Bike`

#* Implement both methods in both child classes.

#^    `Car.start()` → Print `"Car Started"`

#^    `Car.stop()` → Print `"Car Stopped"`

#^    `Bike.start()` → Print `"Bike Started"`

#^    `Bike.stop()` → Print `"Bike Stopped"`

#* Create objects of `Car` and `Bike`.

#* Call both methods for each object.


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")

car = Car()
car.start()
car.stop()

print()

bike = Bike()
bike.start()
bike.stop()



#& 🔴 Question 9 – Shape System

#* Create an abstract class named `Shape`.

#* Create an abstract method:

#* `area()`

#* Create two child classes:

#^    `Circle`

#^    `Rectangle`

#* `Circle` should have:

#^    `__radius`

#* `Rectangle` should have:

#^    `__length`

#^    `__width`

#* Implement the `area()` method in both classes.

#^    Circle Area → `π × radius × radius`

#^    Rectangle Area → `length × width`

#* Create objects of both classes.

#* Call the `area()` method for both objects.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        print(f"Area of the Circle : {(22/7) * self.__radius * self.__radius}")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        print(f"Area of the Rectangle  : {self.__length * self.__width}")

circle = Circle(3)
circle.area()

print()

rectangle = Rectangle(30, 45)
rectangle.area()



#& 🔴 Question 10 – Complete Payment System

#* Create an abstract class named `Payment`.

#* Create a constructor:

#^    `amount`

#* Create two abstract methods:

#^    `pay()`

#^    `refund()`

#* Create three child classes:

#^    `CreditCard`

#^    `UPI`

#^    `Cash`

#* Implement both abstract methods in all three classes.

#^    `CreditCard.pay()` → Print `"Payment using Credit Card"`

#^    `CreditCard.refund()` → Print `"Credit Card Payment Refunded"`

#^    `UPI.pay()` → Print `"Payment using UPI"`

#^    `UPI.refund()` → Print `"UPI Payment Refunded"`

#^    `Cash.pay()` → Print `"Payment using Cash"`

#^    `Cash.refund()` → Print `"Cash Payment Refunded"`

#* Create objects of all three classes.

#* Call `pay()` and `refund()` for each object.

#* Finally identify:

#^    `Payment` → Abstract Class

#^    `pay()` → Abstract Method

#^    `refund()` → Abstract Method

#^    `CreditCard`, `UPI`, `Cash` → Concrete Classes

from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Payment using Credit Card")

    def refund(self):
        print("Credit Card Payment Refunded")

class UPI(Payment):

    def pay(self):
        print("Payment using UPI")

    def refund(self):
        print("UPI Payment Refunded")

class Cash(Payment):

    def pay(self):
        print("Payment using Cash")

    def refund(self):
        print("Cash Payment Refunded")

creditcard = CreditCard(2000)
creditcard.pay()
creditcard.refund()

print()

upi = UPI(2000)
upi.pay()
upi.refund()

print()

cash = Cash(2000)
cash.pay()
cash.refund()
