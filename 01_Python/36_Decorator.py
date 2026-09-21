
#! ==========================================
#! DECORATORS IN PYTHON
#! ==========================================


#? What is a Decorator?

#~ Decorator ek special function hai
#~ jo kisi existing function ke behavior
#~ ko modify ya extend karta hai.

#~ Original function ke code ko change
#~ kiye bina usme extra functionality
#~ add kar sakte hain.

#~ Simple Line:

#~ Decorator → Existing function mein
#~ extra functionality add karta hai
#~ without changing its original code.



#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho tumhare paas ek normal function hai:

#^ Login()

#~ Ab tum Login function ke saath
#~ extra kaam karna chahte ho:

#~ • Login se pehle → Check user
#~ • Login ke baad → Log activity

#~ Original Login() function ko change
#~ kiye bina Decorator se ye extra
#~ functionality add kar sakte ho.



#& ----------------------------------------
#& Why do we use Decorators?
#& ----------------------------------------

#~ Decorators ka use:

#^ 1. Existing function mein
#~ extra functionality add karne ke liye.

#^ 2. Original function ka code
#~ change nahi karna padta.

#^ 3. Code Reusability ke liye.

#^ 4. Repeated code ko avoid karne ke liye.

#^ 5. Logging, authentication,
#~ timing, validation etc. ke liye.



#& ----------------------------------------
#& Basic Concept
#& ----------------------------------------

#~ Decorator ko samajhne ke liye
#~ pehle ye samjho:

#^ Function bhi Python mein
#^ ek object hota hai.

#~ Isliye hum function ko:

#~ • Variable mein store kar sakte hain.
#~ • Dusre function mein pass kar sakte hain.
#~ • Function se return kar sakte hain.



#& ----------------------------------------
#& Function as an Object
#& ----------------------------------------

#* def greet():
#*     print("Hello Pravin")


#* message = greet

#* message()


#^ Output:

#^ Hello Pravin


#~ Yahan:

#^ greet → Function

#^ message → Same function ka reference


#~ Isliye:

#* message()

#~ bhi:

#* greet()

#~ ki tarah work karega.



#& ----------------------------------------
#& Passing Function as Argument
#& ----------------------------------------

#~ Ek function ko dusre function mein
#~ argument ke roop mein pass kar sakte hain.


#* def greet():
#*     print("Hello")


#* def execute(function):
#*     function()


#* execute(greet)


#^ Output:

#^ Hello


#~ Yahan `greet` function ko
#~ `execute()` ke andar pass kiya gaya.



#& ----------------------------------------
#& Nested Function
#& ----------------------------------------

#~ Function ke andar dusra function
#~ define karna Nested Function kehlata hai.


#* def outer():

#*     def inner():
#*         print("Hello")

#*     inner()


#* outer()


#^ Output:

#^ Hello


#~ Decorators mein Nested Functions
#~ bahut important hote hain.



#& ----------------------------------------
#& Higher-Order Function
#& ----------------------------------------

#~ Aisa function jo:

#^ • Kisi function ko argument ke roop mein le.

#^ OR

#^ • Kisi function ko return kare.

#~ Higher-Order Function kehlata hai.


#~ Decorators Higher-Order Functions
#~ ke concept par based hote hain.



#& ----------------------------------------
#& Creating a Simple Decorator
#& ----------------------------------------


#* def decorator(function):

#*     def wrapper():
#*         print("Before function")

#*         function()

#*         print("After function")

#*     return wrapper


#* @decorator
#* def greet():
#*     print("Hello")


#* greet()


#^ Output:

#^ Before function
#^ Hello
#^ After function


#~ Yahan:

#^ decorator → Decorator function

#^ function → Original function

#^ wrapper → Extra functionality

#^ @decorator → Decorator apply karta hai



#& ----------------------------------------
#& How Decorator Works?
#& ----------------------------------------


#* @decorator
#* def greet():
#*     print("Hello")


#~ Python internally approximately:

