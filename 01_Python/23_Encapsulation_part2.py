#& 🔵 CHAPTER – ENCAPSULATION PART-2

#& 🔵 1. What is Name Mangling?

#~ Python mein agar kisi variable ya method ke naam ke starting mein **double underscore `__`** hota hai, 
#~ to Python internally uska naam change kar deta hai.

#~ Is process ko **Name Mangling** kehte hain.

#? Example:

#^ `__marks` → Private Variable

#^ Internally Python ise approximately:

#^ `_Student__marks`

#~ ke form mein store karta hai.

#^ `Student` → Class Name

#^ `__marks` → Private Variable

#^ `_Student__marks` → Mangled Name




#& 🔵 2. Why is Name Mangling Used?

#~ Name Mangling ka main purpose private members ko **accidental access aur accidental overriding** se protect karna hai.

#~ Python mein Private ka matlab completely inaccessible nahi hota.

#~ Python private member ka naam internally change karta hai.

#~ Isliye:

#^ `__marks` → Direct access normally possible nahi

#^ `_Student__marks` → Internally mangled name



#& 🔵 3. Name Mangling Example

#* class Student:

    #* def __init__(self):
    #*     self.__marks = 85

#* student = Student()

#* print(student.__marks)

#? Output:

#^ `AttributeError`

#~ Yahan error aayega kyunki Python ne `__marks` ka naam internally change kar diya hai.

#~ Isliye:

#^ `student.__marks` → ❌ Direct access nahi




#& 🔵 4. Accessing Private Variable using Name Mangling

#~ Technically hum private variable ko uske mangled name se access kar sakte hain.

#* class Student:

    #* def __init__(self):
    #*     self.__marks = 85

#* student = Student()

#* print(student._Student__marks)

#? Output:

#^ `85`

#~ Lekin normally humein private variable ko is tarah access nahi karna chahiye.

#~ Private data ko access karne ke liye **Getter Method** use karna better hai.



#& 🔵 5. What is a Getter?

#~ Getter ek method hota hai jo **private variable ki value ko read/access** karne ke liye use hota hai.

#~ Getter ka main purpose private data ko **controlled way mein read karna** hai.

#? Syntax:

#* def get_variable(self):
#* return self.__variable



#& 🔵 6. Getter Example

#* class Student:

    #* def __init__(self, marks):
    #*     self.__marks = marks

    #* def get_marks(self):
    #*     return self.__marks

#* student = Student(85)

#* print(student.get_marks())


#? Output:

#^ `85`

#~ Yahan:

#^ `__marks` → Private Variable

#^ `get_marks()` → Getter Method

#^ `student.get_marks()` → Private variable ki value read karta hai.



#& 🔵 7. What is a Setter?

#~ Setter ek method hota hai jo **private variable ki value ko change/update** karne ke liye use hota hai.

#~ Setter ka main purpose private data ko **controlled way mein modify karna** hai.

#? Syntax:

#* def set_variable(self, value):
#* self.__variable = value



#& 🔵 8. Setter Example

#* class Student:

    #* def __init__(self, marks):
    #*     self.__marks = marks

    #* def set_marks(self, marks):
    #*     self.__marks = marks

#* student = Student(75)

#* student.set_marks(85)

#~ Ab:

#^ Old Value → `75`

#^ New Value → `85`

#~ `set_marks()` ne private variable ki value update kar di.



#& 🔵 9. Getter and Setter Together

#~ Getter aur Setter ko ek saath use karke private variable ka **controlled access** provide kiya ja sakta hai.

#* class Student:

    #* def __init__(self, marks):
    #*     self.__marks = marks

    #* def get_marks(self):
    #*     return self.__marks

    #* def set_marks(self, marks):
    #*     self.__marks = marks

#* student = Student(75)

#* print(student.get_marks())

#* student.set_marks(85)

#* print(student.get_marks())


#? Output:

#^ `75`

#^ `85`

#~ Working:

#^ `__marks = 75` → Initial value

#^ `get_marks()` → Value read karta hai

#^ `set_marks(85)` → Value change karta hai

#^ `get_marks()` → Updated value read karta hai



#& 🔵 10. Getter vs Setter

#^ | Point          | Getter                    | Setter                         |
#* |----------------|---------------------------|--------------------------------|
#~ | Purpose        | Private data ko read      | Private data ko modify         |
#~ | Return         | Usually return karta hai  | Usually value assign karta hai |
#~ | Value          | Existing value read karta | New value set/change karta     |
#~ | Example        | get_marks()               | set_marks(85)                  |
#~ | Main Work      | Read                      | Change                         |



