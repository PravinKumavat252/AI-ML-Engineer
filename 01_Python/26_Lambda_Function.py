
#! ==========================================
#! Lambda Function
#! ==========================================


#? What is Lambda Function?

#~ Lambda function Python ka ek
#~ small anonymous function hai.

#~ Anonymous ka matlab hai:

#~ Aisa function jiska koi normal
#~ function name nahi hota.

#~ Lambda function mainly small aur
#~ simple operations ke liye use hota hai.


#~ Simple Line:

#~ Lambda → Small Function Without Name


#& ----------------------------------------
#& Why do we use Lambda?
#& ----------------------------------------

#~ Lambda ka use mainly:

#^ • Small function ko short way mein likhne ke liye.

#^ • Ek simple operation ke liye.

#^ • `map()` ke saath use karne ke liye.

#^ • `filter()` ke saath use karne ke liye.

#^ • `sorted()` ke saath custom logic dene ke liye.


#& ----------------------------------------
#& Normal Function vs Lambda
#& ----------------------------------------

#? Normal Function

#* def square(x):
#*     return x * x


#* print(square(5))

#^ Output:

#^ 25


#? Lambda Function

#* square = lambda x: x * x

#* print(square(5))

#^ Output:

#^ 25


#~ Dono ka result same hai.

#~ Difference ye hai ki Lambda function
#~ ko short form mein likha gaya hai.


#& ----------------------------------------
#& Lambda Syntax
#& ----------------------------------------

#* lambda arguments : expression


#~ Easy way:

#^ lambda → Keyword

#^ arguments → Input

#^ `:` → Separator

#^ expression → Calculation / Result


#~ Simple Formula:

#^ Input → Operation → Result


#& ----------------------------------------
#& Example
#& ----------------------------------------

#* square = lambda x: x * x

#* print(square(5))

#^ Output:

#^ 25


#~ Yahan:

#^ `lambda` → Lambda keyword

#^ `x` → Argument

#^ `x * x` → Expression

#^ `square` → Lambda function ko
#^              store karne wala variable


#& ----------------------------------------
#& Lambda with One Argument
#& ----------------------------------------

#* double = lambda x: x * 2

#* print(double(10))

#^ Output:

#^ 20


#~ Yahan Lambda function ko
#~ ek argument `x` mila.


#& ----------------------------------------
#& Lambda with Two Arguments
#& ----------------------------------------

#* add = lambda x, y: x + y

#* print(add(10, 20))

#^ Output:

#^ 30


#~ Yahan:

#^ `x` → First argument

#^ `y` → Second argument

#^ `x + y` → Expression


#& ----------------------------------------
#& Lambda with Three Arguments
#& ----------------------------------------

#* total = lambda x, y, z: x + y + z

#* print(total(10, 20, 30))

#^ Output:

#^ 60


#~ Lambda function mein multiple
#~ arguments ho sakte hain.


#& ----------------------------------------
#& Lambda with Condition
#& ----------------------------------------

#~ Lambda mein `if-else` bhi use
#~ kar sakte hain.

#* check = lambda x: "Even" if x % 2 == 0 else "Odd"

#* print(check(10))

#^ Output:

#^ Even


#* print(check(7))

#^ Output:

#^ Odd


#~ Lambda mein `if-else` ka order:

#^ value_if_true if condition else value_if_false


#& ----------------------------------------
#& Lambda with String
#& ----------------------------------------

#* upper = lambda name: name.upper()

#* print(upper("pravin"))

#^ Output:

#^ PRAVIN


#& ----------------------------------------
#& Lambda with map()
#& ----------------------------------------

#~ Lambda ka sabse common use
#~ `map()` ke saath hota hai.

#* numbers = [1, 2, 3, 4, 5]

#* result = map(lambda x: x * 2, numbers)

#* print(list(result))

#^ Output:

#^ [2, 4, 6, 8, 10]


#~ Yahan:

#^ `lambda x: x * 2`
#~ → Har number ko 2 se multiply karega.

#^ `map()`
#~ → Lambda ko har element par apply karega.


#& ----------------------------------------
#& Lambda with filter()
#& ----------------------------------------

#~ Lambda ka use `filter()` ke saath
#~ bhi commonly hota hai.

#* numbers = [1, 2, 3, 4, 5, 6]

#* result = filter(lambda x: x % 2 == 0, numbers)

#* print(list(result))

#^ Output:

#^ [2, 4, 6]


#~ Yahan:

#^ `lambda x: x % 2 == 0`
#~ → Condition check karta hai.

#^ `filter()`
#~ → Sirf condition satisfy karne
#~ wale elements rakhta hai.


#& ----------------------------------------
#& Lambda with sorted()
#& ----------------------------------------

#~ Lambda ka use `sorted()` ke saath
#~ custom sorting ke liye bhi hota hai.

#* names = ["Pravin", "Amit", "Rahul", "Om"]

#* result = sorted(names, key=lambda x: len(x))

#* print(result)

#^ Output:

#^ ['Om', 'Amit', 'Rahul', 'Pravin']


#~ Yahan:

#^ `key=lambda x: len(x)`
#~ → Names ko unki length ke basis
#~ par sort karta hai.


#& ----------------------------------------
#& Important Rules
#& ----------------------------------------

#~ Lambda function mein:

#^ ✔ `lambda` keyword use hota hai.

#^ ✔ Arguments ho sakte hain.

#^ ✔ Multiple arguments ho sakte hain.

#^ ✔ Sirf ek expression hota hai.

#^ ✔ Expression ka result automatically return hota hai.

#^ ✔ `return` keyword ki zarurat nahi hoti.


#& ----------------------------------------
#& Lambda and return
#& ----------------------------------------

#? Normal Function

#* def add(x, y):
#*     return x + y


#? Lambda

#* add = lambda x, y: x + y


#~ Lambda mein `return` nahi likhte.

#~ Expression ka result automatically
#~ return ho jata hai.


#& ----------------------------------------
#& Lambda Limitations
#& ----------------------------------------

#~ Lambda simple operations ke liye
#~ useful hai.

#~ Lekin complex logic ke liye
#~ normal `def` function better hai.

#^ Lambda:

#~ ✔ Short

#~ ✔ Simple

#~ ✔ One expression


#^ Normal Function:

#~ ✔ Complex logic

#~ ✔ Multiple statements

#~ ✔ Multiple operations


#& ----------------------------------------
#& Important Difference
#& ----------------------------------------

#^ Normal Function

#* def function_name():
#*     statements
#*     return value


#^ Lambda Function

#* lambda arguments: expression


#~ Normal function ka naam hota hai.

#~ Lambda function anonymous hota hai.



#& ----------------------------------------
#& Most Important Syntax
#& ----------------------------------------

#^ One Argument

#* lambda x: expression


#^ Two Arguments

#* lambda x, y: expression


#^ Multiple Arguments

#* lambda x, y, z: expression


#^ With if-else

#* lambda x: value1 if condition else value2


#& ----------------------------------------
#& Quick Revision
#& ----------------------------------------

#~ Lambda ek small anonymous function hai.

#~ Iska use short aur simple operations
#~ ke liye hota hai.

#^ Syntax:

#^ lambda arguments: expression

#~ `return` keyword nahi likhte.

#~ Expression ka result automatically
#~ return hota hai.

#~ Lambda ka common use:

#^ • map()

#^ • filter()

#^ • sorted()


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is Lambda Function?

#~ Lambda is a small anonymous function
#~ in Python that can take arguments
#~ and return a result using a single
#~ expression.



#? Assignment:

#& 🔴 Question 1 – Square

#* Create a Lambda function named `square`.

#^ Find the square of a number.

#^ Use:

#^ 5

#* Print the result.

#^ Expected Output:

#^ 25

# square = lambda x : x * x
# print(square(5))



#& 🔴 Question 2 – Double

#* Create a Lambda function named `double`.

#^ Multiply a number by 2.

#^ Use:

#^ 10

#* Print the result.

#^ Expected Output:

#^ 20

# multiple = lambda x : x * 2
# print(multiple(10))



#& 🔴 Question 3 – Add Two Numbers

#* Create a Lambda function named `add`.

#^ Take two numbers as arguments.

#^ Add both numbers.

#^ Use:

#^ 10, 20

#* Print the result.

#^ Expected Output:

#^ 30

# add = lambda x, y : x + y
# print(add(10, 20))



#& 🔴 Question 4 – Find Maximum

#* Create a Lambda function named `maximum`.

#^ Take two numbers as arguments.

#^ Return the greater number.

#^ Use:

#^ 25, 40

#* Print the result.

#^ Expected Output:

#^ 40

# maximum = lambda x, y : x if x > y else y
# print(maximum(25, 40))



#& 🔴 Question 5 – Even or Odd

#* Create a Lambda function named `check_number`.

#^ If the number is even → `"Even"`

#^ Otherwise → `"Odd"`

#^ Use:

#^ 15

#* Print the result.

#^ Expected Output:

#^ Odd

# odd_even = lambda x : "Even" if x % 2 == 0 else "Odd"
# print(odd_even(15))



#& 🔴 Question 6 – Pass or Fail

#* Create a Lambda function named `result`.

#^ If marks are 50 or above → `"Pass"`

#^ Otherwise → `"Fail"`

#^ Use:

#^ 75

#* Print the result.

#^ Expected Output:

#^ Pass

# result = lambda x : "Pass" if x >= 50 else "Fail"
# print(result(75))



#& 🔴 Question 7 – Uppercase

#* Create a Lambda function named `upper_name`.

#^ Convert a name into uppercase.

#^ Use:

#^ "Pravin"

#* Print the result.

#^ Expected Output:

#^ PRAVIN

# uppercase = lambda x : x.upper()
# print(uppercase("Pravin"))



#& 🔴 Question 8 – Name Length

#* Create a Lambda function named `name_length`.

#^ Find the length of a name.

#^ Use:

#^ "Pravin"

#* Print the result.

#^ Expected Output:

#^ 6

# name_length = lambda x : len(x)
# print(name_length("Pravin"))