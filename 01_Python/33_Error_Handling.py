
#! ==========================================
#! Error Handling in Python
#! ==========================================


#? What is Error Handling?

#~ Error Handling ka matlab hai program me
#~ aane wale errors ko handle karna.

#~ Iska main purpose ye hai ki agar program me
#~ error aaye, to program suddenly crash na ho.

#~ Hum error ko handle karke user ko
#~ proper message de sakte hain.


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho ATM me tum amount withdraw karte ho.

#~ Agar account me sufficient balance nahi hai,
#~ to ATM directly band nahi hota.

#~ Instead wo message deta hai:

#^ "Insufficient Balance"

#~ Python me bhi Error Handling ka kaam
#~ kuch isi tarah hota hai.


#& ----------------------------------------
#& Why Error Handling is Used?
#& ----------------------------------------

#~ Error Handling ka use:

#~ ✔ Program ko crash hone se bachane ke liye.

#~ ✔ Errors ko properly handle karne ke liye.

#~ ✔ User ko meaningful error message dene ke liye.

#~ ✔ Program ko smoothly continue karne ke liye.

#~ ✔ Unexpected situations ko manage karne ke liye.


#& ----------------------------------------
#& Common Errors in Python
#& ----------------------------------------

#~ Python me different types ke errors
#~ aa sakte hain.

#^ 1. SyntaxError
#^ 2. NameError
#^ 3. TypeError
#^ 4. ValueError
#^ 5. ZeroDivisionError
#^ 6. IndexError
#^ 7. KeyError
#^ 8. FileNotFoundError


#& ----------------------------------------
#& Example of Error
#& ----------------------------------------

#* number = 10
#* result = number / 0

#~ Yahan ZeroDivisionError aayega.

#~ Agar error handle nahi kiya,
#~ to program terminate ho jayega.


#& ----------------------------------------
#& Error Handling Keywords
#& ----------------------------------------

#~ Python me Error Handling ke liye
#~ mainly ye keywords use hote hain:

#^ try
#^ except
#^ else
#^ finally
#^ raise


#& ----------------------------------------
#& 1. try
#& ----------------------------------------

#~ try block me hum wo code likhte hain
#~ jisme error aane ki possibility ho.

#* try:
#*     number = 10 / 0


#& ----------------------------------------
#& 2. except
#& ----------------------------------------

#~ except block error ko handle karta hai.

#* try:
#*     number = 10 / 0

#* except:
#*     print("Something went wrong")


#~ Agar try block me error aata hai,
#~ to Python except block execute karta hai.


#& ----------------------------------------
#& try + except Syntax
#& ----------------------------------------

#* try:
#*     # Risky Code

#* except:
#*     # Error Handling Code


#& ----------------------------------------
#& Example
#& ----------------------------------------

#* try:
#*     a = 10
#*     b = 0
#*     print(a / b)

#* except:
#*     print("Cannot divide by zero")


#^ Output:

#^ Cannot divide by zero


#& ----------------------------------------
#& Specific Exception
#& ----------------------------------------

#~ Hum particular error ko bhi handle
#~ kar sakte hain.

#* try:
#*     number = 10 / 0

#* except ZeroDivisionError:
#*     print("Cannot divide by zero")


#~ Ye approach better hai kyunki hum
#~ specific error ko identify kar rahe hain.


#& ----------------------------------------
#& Multiple except Blocks
#& ----------------------------------------

#~ Ek try block ke saath multiple
#~ except blocks use kar sakte hain.

#* try:
#*     number = int(input("Enter number: "))
#*     result = 10 / number

#* except ValueError:
#*     print("Please enter a valid number")

#* except ZeroDivisionError:
#*     print("Cannot divide by zero")


#~ Different errors ke liye
#~ different except blocks use hote hain.


#& ----------------------------------------
#& 3. else
#& ----------------------------------------

#~ else block tab execute hota hai
#~ jab try block successfully execute ho.

#* try:
#*     number = 10 / 2

#* except ZeroDivisionError:
#*     print("Cannot divide by zero")

#* else:
#*     print("Calculation successful")


#^ Output:

#^ Calculation successful


#~ Simple Line:

#~ try successful → else execute


#& ----------------------------------------
#& 4. finally
#& ----------------------------------------

#~ finally block hamesha execute hota hai.

#~ Error aaye ya na aaye,
#~ finally execute hoga.

#* try:
#*     number = 10 / 2

#* except ZeroDivisionError:
#*     print("Error")

#* finally:
#*     print("Program Completed")


#^ Output:

#^ Program Completed


#~ finally ka use generally
#~ cleanup operations ke liye hota hai.


#& ----------------------------------------
#& Complete try-except-else-finally
#& ----------------------------------------

#* try:
#*     number = int(input("Enter number: "))
#*     result = 100 / number

