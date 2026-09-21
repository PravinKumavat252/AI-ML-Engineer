
#! ==========================================
#! Generators in Python
#! ==========================================

#? What is a Generator?

#~ Generator Python me ek special type ka
#~ function hota hai jo values ko
#~ ek-ek karke generate karta hai.

#~ Generator ek saath saari values memory
#~ me store nahi karta.

#~ Ye jab next value ki zarurat hoti hai,
#~ tab next value generate karta hai.

#~ Generator function me `yield` keyword
#~ use hota hai.

#~ Simple Line:

#~ Generator → Values one-by-one generate karta hai.



#& ----------------------------------------
#& Why Generators are Used?
#& ----------------------------------------

#~ Generators ka main use:

#~ ✔ Memory save karne ke liye.

#~ ✔ Large amount of data handle karne ke liye.

#~ ✔ Values ko one-by-one process karne ke liye.

#~ ✔ Performance improve karne ke liye.

#~ ✔ Infinite sequence generate karne ke liye.



#& ----------------------------------------
#& Generator vs Normal Function
#& ----------------------------------------

#^ Normal Function

#~ `return` keyword use karta hai.

#~ Usually ek result return karta hai.

#~ Function complete hone ke baad
#~ uska execution finish ho jata hai.


#^ Generator Function

#~ `yield` keyword use karta hai.

#~ Values one-by-one return karta hai.

#~ Apni current state ko remember karta hai.

#~ Next value ke liye execution wahi se
#~ continue hota hai.



#& ----------------------------------------
#& Generator Syntax
#& ----------------------------------------

#* def generator_function():
#*     yield value

#~ Generator function banane ke liye
#~ `yield` keyword use karna zaroori hai.



#& ----------------------------------------
#& Simple Generator Example
#& ----------------------------------------

#* def numbers():
#*     yield 1
#*     yield 2
#*     yield 3

#* result = numbers()

#* print(next(result))
#* print(next(result))
#* print(next(result))

#^ Output:

#^ 1
#^ 2
#^ 3

#~ `numbers()` call karne par values
#~ immediately generate nahi hoti.

#~ Ye ek Generator Object return karta hai.

#~ `next()` use karne par next value
#~ generate hoti hai.



#& ----------------------------------------
#& yield Keyword
#& ----------------------------------------

#~ `yield` Generator ka most important
#~ keyword hai.

#~ `yield` value return karta hai aur
#~ function ki current state ko save karta hai.

#~ Jab next value maangi jati hai,
#~ function wahi se continue hota hai.


#* def demo():
#*     print("First")
#*     yield 10
#*     print("Second")
#*     yield 20

#* g = demo()

#* print(next(g))
#* print(next(g))

#^ Output:

#^ First
#^ 10
#^ Second
#^ 20

#~ Pehle `next()` par function
#~ `yield 10` par pause hua.

#~ Dusre `next()` par function
#~ wahi se continue hua.



#& ----------------------------------------
#& Generator Object
#& ----------------------------------------

#~ Generator function ko call karne par
#~ normal value nahi milti.

#~ Ek Generator Object milta hai.


#* def numbers():
#*     yield 1
#*     yield 2
#*     yield 3

#* g = numbers()

#* print(g)

#~ `g` ek Generator Object hai.



#& ----------------------------------------
#& next() Function
#& ----------------------------------------

#~ `next()` Generator se next value
#~ retrieve karne ke liye use hota hai.

#* def numbers():
#*     yield 10
#*     yield 20
#*     yield 30

#* g = numbers()

#* print(next(g))
#* print(next(g))
#* print(next(g))

#^ Output:

#^ 10
#^ 20
#^ 30

#~ Har `next()` call par Generator
#~ next value deta hai.



#& ----------------------------------------
#& StopIteration
#& ----------------------------------------

#~ Jab Generator ki saari values
#~ complete ho jati hain,

#~ aur hum `next()` dobara call karte hain,

#~ to Python `StopIteration` exception
#~ raise karta hai.


#* def numbers():
#*     yield 1
#*     yield 2

#* g = numbers()

#* print(next(g))
#* print(next(g))
#* print(next(g))

#^ Output:

#^ 1
#^ 2

#^ StopIteration

#~ Isliye normally Generator ko
#~ `for` loop ke saath use karna easy hota hai.



#& ----------------------------------------
#& Generator with for Loop
#& ----------------------------------------

#* def numbers():
#*     yield 1
#*     yield 2
#*     yield 3

#* for i in numbers():
#*     print(i)

#^ Output:

#^ 1
#^ 2
#^ 3

#~ `for` loop automatically Generator se
#~ values ek-ek karke leta hai.