#* greet = decorator(greet)


#~ Iska matlab:

#^ Original greet()
#*       ↓
#^ decorator()
#*       ↓
#^ wrapper()
#*       ↓
#^ Modified greet()



#& ----------------------------------------
#& @ Syntax
#& ----------------------------------------

#~ Decorator apply karne ke liye
#~ `@` symbol use hota hai.


#^ Syntax:

#* @decorator
#* def function():
#*     pass


#~ Ye approximately equivalent hai:

#* def function():
#*     pass

#* function = decorator(function)



#& ----------------------------------------
#& Decorator Without @
#& ----------------------------------------


#* def decorator(function):

#*     def wrapper():
#*         print("Before")

#*         function()

#*         print("After")

#*     return wrapper


#* def greet():
#*     print("Hello")


#* greet = decorator(greet)

#* greet()


#^ Output:

#^ Before
#^ Hello
#^ After


#~ `@decorator` sirf ek easy syntax hai.



#& ----------------------------------------
#& Decorator with Function Arguments
#& ----------------------------------------

#~ Agar original function arguments
#~ leta hai to wrapper ko bhi
#~ arguments handle karne padte hain.


#* def decorator(function):

#*     def wrapper(name):
#*         print("Before function")

#*         function(name)

#*         print("After function")

#*     return wrapper


#* @decorator
#* def greet(name):
#*     print(f"Hello {name}")


#* greet("Pravin")


#^ Output:

#^ Before function
#^ Hello Pravin
#^ After function



#& ----------------------------------------
#& Problem with Different Arguments
#& ----------------------------------------

#~ Agar different functions ke
#~ different number of arguments hain,

#~ to har wrapper mein manually
#~ arguments define karna difficult ho sakta hai.


#~ Is problem ko solve karne ke liye:

#^ *args

#^ **kwargs

#~ use kiye jaate hain.



#& ----------------------------------------
#& Decorator with *args
#& ----------------------------------------


#* def decorator(function):

#*     def wrapper(*args):
#*         print("Before function")

#*         function(*args)

#*         print("After function")

#*     return wrapper


#* @decorator
#* def add(a, b):
#*     print(a + b)


#* add(10, 20)


#^ Output:

#^ Before function
#^ 30
#^ After function


#& ----------------------------------------
#& Decorator with **kwargs
#& ----------------------------------------


#~ `**kwargs` keyword arguments
#~ handle karta hai.


#* def decorator(function):

#*     def wrapper(**kwargs):
#*         print("Before function")

#*         function(**kwargs)

#*         print("After function")

#*     return wrapper


#* @decorator
#* def student(name, course):
#*     print(name, course)


#* student(name="Pravin", course="AI/ML")



#& ----------------------------------------
#& Decorator with *args and **kwargs
#& ----------------------------------------


#~ Most flexible decorator mein
#~ dono use kar sakte hain.


#* def decorator(function):

#*     def wrapper(*args, **kwargs):

#*         print("Before function")

#*         function(*args, **kwargs)

#*         print("After function")

#*     return wrapper


#~ Ab wrapper different types ke
#~ arguments handle kar sakta hai.



#& ----------------------------------------
#& Practical Example – Login
#& ----------------------------------------


#* def check_login(function):

#*     def wrapper():
#*         print("Checking Login...")

#*         function()

#*     return wrapper


#* @check_login
#* def dashboard():
#*     print("Welcome to Dashboard")


#* dashboard()


#^ Output:

#^ Checking Login...
#^ Welcome to Dashboard


#~ Yahan `check_login()` decorator
#~ dashboard() ke around extra
#~ functionality add kar raha hai.



#& ----------------------------------------
#& Practical Uses
#& ----------------------------------------

#~ Real projects mein decorators ka
#~ use bahut common hai.


#^ Logging

#~ Function kab call hua
#~ ye record karna.


#^ Authentication

#~ User logged-in hai ya nahi
#~ check karna.


#^ Authorization

