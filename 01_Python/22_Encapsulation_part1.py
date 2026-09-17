 #! 🔵 CHAPTER – ENCAPSULATION PART-1

#& 🔵 1. What is Encapsulation?

#~ Encapsulation ka matlab hai **Data (Variables) aur Methods ko ek single unit yani Class ke andar bind karna**.

#~ Iska main purpose data ko **protect karna aur uske access ko control karna** hai.

#^ **Encapsulation = Data + Methods + Controlled Access**

#? Example:

# class BankAccount:

# def __init__(self, balance):
#     self.balance = balance

# def display_balance(self):
#     print(self.balance)


#~ Yahan:

#^ `balance` → Data

#^ `display_balance()` → Method

#^ Dono `BankAccount` class ke andar hain.



#& 🔵 2. Why do we use Encapsulation?

#~ Encapsulation ka use mainly:

#^    1. Data ko protect karne ke liye.
#^    2. Data ke access ko control karne ke liye.
#^    3. Data ko unwanted changes se bachane ke liye.
#^    4. Code ko organized rakhne ke liye.
#^    5. Code ko maintain karna easy banane ke liye.



#& 🔵 3. Access Levels in Python

#~ Python mein kisi variable ya method ke access ko indicate karne ke liye **naming conventions** use ki jaati hain.

#~ Python mein mainly 3 access levels discuss kiye jaate hain:

#^    1. Public
#^    2. Protected
#^    3. Private

#~ Ye teeno variables aur methods dono par apply ho sakte hain.



#& 🟢 4. Public Members

#~ Public member ko **class ke andar bhi aur class ke bahar bhi** access kar sakte hain.

#~ Python mein agar variable ya method ke starting mein koi underscore nahi hai, to wo by default **Public** hota hai.

#^ Syntax:

#^    self.name



#& 🟢 5. Public Variable

# class Student:

# def __init__(self, name):
#     self.name = name

# student = Student("Pravin")

# print(student.name)


#? Output:

#^    Pravin

#~ Yahan:

#^ `name` → Public Variable

#~ Isliye hum class ke bahar directly access kar sakte hain:

#^    student.name



#& 🟢 6. Public Method

# class Student:

# def display(self):
#     print("Student Details")

# student = Student()

# student.display()

#? Output:

#^    Student Details

#~ Yahan:

#^ `display()` → Public Method

#~ Is method ko bhi class ke bahar directly call kar sakte hain.

#^    student.display()



#& 🧠 Public – Remember

#^ `name` → Public Variable

#^ `display()` → Public Method

#^ No leading `_` → Public



#& 🟡 7. Protected Members

#~ Protected member ke naam ke starting mein **single underscore `_`** hota hai.

#^ Syntax:

#^    self._name

#~ Protected member ka purpose hota hai indicate karna ki ye member **class ke internal use aur child classes ke use ke liye intended hai**.

#~ Lekin Python is access ko strictly block nahi karta.



#& 🟡 8. Protected Variable

# class Student:

# def __init__(self, name):
#     self._name = name

# student = Student("Pravin")

# print(student._name)

#^ Output:

#^    Pravin

#~ Python technically `_name` ko class ke bahar access karne deta hai.

#~ Lekin `_name` ek **convention** hai.

#~ Iska meaning:

#^ **"Ye member internal use ke liye hai, ise directly access avoid karo."**



#& 🟡 9. Protected Member with Inheritance

# class Parent:

# def __init__(self):
#     self._name = "Pravin"

# class Child(Parent):

# def display(self):
#     print(self._name)

# child = Child()

# child.display()

#? Output:

#^    Pravin

#~ Yahan `Child` class apni Parent class se `_name` ko access kar rahi hai.

#~ Isliye Protected members inheritance mein useful hote hain.



#& 🧠 Protected – Remember

#^ `_name` → Protected Variable

#^ `_display()` → Protected Method

#^ Single `_` → Protected

#^ Outside access → ⚠️ Technically possible

#^ Main purpose → Internal / Child class use



#& 🔴 10. Private Members

#~ Private member ke naam ke starting mein **double underscore `__`** hota hai.

#^ Syntax:

#^    self.__name

#~ Private member ka purpose hai data ya method ko **direct outside access se restrict karna**.

#~ Python private members ke liye **Name Mangling** use karta hai.



#& 🔴 11. Private Variable

# class Student:

# def __init__(self, name):
#     self.__name = name

# student = Student("Pravin")

# print(student.__name)

#? Output:

#^    AttributeError

#~ Yahan error aayega kyunki `__name` ek Private Variable hai.

#~ Hum normally ise directly class ke bahar access nahi kar sakte.



#& 🔴 12. Private Method

# class Student:

# def __display(self):
#     print("Student Details")

# def show(self):
#     self.__display()

# student = Student()

# student.show()

#^ Output:

#^    Student Details

#~ Yahan:

#^ `__display()` → Private Method

#~ Private method ko class ke andar se access kar sakte hain.

#^    self.__display()



#& 🧠 Private – Remember

#^ `__name` → Private Variable

#^ `__display()` → Private Method

#^ Double `__` → Private

#^ Direct outside access → ❌ Normally not allowed

#^ Main purpose → Direct access ko restrict karna



#& 🔵 13. Public vs Protected vs Private

#^ | Type      | Syntax   | Outside Access            | Main Purpose                 |
#* | --------- | -------- | ------------------------  | ---------------------------- |
#~ | Public    | `name`   | ✅ Allowed               | General access               |
#~ | Protected | `_name`  | ⚠️ Technically possible  | Internal use                 |
#~ | Private   | `__name` | ❌ Normally not allowed  | Direct access restrict karna |



#& 🔵 14. Important Python Point

#~ Python mein Java/C++ ki tarah `public`, `protected`, aur `private` keywords nahi hote.

#~ Python mein naming conventions use hoti hain:

#^ `name` → Public

#^ `_name` → Protected convention

#^ `__name` → Private + Name Mangling

#~ Isliye Protected member ko Python technically bahar se access karne deta hai.

#~ Private member ke case mein Python uske naam ko internally modify karta hai.

#~ Is process ko **Name Mangling** kehte hain.



#& 🧠 15. Easy Memory Trick

#~ Underscore count yaad rakho:

#^ **0 `_` → Public**

#^ **1 `_` → Protected**

#^ **2 `__` → Private**

#? Example:

#^ `name` → 🟢 Public

#^ `_name` → 🟡 Protected

#^ `__name` → 🔴 Private



#& 🔥 16. Quick Revision

#~ **Public**

#^ Starting mein underscore nahi hota.

#^ Example → `self.name`

#^ Outside access → ✅ Allowed



#~ **Protected**

#^ Starting mein single underscore hota hai.

#^ Example → `self._name`

#^ Outside access → ⚠️ Possible, but avoid direct access



#~ **Private**

#^ Starting mein double underscore hota hai.

#^ Example → `self.__name`

#^ Outside direct access → ❌ Normally not allowed




#? Assignment :

#& 🔴 Question 1 – Student Information

#~ Create a class named `Student`.

#~ Create a constructor:

#^    name
#^    _roll_no
#^    __marks

#~ Create an object of `Student`.

#~ Print all three variables.

#~ Identify:

#^    `name` → Public

#^    `_roll_no` → Protected

#^    `__marks` → Private

# class Student:

#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self._roll_no = roll_no
#         self.__marks = marks

#     def display(self):
#         print(f"Name : {self.name}, Roll No : {self._roll_no}, Marks : {self.__marks}")

# student = Student("Pravin", 181, 74.4)

# student.display()



#& 🔴 Question 2 – Employee Details

#~ Create a class named `Employee`.

#~ Create a constructor:

#^    employee_id
#^    _department
#^    __salary

#~ Create an object of `Employee`.

#~ Identify the access level of each variable.

#^    `employee_id` → Public

#^    `_department` → Protected

#^    `__salary` → Private

# class Employee:

#     def __init__(self, employee_id, department, salary):
#         self.employee_id = employee_id
#         self._department = department
#         self.__salary = salary

#     def display(self):
#         return(f"Employee ID : {self.employee_id}, Department : {self._department}, Salary : {self.__salary}")

# employee = Employee(181, "IT", 38000)

# print(employee.display())



#& 🔴 Question 3 – Bank Account

#~ Create a class named `BankAccount`.

#~ Create a constructor:

#^    account_holder
#^    _account_type
#^    __balance

#~ Create an object of `BankAccount`.

#~ Identify which variable is:

#^    Public → account_holder

#^    Protected → _account_type

#^    Private → __balance

# class BankAccount:

#     def __init__(self, account_holder, account_type, balance):
#         self.account_holder = account_holder
#         self._account_type = account_type
#         self.__balance = balance

#     def display(self):
#         print(f"Account Holder Name : {self.account_holder}, Account Type : {self._account_type}, Balance : {self.__balance}")

# bankaccount = BankAccount("Pravin", "Saving", 38000)

# bankaccount.display()




#& 🔴 Question 4 – Student Access

#~ Create a class named `Student`.

#~ Create:

#^    Public variable → `name`

#^    Protected variable → `_roll_no`

#^    Private variable → `__marks`

#~ Create an object.

#~ Try to print all three variables from outside the class.

#~ Observe which ones can be accessed directly.

#~ Write the output/error for each access.

# class Student:

#     def __init__(self):
#         self.name = "Pravin"
#         self._roll_no = 181
#         self.__marks = 74.4

# student = Student()

# print(student.name)
# print(student._roll_no)
# print(student.__marks)




