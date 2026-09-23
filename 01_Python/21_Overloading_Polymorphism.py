#! ==========================================
#! Operator Overloading
#! ==========================================


#? What is Operator Overloading?

#~ Operator Overloading means
#~ Python ke existing operators (+, -, *, ==, etc.)
#~ ko apni class ke objects ke liye customize karna.

#~ Simple Line:
#~ Apni class ke objects ke liye operators ka
#~ behavior define karna.


#& ----------------------------------------
#& Why do we use Operator Overloading?
#& ----------------------------------------

#~ Python ke operators normally numbers aur strings
#~ ke saath kaam karte hain.

#~ Lekin agar hum apni class ke objects ke saath bhi
#~ operators (+, -, ==, <, >) use karna chahte hain,
#~ to Operator Overloading use karte hain.


#& ----------------------------------------
#& Example
#& ----------------------------------------

#? Integer

#^ 5 + 3
#* ↓
#^ 8


#? String

#^ "Hello" + "World"
#* ↓
#^ HelloWorld


#~ Same operator (+)
#~ Different behavior.
#~ Ye hi Operator Overloading hai.


#& ----------------------------------------
#& How does it work?
#& ----------------------------------------

#~ Jab hum likhte hain

#^ a + b

#~ To Python internally call karta hai

#^ a.__add__(b)

#~ Isi tarah har operator ka ek special (magic)
#~ method hota hai.


#& ----------------------------------------
#& Common Special (Magic) Methods
#& ----------------------------------------

#^ +      → __add__()

#^ -      → __sub__()

#^ *      → __mul__()

#^ /      → __truediv__()

#^ ==     → __eq__()

#^ <      → __lt__()

#^ >      → __gt__()

#^ print() → __str__()

#^ len()   → __len__()


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Natural and Readable Code
#~ ✔ Flexible Programming
#~ ✔ Custom Behavior for Objects
#~ ✔ Better Code Reusability
#~ ✔ Easy Maintenance
#~ ✔ Professional OOP Design


#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Beginners ke liye samajhna difficult ho sakta hai.

#~ ❌ Agar galat implementation ho,
#~ to unexpected results aa sakte hain.

#~ ❌ Bahut jyada overloading se
#~ code confusing ho sakta hai.


#& ----------------------------------------
#& Important Note
#& ----------------------------------------

#~ Operator Overloading Python ke
#~ Magic (Dunder) Methods par based hota hai.

#~ Hum directly operator ko change nahi karte.

#~ Hum us operator ke corresponding
#~ special method ko define karte hain.


#& ----------------------------------------
#& Interview Point
#& ----------------------------------------

#? What is Operator Overloading?

#~ Operator Overloading is a feature of Python
#~ that allows us to define how operators
#~ (+, -, *, ==, etc.) should behave
#~ with objects of our own classes.



#^ Assignment :

#& 🔴 Question 1 – Student Marks (__add__())

#* Create a class named Student.

#* Create a constructor:
#^    name
#^    marks

#* Overload the + operator using:
#* __add__(self, other)

#^    Return the sum of marks of both students.

#* Create two Student objects.

#* Add both objects using:
#* student1 + student2

#* Print the total marks.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student('Pravin', 78)
s2 = Student('Hiren', 80)

print(f"Total marks: {s1.__add__(s2)}")




#& 🔴 Question 2 – Product Price (__sub__())

#* Create a class named Product.

#* Create a constructor:
#^ name
#^ price

#* Overload the - operator using:
#* __sub__(self, other)

#^ Return the difference between the prices of two products.

#* Create two Product objects.

#* Subtract them using:
#* product1 - product2

#* Print the price difference.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __sub__(self, other):
        return self.price - other.price

p1 = Product('Laptop', 65000)
p2 = Product('Mobile', 25000)

difference = p1 - p2
print(F"Difference of Price between {p1.name} and {p2.name} is : {difference}")



#& 🔴 Question 3 – Rectangle (__mul__())

#* Create a class named Rectangle.

#* Create a constructor:
#^ length
#^ width

#* Overload the * operator using:
#* __mul__(self, other)

#^ Return the product of the areas of two rectangles.

#* Create two Rectangle objects.

#* Multiply them using:
#* rectangle1 * rectangle2

#* Print the result.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __mul__(self, other):
        return(self.length * other.length * self.width * other.width)
    

r1 = Rectangle(10, 5)
r2 = Rectangle(4, 3)

area = r1 * r2

print(f"Area of Rectangle : {area}")



#& 🔴 Question 4 – Employee (__str__())

#* Create a class named Employee.

#* Create a constructor:
#^ name
#^ salary

#* Overload the __str__() method.

#^ Return:
#^ "Employee: <name>, Salary: <salary>"

#* Create one Employee object.

#* Print the object directly using:
#* print(employee)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return(f"Employee : {self.name}, Salary : {self.salary}")

employee = Employee('Rohit', 50000)
print(employee)



#& 🔴 Question 5 – Library (__len__())

#* Create a class named Library.

#* Create a constructor:
#^ total_books

#* Overload the __len__() method.

#^ Return the total number of books.

#* Create one Library object.

#* Print the result using:
#* len(library)