#~ User ko permission hai ya nahi
#~ check karna.


#^ Timing

#~ Function ko execute hone mein
#~ kitna time laga.


#^ Validation

#~ Input valid hai ya nahi
#~ check karna.


#^ Caching

#~ Previous result ko store karke
#~ performance improve karna.



#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Code Reusability

#~ ✔ Code Duplication kam hota hai.

#~ ✔ Original function ka code
#~ change nahi karna padta.

#~ ✔ Extra functionality easily
#~ add kar sakte hain.

#~ ✔ Large projects mein useful.



#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Beginners ke liye initially
#~ confusing ho sakta hai.

#~ ❌ Multiple decorators hone par
#~ code difficult to understand ho sakta hai.

#~ ❌ Debugging kabhi-kabhi difficult
#~ ho sakti hai.



#& ----------------------------------------
#& Important Keywords
#& ----------------------------------------

#^ Decorator

#~ Existing function ke behavior ko
#~ modify/extend karta hai.


#^ Wrapper

#~ Original function ko wrap karta hai
#~ aur extra functionality provide karta hai.


#^ @

#~ Decorator apply karne ka
#~ shortcut syntax.


#^ *args

#~ Multiple positional arguments
#~ handle karta hai.


#^ **kwargs

#~ Multiple keyword arguments
#~ handle karta hai.



#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#^ Function
#*    ↓
#^ Decorator
#*    ↓
#^ Wrapper
#*    ↓
#^ Extra Functionality
#*    ↓
#^ Original Function


#~ Yaad rakho:

#~ Decorator original function ko
#~ directly change nahi karta.

#~ Wo uske around extra functionality
#~ add karta hai.



#& ==========================================
#& INTERVIEW DEFINITIONS
#& ==========================================


#? What is a Decorator?

#~ A Decorator is a function that modifies
#~ or extends the behavior of another
#~ function without changing its
#~ original code.


#? What is `@decorator`?

#~ `@decorator` is the special syntax
#~ used to apply a decorator to a function.


#? What is a Wrapper Function?

#~ A Wrapper Function is an inner function
#~ that wraps the original function and
#~ adds extra functionality around it.


#? Why use *args and **kwargs in Decorators?

#~ `*args` and `**kwargs` allow a wrapper
#~ function to handle different numbers
#~ and types of arguments.



#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#^ Original Function
#*       ↓
#^ Decorator
#*       ↓
#^ Wrapper Function
#*       ↓
#^ Extra Functionality
#*       ↓
#^ Original Function Executes


#? Assignment:


#& 🔴 Question 1 – Hello Decorator

#* Create a decorator named `decorator`.

#* Print:

#^ "Before Function"

#* Call the original function.

#* Print:

#^ "After Function"

#* Create a function named `greet()`.

#^ Print "Hello"


#^ Expected Output:

#^ Before Function
#^ Hello
#^ After Function

# def decorator(function):

#     def wrapper():
#         print("Before Function")

#         function()

#         print("After Function")

#     return wrapper

# def greet(): 
#     print("Hello")

# greet = decorator(greet)

# greet()



#& 🔴 Question 2 – Welcome Message

#* Create a decorator named `welcome`.

#* Print:

#^ "Welcome to Python"

#* Call the original function.

#* Create a function named `study()`.

#^ Print "I am studying Python"


#^ Expected Output:

#^ Welcome to Python
#^ I am studying Python

# def welcome(function):

#     def wrapper():
#         print("Welcome to Python")

#         function()

#     return wrapper

# def study():
#     print("I am studying Python")

# study = welcome(study)

# study()



#& 🔴 Question 3 – @ Syntax

#* Create a decorator named `my_decorator`.

#* Use `@my_decorator`.

#* Create a function named `message()`.

#^ Print "Hello Pravin"

#* Decorator should print:

#^ "Function Started"

#* before calling the function.

# def my_decorator(function):

#     def wrapper():
#         print("Hello Pravin")

#         function()

#     return wrapper


