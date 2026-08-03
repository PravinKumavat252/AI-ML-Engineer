 #! Static Method (`@staticmethod`)

#& What is a Static Method?

#~ Static Method ek aisa method hota hai jo **na object se related hota hai aur na class se related hota hai.**
#~ Is method ko object ki information bhi nahi chahiye aur class ki information bhi nahi chahiye.
#~ Isliye Static Method ke andar:

#^ `self` nahi hota.
#^ `cls` nahi hota.

#~ Static Method sirf **general utility work** ke liye use hota hai.



#& Syntax

#* class ClassName:

#*     @staticmethod
#*     def method_name():
#*         print("Hello")


#? Call karne ka tarika:

#* ClassName.method_name()



#& Static Method me `self` kyu nahi hota?

#~ `self` current object ko represent karta hai.


#? Example:

#* class Student:

#*     def __init__(self, name):
#*         self.name = name

#~ Yaha har object ka alag `name` hota hai.

#* s1 → name = Pravin
#* s2 → name = Rahul

#~ Lekin Static Method kisi object ka data use hi nahi karta.
#~ Isliye usme `self` ki zarurat nahi hoti.



#& Static Method me `cls` kyu nahi hota?

#~ `cls` class ko represent karta hai.
#~ Ye Class Variable ko access ya modify karne ke liye use hota hai.

#? Example:

#* @classmethod
#* def change_college(cls):
#*     cls.college = "GTU"

#~ Lekin Static Method class ke data ko bhi use nahi karta.
#~ Isliye usme `cls` bhi nahi hota.



#& Static Method kab use karte hain?

#~ Jab method ko:

#^ Object ki information nahi chahiye.
#^ Class ki information nahi chahiye.

#~ Tab Static Method use karte hain.



#& Example 1 – Welcome Message

#* class Student:

#*     @staticmethod
#*     def welcome():
#*         print("Welcome Students")


#? Call

#* Student.welcome()



#~ Yaha sirf message print ho raha hai.
#~ Na object use hua.
#~ Na class use hui.



#& Kya Static Method Instance Variable Access kar sakta hai?

#~ No.


#? Example

#* class Student:

#*     def __init__(self, name):
#*         self.name = name

#*     @staticmethod
#*     def display():

#*         print(self.name)



#^ Reason:

#~ Static Method ke andar `self` hota hi nahi.



#& Kya Static Method Class Variable Access kar sakta hai?

#~ Directly `cls` se nahi.


#? Wrong Example

#* class Student:

#*     college = "Monark University"

#*     @staticmethod
#*     def display():

#*         print(cls.college)


#^ Reason:

#~ Static Method ke andar `cls` bhi nahi hota.
#~ Agar Class Variable Access karna ho


#* class Student:

#*     college = "Monark University"

#*     @staticmethod
#*     def display():

#*         print(Student.college)


#~ Yaha `Student.college` likha hai.
#~ Isliye ye work karega.



#& Static Method ko Call kaise karte hain?

#? Best Practice

#* Student.display()



#? Ye bhi work karega

#* s1.display()



#? Lekin professional coding aur interview me hamesha:

#* ClassName.method_name()

#~ use karna best practice hai.



#& Difference Between Three Methods

#? 1. Instance Method

#^ `self` use karta hai.
#^ Object ka data use karta hai.
#^ Instance Variable access kar sakta hai.
#^ Object se call hota hai.



#? 2. Class Method

#^  `cls` use karta hai.
#^  Class Variable use karta hai.
#^  Class Variable change kar sakta hai.
#^  Class Name se call hota hai.



#? 3. Static Method

#^  Na `self`
#^  Na `cls`
#^  Sirf utility function.
#^  Class Name se call hota hai.



#& Summary

#^ | Method          | First Parameter | Uses Object Data | Uses Class Data | Best Call            |
#* | --------------- | --------------- | ---------------- | --------------- | -------------------- |
#~ | Instance Method | `self`          | Yes              | Yes             | `object.method()`    |
#~ | Class Method    | `cls`           | No               | Yes             | `ClassName.method()` |
#~ | Static Method   | None            | No               | No              | `ClassName.method()` |




#^ Assignment :-

#& 🔴 Question 1 – Calculator Class

#? Create a class named Calculator.

#* Requirements:

#~ Create a static method add(a, b) that returns the addition of two numbers.
#~ Create a static method subtract(a, b) that returns the subtraction of two numbers.
#~ Call both methods using the class name.

# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return f"Addition : {a} + {b} : {a + b}"

#     @staticmethod
#     def subtract(a, b):
#         return f"subtraction : {a} - {b} : {a - b}"

# print(Calculator.add(10, 5))
# print(Calculator.subtract(10, 5))


    
#& 🔴 Question 2 – Number Class

#? Create a class named Number.

#^ Requirements:

#~ Create a static method check_even_odd(num).
#~ If the number is even, return "Even".
#~ Otherwise, return "Odd".
#~ Create two test cases.

# class Number:

#     @staticmethod
#     def check_even_odd(num):
#         if num % 2 == 0:
#             return f"{num} is even"
#         else:
#             return f"{num} is odd"

# print(Number.check_even_odd(10))
# print(Number.check_even_odd(15))



#& 🔴 Question 3 – Temperature Class

#? Create a class named Temperature.

#^ Requirements:

#* Create a static method celsius_to_fahrenheit(celsius).
#* Formula:
#* fahrenheit = (celsius * 9/5) + 32
#* Return the Fahrenheit value.

# class Temperature:

#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         fahrenhrit = (celsius * 9 / 5) + 32
#         return fahrenhrit

# print(Temperature.celsius_to_fahrenheit(25))



#& 🔴 Question 4 – Student Result Class

#? Create a class named StudentResult.

#^ Requirements:

#~ Create a static method calculate_percentage(marks, total_marks).
#~ Calculate percentage using:
#~ percentage = (marks / total_marks) * 100
#~ Return the percentage.

# class Result:

#     @staticmethod
#     def calculate_percentage(marks, total_marks):
#         percentage = (marks / total_marks) * 100
#         return percentage

# print(Result.calculate_percentage(450, 500))




#& 🔴 Question 5 – Bank Class

#? Create a class named Bank.

#^ Requirements:

#~ Create a static method check_loan_eligibility(age, salary).
#~ Conditions:
#~ Age >= 21 and Salary >= 30000
#~ Return:
#~ "Eligible for Loan"
#~ Otherwise:
#~ "Not Eligible for Loan"

# class Bank:

#     @staticmethod
#     def check_loan_eligibility(age, salary):
#         if age >= 21 and salary >= 30000:
#             return "Eligible for Loan"
#         else:
#             return "Not Eligible for Loan"

# print(Bank.check_loan_eligibility(25, 50000))