#& ----------------------------------------
#& Generator for Large Data
#& ----------------------------------------

#~ Agar hume bahut saari values
#~ process karni ho, to Generator
#~ memory efficient hota hai.

#* def numbers():
#*     for i in range(1, 1000001):
#*         yield i

#* for i in numbers():
#*     print(i)

#~ Yahan 10 lakh values ko ek saath
#~ memory me store nahi kiya jata.

#~ Values one-by-one generate hoti hain.



#& ----------------------------------------
#& Generator vs List
#& ----------------------------------------

#^ List

#~ Saari values memory me store hoti hain.

#* numbers = [1, 2, 3, 4, 5]

#^ Generator

#~ Values one-by-one generate hoti hain.

#* def numbers():
#*     for i in range(1, 6):
#*         yield i

#~ Large data ke liye Generator
#~ zyada memory efficient hota hai.



#& ----------------------------------------
#& Generator Expression
#& ----------------------------------------

#~ Generator Expression ek short way hai
#~ Generator create karne ka.

#~ Isme square brackets `[]` ki jagah
#~ round brackets `()` use hote hain.

#* g = (i * i for i in range(1, 6))

#* for i in g:
#*     print(i)

#^ Output:

#^ 1
#^ 4
#^ 9
#^ 16
#^ 25


#& ----------------------------------------
#& List Comprehension vs Generator Expression
#& ----------------------------------------

#^ List Comprehension

#* numbers = [i * i for i in range(1, 6)]

#~ Saari values ek list me
#~ memory me store hoti hain.

#^ Generator Expression

#* numbers = (i * i for i in range(1, 6))

#~ Values one-by-one generate hoti hain.

#~ Simple Difference:

#~ `[]` → List Comprehension

#~ `()` → Generator Expression



#& ----------------------------------------
#& Generator with Parameters
#& ----------------------------------------

#~ Generator function normal function ki
#~ tarah parameters bhi le sakta hai.

#* def numbers(start, end):
#*     for i in range(start, end + 1):
#*         yield i

#* for i in numbers(1, 5):
#*     print(i)

#^ Output:

#^ 1
#^ 2
#^ 3
#^ 4
#^ 5



#& ----------------------------------------
#& Multiple yield
#& ----------------------------------------

#~ Ek Generator function me
#~ multiple `yield` statements ho sakte hain.

#* def student():
#*     yield "Pravin"
#*     yield 23
#*     yield "AI/ML"

#* for i in student():
#*     print(i)

#^ Output:

#^ Pravin
#^ 23
#^ AI/ML



#& ----------------------------------------
#& Important Features
#& ----------------------------------------

#~ ✔ Generator function `yield` use karta hai.

#~ ✔ Generator values one-by-one generate karta hai.

#~ ✔ Generator apni state remember karta hai.

#~ ✔ `next()` next value retrieve karta hai.

#~ ✔ Generator memory efficient hota hai.

#~ ✔ Large datasets ke liye useful hai.

#~ ✔ Infinite sequences ke liye useful hai.

#~ ✔ Generator expression bhi create kar sakte hain.



#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ Less Memory Usage

#~ ✔ Better for Large Data

#~ ✔ Efficient Data Processing

#~ ✔ One-by-One Processing

#~ ✔ Infinite Data Streams Handle kar sakte hain.



#& ----------------------------------------
#& Disadvantages
#& ----------------------------------------

#~ ❌ Values ko directly index nahi kar sakte.

#~ ❌ Generator ki values generally
#~ one-time consume hoti hain.

#~ ❌ Previous values ko directly
#~ access nahi kar sakte.



#& ----------------------------------------
#& Real-World Uses
#& ----------------------------------------

#~ Generators ka use:

#~ • Large Dataset Processing

#~ • File Reading

#~ • Data Processing

#~ • Machine Learning Data Pipelines

#~ • API Data Streaming

#~ • Log Processing

#~ • Large File Processing

#~ • Infinite Sequences



#& ----------------------------------------
#& Important Difference
#& ----------------------------------------

#^ return

#~ Function ko completely stop karta hai.

#~ Value return karke function
#~ execution finish ho jata hai.

#^ yield

#~ Function ko temporarily pause karta hai.

#~ Current state save hoti hai.

#~ Next `next()` call par execution
#~ wahi se continue hota hai.



#& ----------------------------------------
#& Easy Way to Remember
#& ----------------------------------------

#~ Generator
#~ → Values one-by-one

#~ yield
#~ → Value do + pause ho jao

#~ next()
#~ → Next value lao

#~ StopIteration
#~ → Values complete