# @my_decorator
# def message():
#     print("Function Started")

# message()



#& 🔴 Question 4 – Name Argument

#* Create a decorator named `decorator`.

#* Create a function named `greet(name)`.

#* Print:

#^ "Hello <name>"

#* Use the decorator.

#* Call:

#^ greet("Pravin")


#^ Expected Output:

#^ Function Started
#^ Hello Pravin

# def decorator(function):

#     def wrapper(name):
#         print("Function Started")

#         function(name)

#     return wrapper

# def greet(name):
#     print(f"Hello {name}")

# greet = decorator(greet)

# greet("Pravin")



#& 🔴 Question 5 – Add Two Numbers

#* Create a decorator.

#* Create a function named `add(a, b)`.

#* Return the sum of two numbers.

#* Use the decorator.

#* Call:

#^ add(10, 20)

#* Print the result.

# def decorator(function):

#     def wrapper(a, b):
#         print("Function Started")
#         return function(a, b)

#     return wrapper

# def add(a, b):
#     return a + b

# add = decorator(add)
# result = add(10, 20)
# print(result)



#& 🔴 Question 6 – Multiple Arguments

#* Create a decorator using `*args`.

#* Create a function named `add(a, b, c)`.

#* Return the sum of all three numbers.

#* Use the decorator.

#* Call:

#^ add(10, 20, 30)


#^ Expected Output:

#^ 60

# def decorator(function):

#     def wrapper(*args):
#         print("Function Started")
#         return function(*args)

#     return wrapper

# def add(a, b, c):
#     print(a + b + c)

# add = decorator(add)

# add(10, 20, 30)



#& 🔴 Question 7 – Student Information

#* Create a decorator using `**kwargs`.

#* Create a function named `student()`.

#* Accept:

#^ name
#^ course

#* Print both values.

#* Use the decorator.

#* Call:

#^ student(name="Pravin", course="AI/ML")

# def decorator(function):

#     def wrapper(**kwargs):
#         print("Function Started")
#         return function(**kwargs)

#     return wrapper

# def student(**kwargs):
#     print(kwargs)

# student = decorator(student)

# student(name = "Pravin", course = "AI/ML")



#& 🔴 Question 8 – Flexible Decorator

#* Create a decorator using:

#^ `*args`

#^ `**kwargs`

#* Create a function named `details()`.

#* Accept any number of arguments.

#* Print the arguments.

#* Use the decorator.

# def decorator(function):

#     def wrapper(*args, **kwargs):
#         print("Function Started")
#         return function(*args, **kwargs)

#     return wrapper

# def details(*args, **kwargs):
#     print("Arguments : ", args, kwargs)

# details = decorator(details)

# details(1, 2, 3, name = "Pravin", course = "AI/ML")



#& 🔴 Question 9 – Execution Message

#* Create a decorator named `check`.

#* Before the function:

#^ Print "Function Started"

#* After the function:

#^ Print "Function Completed"

#* Create a function named `calculate()`.

#^ Print "Calculating..."


#^ Expected Output:

#^ Function Started
#^ Calculating...
#^ Function Completed

# def check(function):

#     def wrapper():
#         print("Function Started")

#         function()

#         print("Function Completed")

#     return wrapper

# def calculating():
#     print("Calculating...")

# calculating = check(calculating)

# calculating()



#& 🔴 Question 10 – Practical Login Decorator

#* Create a decorator named `login_required`.

#* Before calling the function, print:

#^ "Checking Login..."


#* Create a function named `dashboard()`.

#^ Print "Welcome to Dashboard"


#* Apply the decorator using `@`.

#* Call `dashboard()`.


#^ Expected Output:

#^ Checking Login...
#^ Welcome to Dashboard

# def login_required(function):

#     def wrapper():
#         print("Checking Login...")

#     function()

#     return wrapper

# @login_required
# def dashboard():
#     print("Welcome to Dashboard")

# dashboard()



#& 🔴 Question 11 – Decorator with Return Value

