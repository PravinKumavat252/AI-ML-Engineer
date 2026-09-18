 #! ==========================================
#! map() Function
#! ==========================================


#? What is map()?

#~ `map()` Python ka ek built-in function hai
#~ jo kisi function ko collection ke
#~ har element par apply karta hai.

#~ Simple Line:

#~ One Function → Every Element


#& ----------------------------------------
#& Why do we use map()?
#& ----------------------------------------

#~ `map()` ka use mainly:

#^ • Har element par same operation perform karne ke liye.
#^ • List ke elements ko transform karne ke liye.
#^ • Loop ko short aur readable banane ke liye.
#^ • Ek collection se new values generate karne ke liye.


#& ----------------------------------------
#& Syntax
#& ----------------------------------------

#* map(function, iterable)

#~ Yahan:

#^ function → Jo operation perform karna hai.

#^ iterable → Jiske har element par
#^             function apply hoga.


#& ----------------------------------------
#& Simple Example
#& ----------------------------------------

#* def square(x):
#*     return x * x

#* numbers = [1, 2, 3, 4, 5]

#* result = map(square, numbers)

#* print(list(result))

#^ Output:

#^ [1, 4, 9, 16, 25]


#~ Yahan:

#^ square() → Function

#^ numbers → Iterable

#^ map() → Har number par square()
#^          apply karta hai.


#& ----------------------------------------
#& map() with Lambda
#& ----------------------------------------

#~ `map()` ke saath Lambda function
#~ commonly use kiya jata hai.

#* numbers = [1, 2, 3, 4, 5]

#* result = map(lambda x: x * 2, numbers)

#* print(list(result))

#^ Output:

#^ [2, 4, 6, 8, 10]


#~ Yahan:

#^ lambda x: x * 2
#~ → Har number ko 2 se multiply karega.


#& ----------------------------------------
#& map() with String
#& ----------------------------------------

#* names = ["pravin", "rahul", "amit"]

#* result = map(str.upper, names)

#* print(list(result))

#^ Output:

#^ ['PRAVIN', 'RAHUL', 'AMIT']


#~ Yahan `str.upper` function
#~ har string par apply hua.


#& ----------------------------------------
#& map() with Multiple Iterables
#& ----------------------------------------

#~ `map()` ek se zyada iterable ke
#~ saath bhi kaam kar sakta hai.

#* numbers1 = [1, 2, 3]
#* numbers2 = [10, 20, 30]

#* result = map(lambda x, y: x + y,
#*              numbers1, numbers2)

#* print(list(result))

#^ Output:

#^ [11, 22, 33]


#~ Yahan:

#^ 1 + 10 → 11

#^ 2 + 20 → 22

#^ 3 + 30 → 33


#& ----------------------------------------
#& map() Returns What?
#& ----------------------------------------

#~ Python 3 mein `map()` directly
#~ list return nahi karta.

#~ Ye ek **map object** return karta hai.

#* numbers = [1, 2, 3]

#* result = map(lambda x: x * 2, numbers)

#* print(result)

#^ Output:

#^ <map object at ...>


#~ Actual values dekhne ke liye
#~ usually `list()` use karte hain.

#* print(list(result))

#^ Output:

#^ [2, 4, 6]


#& ----------------------------------------
#& map() with Normal for Loop
#& ----------------------------------------

#~ Same kaam normal `for` loop se:

#* numbers = [1, 2, 3, 4, 5]

#* result = []

#* for i in numbers:
#*     result.append(i * 2)

#* print(result)


#~ `map()` se:

#* numbers = [1, 2, 3, 4, 5]

#* result = map(lambda x: x * 2, numbers)

#* print(list(result))


#~ Dono ka output same hai:

#^ [2, 4, 6, 8, 10]


#& ----------------------------------------
#& map() vs List Comprehension
#& ----------------------------------------

#^ List Comprehension

#* [x * 2 for x in numbers]


#^ map()

#* list(map(lambda x: x * 2, numbers))


#~ Dono ka result same ho sakta hai.

#~ List Comprehension mein
#~ expression directly likhte hain.

#~ `map()` mein function ko
#~ elements par apply karte hain.


#& ----------------------------------------
#& Important Point
#& ----------------------------------------

#~ `map()` ka main purpose
#~ **filter karna nahi hai.**

#~ `map()` ka main purpose hai:

#^ **Transform / Modify each element**


#? Example:

#^ [1, 2, 3, 4]

#~ Har element ko double karna:

#^ [2, 4, 6, 8]

#~ Yahan `map()` suitable hai.


#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#~ `map()` ko yaad rakho:

#^ MAP = Modify / Transform


#~ Simple formula:

#^ Function + Every Element


#^ map(function, iterable)


#& ----------------------------------------
#& Quick Revision
#& ----------------------------------------

#~ `map()` ek built-in function hai.

#~ Ye function ko iterable ke
#~ har element par apply karta hai.

#^ Syntax:

#^ map(function, iterable)

#^ Returns:

#^ Map Object

#^ Values ke liye:

#^ list(map(...))


#~ Main Use:

#^ Transform / Modify elements


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is map()?

#~ `map()` is a built-in Python function
#~ that applies a given function to every
#~ item of an iterable and returns a
#~ map object containing the results.


#^ Assignment:

#& 🔴 Question 1 – Double Numbers

#* Create a list:

#^ [1, 2, 3, 4, 5]

#* Use `map()` to multiply every number by `2`.

#* Print the result as a list.

# lst = [1, 2, 3, 4, 5]

# result = list(map(lambda x : x*2, lst))
# print(result)



#& 🔴 Question 2 – Square Numbers

#* Create a list:

#^ [1, 2, 3, 4, 5]

#* Use `map()` to find the square of
#* every number.

#* Print the result as a list.

# lst = [1, 2, 3, 4, 5]

# result = list(map(lambda x : x*x, lst))
# print(result)



#& 🔴 Question 3 – Add 10

#* Create a list:

#^ [5, 10, 15, 20]

#* Use `map()` to add `10` to every number.

#* Print the result as a list.

# lst = [5, 10, 15, 20]

# result = list(map(lambda x : x+10, lst))
# print(result)



#& 🔴 Question 4 – Convert to Uppercase

#* Create a list:

#^ ["python", "java", "sql"]

#* Use `map()` to convert every string
#* into uppercase.

#* Print the result as a list.

# lst = ["python", "java", "sql"]

# result = list(map(lambda x : x.upper(), lst))
# print(result)



#& 🔴 Question 5 – Find Length

#* Create a list:

#^ ["Pravin", "Rahul", "Amit"]

#* Use `map()` to find the length of
#* every name.

#* Print the result as a list.

# lst = ["Pravin", "Rahul", "Amit"]

# result = list(map(lambda x : len(x), lst))
# print(result)



#& 🔴 Question 6 – Cube Using Function

#* Create a function named `cube()`.

#^ Return the cube of a number.

#* Create a list:

#^ [1, 2, 3, 4]

#* Use `map()` with the `cube()` function.

#* Print the result as a list.

# lst = [1, 2, 3, 4]

# result = list(map(lambda x : x**3, lst))
# print(result)



#& 🔴 Question 7 – Even or Odd

#* Create a function named `check_number()`.

#^ If the number is even → return `"Even"`.

#^ Otherwise → return `"Odd"`.

#* Create a list:

#^ [1, 2, 3, 4, 5]

#* Use `map()` with `check_number()`.

#* Print the result as a list.

# lst = [1, 2, 3, 4, 5]

# def check_number(x):
#      if x % 2 == 0:
#           return "Even"
#      else:
#           return "Odd"

# result = list(map(check_number, lst))
# print(result)



#& 🔴 Question 8 – Multiply by 5

#* Create a list:

#^ [2, 4, 6, 8]

#* Use `map()` with a Lambda function.

#^ Multiply every number by `5`.

#* Print the result as a list.

# lst = [2, 4, 6, 8]

# result = list(map(lambda x : x*5, lst))
# print(result)



#& 🔴 Question 9 – Convert Celsius to Fahrenheit

#* Create a list:

#^ [0, 10, 20, 30]

#* Use `map()` with Lambda.

#^ Formula:

#^ `(C × 9/5) + 32`

#* Print the result as a list.

# lst = [0, 10, 20, 30]

# result = list(map(lambda x : (x * 9/5) + 32, lst))
# print(result)



#& 🔴 Question 10 – Add Two Lists

#* Create two lists:

#^ [1, 2, 3, 4]

#^ [10, 20, 30, 40]

#* Use `map()` with Lambda.

#^ Add corresponding elements.

#* Print the result as a list.

#^ Expected:

#^ [11, 22, 33, 44]

# lst1 = [1, 2, 3, 4]
# lst2 = [10, 20, 30, 40]

# result = list(map(lambda x, y : x+y, lst1, lst2))
# print(result)