#~ Generator Expression
#~ → `(expression for item in iterable)`



#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is a Generator in Python?

#~ A Generator is a special type of function
#~ that generates values one at a time using
#~ the `yield` keyword.

#~ It does not store all values in memory
#~ at once, making it memory efficient
#~ for large datasets.


#? Assignment:


#& 🔴 Question 1 – Generate Numbers

#* Create a Generator function named `numbers()`.

#* Use `yield` to generate:

#^ 1
#^ 2
#^ 3

#* Use a `for` loop to print the values.

#^ Expected Output:

#^ 1
#^ 2
#^ 3

# def numbers():

#     for i in range(1, 4):
#         yield i

# for i in numbers():
#     print(i)



#& 🔴 Question 2 – Generate Even Numbers

#* Create a Generator function named `even_numbers()`.

#* Generate even numbers from `2` to `10`.

#* Use a `for` loop to print the values.

#^ Expected Output:

#^ 2
#^ 4
#^ 6
#^ 8
#^ 10

# def even_numbers():

#     for i in range(1, 11):
#         if i % 2 == 0:
#             yield i

# for i in even_numbers():
#     print(i)



#& 🔴 Question 3 – Generate Squares

#* Create a Generator function named `squares()`.

#* Generate the square of numbers
#* from `1` to `5`.

#* Use a `for` loop.

#^ Expected Output:

#^ 1
#^ 4
#^ 9
#^ 16
#^ 25

# def  squares():

#     for i in range(1, 6):
#         yield i * i

# for i in squares():
#     print(i)



#& 🔴 Question 4 – Use next()

#* Create a Generator function named `numbers()`.

#* Generate:

#^ 10
#^ 20
#^ 30

#* Create a Generator object.

#* Use `next()` three times.

#* Print each value. 

# def numbers():

#     yield 10
#     yield 20
#     yield 30

# n = numbers()

# print(next(n))
# print(next(n))
# print(next(n))



#& 🔴 Question 5 – Generator State

#* Create a Generator function named `count()`.

#* Generate numbers:

#^ 1
#^ 2
#^ 3
#^ 4
#^ 5

#* Create a Generator object.

#* Call `next()` two times.

#* Print the values.

#* Call `next()` two more times.

#* Print the values.

# def count():

#     for i in range(1, 6):
#         yield i

# c = count()

# next(c)
# next(c)
# print(next(c))
# next(c)
# next(c)



#& 🔴 Question 6 – Numbers Greater Than 5

#* Create a Generator function named `numbers()`.

#* Generate numbers from `1` to `10`.

#* Use a condition inside the Generator.

#* Generate only numbers greater than `5`.

#* Print the values using a `for` loop.

#^ Expected Output:

#^ 6
#^ 7
#^ 8
#^ 9
#^ 10

# def numbers():

#     for i in range(1, 11):
#         if i > 5:
#             yield i

# for i in numbers():
#     print(i)



#& 🔴 Question 7 – Multiplication Table

#* Create a Generator function named `table()`.

#* Generate the multiplication table
#* of `5`.

#* Generate values from:

#^ 5 × 1
#^ to
#^ 5 × 10

#* Print the generated results.

#^ Expected Output:

#^ 5
#^ 10
#^ 15
#^ ...
#^ 50

# def table(n):

#     for i in range(1, 11):
#         yield(f"{n} * {i} = {n * i}")

# for i in table(5):
#     print(i)



#& 🔴 Question 8 – Square Generator Expression

#* Create a Generator Expression.

#* Generate squares from `1` to `5`.

#* Use:

#^ `( )`

#* Print all values using a `for` loop.

#^ Expected Output:

#^ 1
#^ 4
#^ 9
#^ 16
#^ 25

# squares = (i*i for i in range(1, 6))

# for i in squares:
#     print(i)



#& 🔴 Question 9 – Even Number Generator Expression

#* Create a Generator Expression.

#* Generate even numbers from `1` to `10`.

#* Print the values using a `for` loop.

#^ Expected Output:

#^ 2
#^ 4
#^ 6
#^ 8
#^ 10

# even = (i for i in range(1, 11) if i % 2 == 0)

# for i in even:
#     print(i)



#& 🔴 Question 10 – Generator vs List

#* Create a List Comprehension that generates
#* squares from `1` to `5`.

#* Create a Generator Expression that generates
#* the same squares.

#* Print both.

#* Check their types using `type()`.

#~ Understand the difference between:

#^ List

# lst = [i*i for i in range(1, 6)]
# print(type(lst))


#^ Generator

# squares = (i*i for i in range(1, 6))

# for i in squares:
#     print(i)

# print(type(squares))