class Library:

    def __init__(self, total_books):
        self.total_books = total_books

    def __len__(self):
        return self.total_books

    def __str__(self):
        return f"The total number of books : {self.total_books}"


library = Library(250)

print(library)
print(len(library))



#& 🟡 Question 6 – Student Marks (__add__())

#* Create a class named Student.

#* Create a constructor:
#^    name
#^    marks

#* Overload the + operator using:
#* __add__(self, other)

#^    Return a new message:
#^    "<student1 name> and <student2 name> total marks: <total>"

#* Create two Student objects.

#* Add both objects using:

#^    student1 + student2

#* Print the result.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student("Rahul", 85)
s2 = Student("Amit", 90)

result = s1 + s2

print(f"{s1.name} and  {s2.name} has total marks : {result}")



#& 🟡 Question 7 – Bank Account (__add__())

#* Create a class named BankAccount.

#* Create a constructor:
#^    account_holder
#^    balance

#* Overload the + operator.

#* Add the balances of two accounts.

#^    Return:
#^    "Total Balance: <amount>"

#* Create two bank account objects.

#* Add them using:

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

b1 = BankAccount("Pravin", 50000)
b2 = BankAccount("Hiren", 30000)

print(f"{b1.account_holder} and  {b2.account_holder} has total balance : {b1 + b2}")




#& 🟡 Question 8 – Product Quantity (__mul__())

#* Create a class named Product.

#* Create a constructor:
#^    name
#^    price
#^    quantity

#* Overload the * operator.

#* Calculate:
#^    Total Price = price × quantity

#* Return the total cost of the product.

#* Create a Product object.

#* Use:

# product * product

# (Use the object to calculate total value.)

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __mul__(self):
        return self.price * self.quantity

product = Product("Laptop", 65000, 2)

print(f"the total cost of the product : {product.price * product.quantity}")



#& 🟡 Question 9 – Employee Comparison (__eq__())

#* Create a class named Employee.

#* Create a constructor:
#^    name
#^    salary

#* Overload the == operator using:

#^    __eq__(self, other)

#* Check whether two employees have the same salary.

#* Return:

#^    True or False

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.salary == other.salary

e1 = Employee("Rahul", 50000)
e2 = Employee("Amit", 5000)

if e1 == e2:
    print(f"{e1.name} and {e2.name} do have same salary")
else:
    print(f"{e1.name} and {e2.name}do  not have same salary")
    


#& 🟡 Question 10 – Book Information (__str__())

#* Create a class named Book.

#* Create a constructor:
#^    title
#^    author
#^    price

#* Overload:

#^    __str__()

#* Return:

#^    Book: <title>, Author: <author>, Price: <price>

#* Create a Book object.

#* Print the object directly.

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return(f"Book : {self.title}, Author : {self.author}, Price : {self.price}")

book = Book("Python Basics", "Guido", 599)

print(book)



#& 🔴 Question 11 – Student Comparison (__lt__())

#* Create a class named Student.

#* Create a constructor:

#^ name
#^ marks

#* Overload the < operator using:

# __lt__(self, other)

#* Compare marks of two students.

#* Return:

# True

# if first student has fewer marks.

#* Create two Student objects.

#* Compare:

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Rahul", 95)
s2 = Student("Amit", 90)

if s1 < s2:
    print(f"{s1.name} has fewer marks than {s2.name}")
else:
    print(f"{s1.name} has more marks than {s2.name}")




#& 🔴 Question 12 – Product Comparison (__gt__())

#* Create a class named Product.

#* Create a constructor:

#^ name
#^ price

#* Overload the > operator using:

# __gt__(self, other)

#* Compare prices of two products.

#* Return:

# True

# if first product price is greater.

#* Compare:

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 65000)
p2 = Product("Mobile", 25000)

if p1 > p2:
    print(f"{p1.name} has greater price than {p2.name}")
else:
    print(f"{p2.name} has greater price than {p1.name}")



#& 🔴 Question 13 – Shopping Cart (__len__())

#* Create a class named ShoppingCart.

#* Create a constructor:

#^ items

#* Overload:

# __len__()

#* Return the total number of items in the cart.

#* Create a ShoppingCart object.

#* Use:

class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

cart = ShoppingCart(["Laptop", "Mouse", "Keyboard", "Monitor"])
print(f"the total number of items in the cart : {len(cart)}")



#& 🔴 Question 14 – Student Record (__getitem__())

#* Create a class named Student.

#* Create a constructor:

#^ name
#^ marks list

#* Overload:

# __getitem__(self, index)

#* Allow accessing marks like:

# student[0]
# student[1]

#* Return the mark at that index.

class Student:

    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def __getitem__(self, key):
        return self.marks_list[key]

student = Student("Pravin", [85, 90, 78])

print(student[0])
print(student[1])
print(student[-1])



#& 🔴 Question 15 – Calculator Object (__call__())

#* Create a class named Calculator.

#* Create a method:

# __call__(self, a, b)

#* Return the sum of two numbers.

#* Create a Calculator object.

#* Call object directly:

class Calculator:

    def __call__(self, a, b):
        return a + b

calculator = Calculator()

print(calculator(10, 20))