#& 🔴 Question 5 – Employee Access

#~ Create a class named `Employee`.

#~ Create:

#^    Public variable → `name`

#^    Protected variable → `_department`

#^    Private variable → `__salary`

#~ Create an object.

#~ Try to access:

#^    `employee.name`

#^    `employee._department`

#^    `employee.__salary`

#~ Identify:

#^    Which access works?

#^    Which access gives an error?

#^    Why?

# class Employee:

#     def __init__(self):
#         self.name = "Pravin"
#         self._department = "IT"
#         self.__salary = 38000
        

# employee = Employee()

# print(employee.name)
# print(employee._department)
# print(employee.__salary)




#& 🔴 Question 6 – Predict the Output

#~ Predict what will happen when this code runs:

# class Student:

# def __init__(self):
#     self.name = "Pravin"
#     self._roll_no = 101
#     self.__marks = 85


# student = Student()

# print(student.name)
# print(student._roll_no)
# print(student.__marks)

#~ Write:

#^    Output of `student.name` → Pravin

#^    Output of `student._roll_no` → 101

#^    `student.__marks` → error

#^    Why?





#& 🔴 Question 7 – Student Management

#~ Create a class named `Student`.

#~ Create a constructor:

#^    name
#^    _course
#^    __fees

#~ Create a method named `display()`.

#~ Inside `display()`:

#^    Print `name`.

#^    Print `_course`.

#^    Print `__fees`.

#~ Create an object and call `display()`.

#~ Also try accessing all three variables from outside the class.

#~ Observe the difference between **inside access and outside access**.

# class Student:

#     def __init__(self, name, course, fees):
#         self.name = name
#         self._course = course
#         self.__fees = fees

#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"Course : {self._course}")
#         print(f"Fees : {self.__fees}")

# student = Student("Pravin", "ICT", 60000)

# student.display()

# print(student.name)
# print(student._course)
# print(student.__fees)



#& 🔴 Question 8 – Employee Management

#~ Create a class named `Employee`.

#~ Create a constructor:

#^    name
#^    _department
#^    __salary

#~ Create a method named `display_employee()`.

#~ Inside the method, print all three variables.

#~ Create an object.

#~ Call `display_employee()`.

#~ Then try to access all three variables directly from outside the class.

#~ Identify the behavior of:

#^    Public

#^    Protected

#^    Private

# class Employee:

#     def __init__(self, name, department, salary):
#         self.name = name
#         self._department = department
#         self.__salary = salary

#     def display_employee(self):
#         print(f"Name : {self.name}, Department : {self._department}, Slary : {self.__salary}")

# employee = Employee("Pravin", "IT", 38000)

# employee.display_employee()

# print(f"Name :{employee.name}")
# print(f"Department : {employee._department}")
# print(f"Salary : {employee.__salary}")



#& 🔴 Question 9 – Bank Account

#~ Create a class named `BankAccount`.

#~ Create a constructor:

#^    account_holder
#^    _account_type
#^    __balance

#~ Create the following methods:

#^    `display_account()`

#~ Inside `display_account()`:

#^    Print account holder.

#^    Print account type.

#^    Print balance.

#~ Create an object.

#~ Call the method.

#~ Then try to access all three variables directly from outside the class.

#~ Explain why the access behavior is different for each variable.

# class BankAccount:

#     def __init__(self, account_holder, account_type, balance):
#         self.account_holder = account_holder
#         self._account_type = account_type
#         self.__balance = balance

#     def display_account(self):
#         print(f"Account Holder : {self.account_holder}, Account Type : {self._account_type}, Balance : {self.__balance}")


# bank_account = BankAccount("Pravin", "Savings", 10000)
# bank_account.display_account()

# print()
# print(bank_account.account_holder)
# print(bank_account._account_type)
# print(bank_account.__balance)



#& 🔴 Question 10 – Complete Comparison

#~ Create a class named `Product`.

#~ Create a constructor:

#^    name
#^    _category
#^    __price

#~ Create a method named `display_product()`.

#~ Inside the method, print all three variables.

#~ Create an object.

#~ Perform the following:

#^    1. Access `name` from outside.

#^    2. Access `_category` from outside.

#^    3. Access `__price` from outside.

#^    4. Access all three from inside the class.

#~ Finally, write:

#^    `name` → Public 

#^    `_category` → Protected 

#^    `__price` → Private

#^    Which one is technically accessible outside?

#^    Which one is intended for internal use?

#^    Which one restricts direct access?

class Product:

    def __init__(self, name, category, price):
        self.name = name
        self._category = category
        self.__price = price

    def display_product(self):
        print(f"Name : {self.name}, Category : {self._category}, Price : {self.__price}")

product = Product("Laptop", "Electronics", 80000)
product.display_product()

print()
print(product.name)         
print(product._category)    
print(product.__price)       