#* Create a decorator named `decorator`.

#* Before calling the function, print:

#^ "Function Started"

#* Call the original function.

#* Return the result from the original function.

#* Create a function named `multiply(a, b)`.

#^ Return the multiplication of two numbers.

#* Apply the decorator using `@`.

#* Call:

#^ multiply(5, 4)

#* Print the result.

#^ Expected Output:

#^ Function Started
#^ 20

# def decorator(function):

#     def wrapper(a, b):
#         print("Function Started")
#         return function(a, b)

#     return wrapper

# @decorator
# def multiplication(a, b):
#     return a * b


# result = multiplication(5, 4)
# print(result)




#& 🔴 Question 12 – Decorator with *args

#* Create a decorator named `decorator`.

#* Use `*args` in the wrapper.

#* Print:

#^ "Arguments Received"

#* Call the original function using `*args`.

#* Create a function named `add()`.

#* Accept any number of numbers using `*args`.

#* Return their total.

#* Apply the decorator using `@`.

#* Call:

#^ add(10, 20, 30, 40)

#* Print the result.

#^ Expected Output:

#^ Arguments Received
#^ 100

# def decorator(function):

#     def wrapper(*args):
#         print("Arguments Received")
#         return function(*args)

#     return wrapper

# @decorator
# def add(a, b, c, d):
#     return(f"Total : {a+b+c+d}")

# result = add(10, 20, 30, 40)
# print(result)



#& 🔴 Question 13 – Decorator with **kwargs

#* Create a decorator named `decorator`.

#* Use `**kwargs` in the wrapper.

#* Print:

#^ "Student Details"

#* Call the original function using `**kwargs`.

#* Create a function named `student()`.

#* Accept:

#^ name
#^ course
#^ marks

#* Print the values.

#* Apply the decorator using `@`.

#* Call:

#^ student(name="Pravin", course="AI/ML", marks=85)

#^ Expected Output:

#^ Student Details
#^ Pravin
#^ AI/ML
#^ 85

# def decorator(function):

#     def wrapper(**kwargs):
#         print("Student Details")
#         return function(**kwargs)

#     return wrapper

# @decorator
# def student(**kwargs):
#     return(kwargs)

# result = student(name="Pravin", course="AI/ML", marks=85)
# print(result)



#& 🔴 Question 14 – Before and After Decorator

#* Create a decorator named `check`.

#* Before calling the function, print:

#^ "Starting Calculation"

#* Call the original function.

#* After the function completes, print:

#^ "Calculation Completed"

#* Create a function named `square(n)`.

#^ Return the square of `n`.

#* Apply the decorator using `@`.

#* Call:

#^ square(5)

#* Print the returned result.

#^ Expected Output:

#^ Starting Calculation
#^ Calculation Completed
#^ 25

# def check(function):

#     def wrapper(n):
#         print("Starting Calculation")

#         result = function(n)

#         print("Calculation Completed")

#         return result

#     return wrapper


# @check
# def square(n):
#     return n * n


# result = square(5)
# print(result)
    



#& 🔴 Question 15 – Login Check Decorator

#* Create a decorator named `login_required`.

#* Create a variable:

#^ is_logged_in = True

#* Inside the wrapper:

#~ If `is_logged_in` is `True`:

#^ Print "Access Granted"

#^ Call the original function.

#~ Otherwise:

#^ Print "Access Denied"

#* Create a function named `dashboard()`.

#^ Print "Welcome to Dashboard"

#* Apply the decorator using `@`.

#* Call `dashboard()`.

#^ Expected Output:

#^ Access Granted
#^ Welcome to Dashboard

# def login_required(function):

#     is_logged_in = True

#     def wrapper():
#         if is_logged_in is True:
#             print("Access Granted")
#             return function()
#         else:
#             print("Access Denied")

#     return wrapper

# @login_required
# def dashboard():
#     return("Welcome to Dashboard")

# result = dashboard()
# print(result)