#& 🔵 11. Why do we Use Getter and Setter?

#~ Getter aur Setter ka use private data ko **controlled access** dene ke liye hota hai.

#~ Iske main benefits:

#^ 1. Private data ko safely read kar sakte hain.

#^ 2. Private data ko controlled way mein modify kar sakte hain.

#^ 3. Setter ke andar validation laga sakte hain.

#^ 4. Invalid data ko prevent kar sakte hain.

#^ 5. Data ko unwanted changes se protect kar sakte hain.



#& 🔵 12. Setter with Validation

#~ Setter ke andar value change karne se pehle condition check kar sakte hain.

#~ Is process ko **Validation** kehte hain.

#* class Student:

    #* def __init__(self, marks):
    #*     self.__marks = marks

    #* def get_marks(self):
    #*     return self.__marks

#* def set_marks(self, marks):

#*     if marks >= 0 and marks <= 100:
#*         self.__marks = marks
#*     else:
#*         print("Invalid Marks")

#* student = Student(75)

#* student.set_marks(90)

#* print(student.get_marks())

#* student.set_marks(120)


#? Output:

#^ `90`

#^ `Invalid Marks`

#~ Yahan:

#^ `90` → Valid Marks

#^ `120` → Invalid Marks

#~ Setter invalid value ko private variable mein store nahi hone deta.



#& 🧠 13. What is Validation?

#~ Validation ka matlab hai **data ko store ya update karne se pehle check karna**.

#~ Example:

#^ Marks → `0 to 100`

#^ Age → Positive honi chahiye.

#^ Salary → Negative nahi honi chahiye.

#^ Balance → Negative nahi hona chahiye.

#~ Isliye Setter ke andar validation useful hoti hai.



#& 🔵 14. Real-Life Example – Bank Account

#~ Bank account mein balance ko directly change karna safe nahi hai.

#~ Isliye balance ko private rakha ja sakta hai.

#* class BankAccount:

#*     def __init__(self, balance):
#*         self.__balance = balance

#*     def get_balance(self):
#*         return self.__balance

#*     def set_balance(self, balance):

#*         if balance >= 0:
#*             self.__balance = balance
#*         else:
#*             print("Invalid Balance")

#* account = BankAccount(10000)

#* print(account.get_balance())

#* account.set_balance(15000)

#* print(account.get_balance())

#? Output:

#^ `10000`

#^ `15000`

#~ Agar:

#^ `account.set_balance(-5000)`

#~ kiya jaaye, to:

#^ `Invalid Balance`

#~ print hoga.



#& 🔵 15. Getter + Setter Complete Flow

#~ Private Variable:

#^ `__balance`


#~ Getter:

#^ `get_balance()`

#^ → Balance ko read karta hai.


#~ Setter:

#^ `set_balance()`

#^ → Balance ko change karta hai.


#~ Validation:

#^ `if balance >= 0`

#^ → Invalid balance ko prevent karta hai.


#~ Complete Flow:

#^ **Private Data → Getter → Read**

#^ **Private Data → Setter → Change**

#^ **Setter + Validation → Controlled Data**



#& 🔵 16. What is `@property`?

#~ Python mein Getter aur Setter ko aur clean way mein implement karne ke liye **`@property` decorator** use kiya ja sakta hai.

#~ `@property` ki help se method ko **variable ki tarah access** kar sakte hain.

#~ Example:

# class Student:

#     def __init__(self, marks):
#         self.__marks = marks

#     @property
#     def marks(self):
#         return self.__marks

# student = Student(85)

# print(student.marks)

#? Output:

#^ `85`

#~ Yahan:

#^ `@property` → Getter create karta hai.

#^ `marks()` → Getter Method

#^ `student.marks` → Method ko variable ki tarah access karta hai.



#& 🧠 Important Point

#~ Normal Getter:

#^ `student.get_marks()`

#~ Property Getter:

#^ `student.marks`

#~ Dono ka purpose private value ko **read** karna hai.



#& 🔵 17. Getter and Setter vs Direct Access

#~ Direct access:

#^ `student.__marks`

#^ ❌ Normally allowed nahi hai.


#~ Getter:

#^ `student.get_marks()`

#^ ✅ Private value read kar sakte hain.


#~ Setter:

#^ `student.set_marks(90)`

#^ ✅ Private value change kar sakte hain.


#~ Property:

#^ `student.marks`

#^ ✅ Getter ko variable ki tarah use kar sakte hain.



#? Assignment :


#& 🔴 Question 1 – Student Marks

#* Create a class named `Student`.

#* Create a constructor:

#^    `__marks`

#* Create a method:

#* `get_marks()`

#^    Return `__marks`.

#* Create an object of `Student`.

#* Use `get_marks()` to print the marks.

#^    Expected Output → `75`

# class Student:

#     def __init__(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

# student = Student(85)

# print(f"Student marks : {student.get_marks()}")



#& 🔴 Question 2 – Employee Salary

#* Create a class named `Employee`.

#* Create a constructor:

#^    `__salary`

#* Create a method:

#* `get_salary()`

#^    Return `__salary`.

#* Create an object of `Employee`.

#* Use `get_salary()` to print the salary.

#^    Expected Output → `38000`

# class Employee:

#     def __init__(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         return(self.__salary)

# employee = Employee(38000)

# print(f"Employee salary : {employee.get_salary()}")



#& 🔴 Question 3 – Student Marks Update

#* Create a class named `Student`.

#* Create a constructor:

#^    `__marks`

#* Create two methods:

#^    `get_marks()`

#^    `set_marks()`

#* `get_marks()` should return `__marks`.

#* `set_marks()` should update `__marks`.

#* Create an object with marks `70`.

#* Print the marks using `get_marks()`.

#* Update the marks to `85` using `set_marks()`.

#* Print the updated marks using `get_marks()`.

# class Student:

#     def __init__(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#         self.__marks = marks

# student = Student(70)
# print(f"Student marks : {student.get_marks()}")

# print()

# student.set_marks(85)
# print(f"Student marks : {student.get_marks()}")



#& 🔴 Question 4 – Bank Account

#* Create a class named `BankAccount`.

#* Create a constructor:

#^    `__balance`

#* Create two methods:

#^    `get_balance()`

#^    `set_balance()`

#* `get_balance()` should return `__balance`.

#* `set_balance()` should update `__balance`.

#* Create an object with balance `10000`.

#* Print the balance using `get_balance()`.

#* Update the balance to `15000` using `set_balance()`.

#* Print the updated balance using `get_balance()`.

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return(f"Bank Balance : {self.__balance}")

#     def set_balance(self, balance):
#         self.__balance = balance

# bank = BankAccount(10000)
# print(bank.get_balance())

# print()

# bank.set_balance(15000)
# print(bank.get_balance())



#& 🔴 Question 5 – Product Price

#* Create a class named `Product`.

#* Create a constructor:

#^    `__price`

#* Create two methods:

#^    `get_price()`

#^    `set_price()`

#* `get_price()` should return `__price`.

#* `set_price()` should update `__price`.

#* Create an object with price `50000`.

#* Print the price using `get_price()`.

#* Change the price to `55000` using `set_price()`.

#* Print the updated price using `get_price()`.

#* Identify:

#^    `__price` → Private Variable

#^    `get_price()` → Getter

#^    `set_price()` → Setter

# class Product:

#     def __init__(self, price):
#         self.__price = price

#     def get_price(self):
#         return(f"Product Price : {self.__price}")

#     def set_price(self, price):
#         self.__price = price

# product = Product(500000)
# print(product.get_price())

# print()

# product.set_price(55000)
# print(product.get_price())



#& 🔴 Question 6 – Student Name

#* Create a class named `Student`.

#* Create a constructor:

#^    `__name`

#* Create two methods:

#^    `get_name()`

#^    `set_name()`

#* `get_name()` should return `__name`.

#* `set_name()` should update `__name`.

#* Create an object with name `"Pravin"`.

#* Print the name using `get_name()`.

#* Change the name to `"Rahul"` using `set_name()`.

#* Print the updated name using `get_name()`.

# class Student:

#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return(f"Student name : {self.__name}")

#     def set_name(self, name):
#         self.__name = name

# student = Student("Pravin")
# print(student.get_name())

# print()

# student.set_name("Rahul")
# print(student.get_name())



#& 🔴 Question 7 – Employee Details

#* Create a class named `Employee`.

#* Create a constructor:

#^    `__name`

#^    `__salary`

#* Create four methods:

#^    `get_name()`

#^    `set_name()`

#^    `get_salary()`

#^    `set_salary()`

#* Getter methods should return their respective private variables.

#* Setter methods should update their respective private variables.

#* Create an object of `Employee`.