#* except ValueError:
#*     print("Invalid input")

#* except ZeroDivisionError:
#*     print("Cannot divide by zero")

#* else:
#*     print("Result:", result)

#* finally:
#*     print("Program Completed")


#& ----------------------------------------
#& Error Handling Flow
#& ----------------------------------------

#^              try
#*                │
#*                ▼
#^          Error Occurred?
#*           /           \
#*         Yes            No
#*          ↓              ↓
#^       except           else
#*          \              /
#*           \            /
#*            ▼          ▼
#^              finally
#*                  │
#*                  ▼
#^              Program End


#& ----------------------------------------
#& 5. raise
#& ----------------------------------------

#~ raise keyword ka use hum
#~ manually error generate karne ke liye karte hain.

#* age = 15

#* if age < 18:
#*     raise ValueError("Age must be 18 or above")


#~ Yahan hum khud ValueError
#~ raise kar rahe hain.


#& ----------------------------------------
#& Handling raise
#& ----------------------------------------

#* try:
#*     age = 15

#*     if age < 18:
#*         raise ValueError("Age must be 18 or above")

#* except ValueError as e:
#*     print(e)


#^ Output:

#^ Age must be 18 or above


#& ----------------------------------------
#& Exception Object
#& ----------------------------------------

#~ `as e` ka use karke hum
#~ error ki information store kar sakte hain.

#* try:
#*     number = 10 / 0

#* except ZeroDivisionError as e:
#*     print(e)


#^ Output:

#^ division by zero


#~ Yahan `e` exception object ko
#~ represent karta hai.


#& ----------------------------------------
#& Important Syntax
#& ----------------------------------------

#* try:
#*     risky_code

#* except ExceptionType:
#*     error_handling_code

#* else:
#*     successful_code

#* finally:
#*     cleanup_code


#& ----------------------------------------
#& Important Points
#& ----------------------------------------

#~ ✔ try → Risky code

#~ ✔ except → Error handle karta hai

#~ ✔ else → Error na aaye tab execute hota hai

#~ ✔ finally → Hamesha execute hota hai

#~ ✔ raise → Manually exception generate karta hai

#~ ✔ `as e` → Exception ki information
#~    access karne ke liye.


#& ----------------------------------------
#& Real-World Uses
#& ----------------------------------------

#~ Error Handling ka use:

#~ • File Handling
#~ • Database Operations
#~ • User Input
#~ • API Requests
#~ • Payment Systems
#~ • Web Applications
#~ • Data Processing
#~ • Machine Learning Applications


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Error Handling?

#~ Error Handling is a mechanism in Python
#~ used to handle runtime errors and prevent
#~ the program from terminating unexpectedly.

#~ Python me Error Handling mainly
#~ try, except, else, finally aur raise
#~ keywords ke through ki jati hai.


#? Assignment: 
 
#& 🔴 Question 1 – Division by Zero

#* Create two variables:

#^ a = 10
#^ b = 0

#* Divide `a` by `b`.

#* Use `try-except` to handle
#* ZeroDivisionError.

#^ Expected Output:

#^ Cannot divide by zero

# a = 10
# b = 0

# try:
#     result = a/b

# except ZeroDivisionError:
#     print("Cannot divide by zero")



#& 🔴 Question 2 – User Input

#* Ask the user to enter a number.

#* Convert the input into an integer.

#* Use `try-except` to handle
#* ValueError.

#^ Expected Output:

#^ Enter a valid number

# try:
#     user_input = int(input("Enter a number :")) 
#     print("Valid Number")

# except ValueError:
#     print("Invalid Number")



#& 🔴 Question 3 – Division with User Input

#* Ask the user to enter two numbers.

#* Divide the first number by the second number.

#* Handle:

#^ ValueError
#^ ZeroDivisionError

#^ Expected:

#^ Invalid input
#^ OR
#^ Cannot divide by zero

# try:
#     a = int(input("Enter a number : "))
#     b = int(input("Enter a number : "))

#     result = a/b

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")



#& 🔴 Question 4 – List Index

#* Create a list:

#^ [10, 20, 30, 40, 50]

#* Ask the user to enter an index.

#* Print the element at that index.

#* Handle `IndexError`.

#^ Expected Output:

#^ Invalid index

# lst = [10, 20, 30, 40, 50]

# try:
#     user_index = int(input("Enter a index : "))
#     print(lst[user_index])

# except IndexError:
#     print("Invalid index")



#& 🔴 Question 5 – Dictionary Key

#* Create a dictionary:

#^ {"name": "Pravin", "age": 23}

#* Ask the user to enter a key.

#* Print its value.

#* Handle `KeyError`.

#^ Expected Output:

#^ Key not found

# dic = {"name": "Pravin", "age": 23}

# try:
#     user_key = input("Enter the key : ")
#     print(dic[user_key])

# except KeyError:
#     print("Key not found")



#& 🔴 Question 6 – Multiple Exceptions

#* Ask the user to enter two numbers.

#* Divide the first number by the second.

#* Handle:

#^ ValueError
#^ ZeroDivisionError

#* Use separate `except` blocks.

# try:
#     a = int(input("Enter a number : "))
#     b = int(input("Enter a number : "))

#     print(a/b)

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError as e:
#     print(e)



#& 🔴 Question 7 – try-except-else

#* Ask the user to enter a number.

#* Convert it into an integer.

#* If conversion is successful,
#* print `"Valid Number"`.

#* If conversion fails,
#* print `"Invalid Number"`.

#* Use `try`, `except`, and `else`.

# try:
#     n = input("Enter the number : ")
#     n = int(n)

# except ValueError:
#     print("Invalid Number")

# else:
#     print("Valid Number")



#& 🔴 Question 8 – finally

#* Create a program that divides:

#^ 100 / 5

#* Use:

#^ try
#^ except
#^ finally

#* Print `"Program Completed"`
#* inside `finally`.

#^ Expected Output:

#^ 20.0
#^ Program Completed

# try:
#     a = int(input("Enter the number : "))
#     b = int(input("Enter the number : "))

#     print(a/b)

# except ValueError:
#     print("Invalid Number")

# finally:
#     print("Program Completed")



#& 🔴 Question 9 – Exception Object

#* Create a program:

#^ 10 / 0

#* Handle `ZeroDivisionError`.

#* Use `as e` to store the exception.

#* Print the error message.

#^ Expected Output:

#^ division by zero

# try:
#     a = int(input("Enter the number : "))
#     b = int(input("Enter the number : "))

#     print(a/b)

# except ZeroDivisionError as e:
#     print(e)



#& 🔴 Question 10 – File Error

#* Try to open a file named:

#^ "students.txt"

#* Read its content.

#* Handle `FileNotFoundError`.

#^ Expected Output:

#^ File not found

# try:
#     with open("students.txt", "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found")



#& 🔴 Question 11 – raise ValueError

#* Create a variable:

#^ age = 15

#* If age is less than 18:

#^ Raise `ValueError`

#^ Message:

#^ "Age must be 18 or above"

# try:
#     age = int(input("Enter the age : "))

#     if age < 18:
#         raise ValueError("Age must be 18 or above")

# except ZeroDivisionError as e:
#     print(e)

# else:
#     print("You are adult")



#& 🔴 Question 12 – Handle raise

#* Create:

#^ age = 15

#* Use `try-except`.

#* If age is less than 18,
#* raise `ValueError`.

#* Handle the error and print
#* the error message.

#^ Expected Output:

#^ Age must be 18 or above

# age = int(input("Enter the age : "))

# try:
#     if age < 18:
#         raise ValueError("Age must be 18 or above")

# except ZeroDivisionError as e:
#     print(e)

# else:
#     print("You are adult")



#& 🔴 Question 13 – Positive Number

#* Ask the user to enter a number.

#* If the number is negative:

#^ Raise `ValueError`

#^ Message:

#^ "Number must be positive"

#* Handle the error using `except`.

# n = int(input("Enter the number : "))

# try: 
#     if n < 0:
#         raise ValueError("number is negative")

# except ZeroDivisionError as e:
#     print(e)

# else:
#     print("number is positive")



#& 🔴 Question 14 – Complete Error Handling

#* Ask the user to enter two numbers.

#* Divide the first number by the second.

#* Handle:

#^ ValueError
#^ ZeroDivisionError

#* Use:

#^ try
#^ except
#^ else
#^ finally

#^ Expected:

#^ Correct result → else
#^ Error → except
#^ Always → finally

# try:
#     a = int(input("Enter the number : "))
#     b = int(input("Enter the number : "))

#     print(a/b)

# except ValueError:
#     print("Invalid Number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Valid Number")

# finally:
#     print("Program Completed")



#& 🔴 Question 15 – Mini Calculator

#* Ask the user to enter:

#^ First number
#^ Second number
#^ Operator

#* Support:

#^ +
#^ -
#^ *
#^ /

#* Handle:

#^ ValueError
#^ ZeroDivisionError
#^ Invalid operator

#* Use:

#^ try
#^ except
#^ else
#^ finally

# try:
#     a = int(input("Enter the number : "))
#     b = int(input("Enter the number : "))

#     print(f"Addition : {a + b}")
#     print(f"Substract : {a - b}")
#     print(f"Multiplication : {a * b}")
#     print(f"Divide : {a / b}")

# except ValueError:
#     print("Invalid Number")

# except ZeroDivisionError:
#     print("cannot divide by zero")

# else:
#     print("Valid Number")

# finally:
#     print("Program Completed")