#* Print the name and salary using Getter methods.

#* Update the name and salary using Setter methods.

#* Print the updated values using Getter methods.

#* Identify:

#^    Private Variables

#^    Getter Methods

#^    Setter Methods

# class Employee:

#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary

#     def get_name(self):
#         return(f"Employee name : {self.__name}")

#     def set_name(self, name):
#         self.__name = name
        
#     def get_salary(self):
#         return(f"Employee salary : {self.__salary}")

#     def set_salary(self, salary):
#         self.__salary = salary

# employee = Employee("Pravin", 38000)
# print(employee.get_name())
# print(employee.get_salary())

# print()

# employee.set_name("Rahul")
# employee.set_salary(45000)

# print(employee.get_name())
# print(employee.get_salary())



#& 🔴 Question 8 – Student Marks Validation

#* Create a class named `Student`.

#* Create a constructor:

#^    `__marks`

#* Create two methods:

#^    `get_marks()`

#^    `set_marks()`

#* `get_marks()` should return `__marks`.

#* `set_marks()` should update `__marks`.

#* Add validation inside `set_marks()`.

#^    Marks must be between `0` and `100`.

#^    If valid → Update marks.

#^    If invalid → Print `"Invalid Marks"`.

#* Create an object with marks `75`.

#* Test the Setter with:

#^    `85` → Valid

#^    `120` → Invalid

#^    `-10` → Invalid

# class Student:

#     def __init__(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         print(f"Student's marks : {self.__marks}")

#     def set_marks(self, marks):

#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid Marks")

# student = Student(75)
# student.get_marks()

# print()

# student.set_marks(85)
# student.get_marks()

# print()

# student.set_marks(-10)
# student.set_marks(120)



#& 🔴 Question 9 – Bank Balance Validation

#* Create a class named `BankAccount`.

#* Create a constructor:

#^    `__balance`

#* Create two methods:

#^    `get_balance()`

#^    `set_balance()`

#* `get_balance()` should return `__balance`.

#* `set_balance()` should update `__balance`.

#* Add validation inside `set_balance()`.

#^    Balance cannot be negative.

#^    If valid → Update balance.

#^    If invalid → Print `"Invalid Balance"`.

#* Create an object with balance `10000`.

#* Test the Setter with:

#^    `15000` → Valid

#^    `-5000` → Invalid

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         print(f"Bank Balance : {self.__balance}")

#     def set_balance(self, balance):

#         if balance > 0:
#             self.__balance = balance
#         else:
#             print("Invalid Balance")

# bank = BankAccount(10000)
# bank.get_balance()

# print()

# bank.set_balance(15000)
# bank.get_balance()

# print()

# bank.set_balance(-5000)



#& 🔴 Question 10 – Employee Salary Management

#* Create a class named `Employee`.

#* Create a constructor:

#^    `__name`

#^    `__salary`

#* Create four methods:

#^    `get_name()`

#^    `set_name()`

#^    `get_salary()`

#^    `set_salary()`

#* Getter methods should return the respective private variables.

#* Setter methods should update the respective private variables.

#* Add validation inside `set_salary()`.

#^    Salary must be greater than `0`.

#^    If valid → Update salary.

#^    If invalid → Print `"Invalid Salary"`.

#* Create an object:

#^    Name → `"Pravin"`

#^    Salary → `38000`

#* Perform the following:

#^    1. Print name using `get_name()`.

#^    2. Print salary using `get_salary()`.

#^    3. Change name using `set_name()`.

#^    4. Change salary using `set_salary()`.

#^    5. Print updated name and salary.

#^    6. Try to set salary to `-5000`.

#^    7. Observe the validation.

#* Finally, identify:

#^    `__name` → Private Variable

#^    `__salary` → Private Variable

#^    `get_name()` → Getter

#^    `set_name()` → Setter

#^    `get_salary()` → Getter

#^    `set_salary()` → Setter

# class Employee:

#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary

#     def get_name(self):
#         print(f"Employee name : {self.__name}")

#     def set_name(self, name):
#         self.__name = name

#     def get_salary(self):
#             print(f"Employee salary : {self.__salary}")
    
#     def set_salary(self, salary):

#         if salary > 0:
#             self.__salary = salary
#         else:
#              print("Invalid Salary")

# employee = Employee("Pravin", 38000)
# employee.get_name()
# employee.get_salary()

# print()

# employee.set_name("Rahul")
# employee.set_salary(45000)

# print()

# employee.set_salary(-5000)