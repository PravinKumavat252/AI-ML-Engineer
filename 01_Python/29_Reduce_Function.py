
#! ==========================================
#! reduce() Function
#! ==========================================


#? What is reduce()?

#~ `reduce()` ek function hai jo
#~ iterable ke multiple elements ko
#~ repeatedly combine karke
#~ ek single final result mein convert karta hai.

#~ Simple Line:

#~ Multiple Values → Combine → One Value


#~ Example:

#^ [1, 2, 3, 4, 5]

#~ Agar hum sum karna chahte hain:

#^ 1 + 2 + 3 + 4 + 5

#^ Result → 15

#~ Yahan multiple values ko combine karke
#~ ek single value mili.


#& ----------------------------------------
#& Why do we use reduce()?
#& ----------------------------------------

#~ `reduce()` ka use mainly:

#^ 1. Multiple values ko combine karne ke liye.
#^ 2. Total/Sum calculate karne ke liye.
#^ 3. Product calculate karne ke liye.
#^ 4. Maximum ya minimum value find karne ke liye.
#^ 5. Repeated calculation perform karne ke liye.


#& ----------------------------------------
#& Import reduce()
#& ----------------------------------------

#~ `reduce()` Python ke `functools` module
#~ ke andar available hota hai.

#~ Isliye `reduce()` use karne ke liye
#~ pehle import karna padta hai.

#^ Syntax:

#* from functools import reduce


#& ----------------------------------------
#& Basic Syntax
#& ----------------------------------------

#* reduce(function, iterable)


#~ Yahan:

#^ function → Do values ko combine karta hai.

#^ iterable → Jiske elements par
#^             operation perform hoga.


#~ Simple Formula:

#^ Iterable → Combine → Combine → Final Result


#& ----------------------------------------
#& Simple Example – Addition
#& ----------------------------------------

#* from functools import reduce

#* numbers = [1, 2, 3, 4, 5]

#* result = reduce(lambda x, y: x + y, numbers)

#* print(result)

#^ Output:

#^ 15


#~ Working:

#^ 1 + 2 → 3

#^ 3 + 3 → 6

#^ 6 + 4 → 10

#^ 10 + 5 → 15


#~ Final Result:

#^ 15


#& ----------------------------------------
#& How reduce() Works?
#& ----------------------------------------

#~ Suppose:

#^ numbers = [10, 20, 30, 40]

#~ Operation:

#^ x + y


#~ Step 1:

#^ 10 + 20 = 30


#~ Step 2:

#^ 30 + 30 = 60


#~ Step 3:

#^ 60 + 40 = 100


#^ Final Result → 100


#~ Important:

#~ `reduce()` previous result ko
#~ next element ke saath combine karta hai.


#& ----------------------------------------
#& reduce() with Normal Function
#& ----------------------------------------

#* from functools import reduce

#* def add(x, y):
#*     return x + y

#* numbers = [10, 20, 30, 40]

#* result = reduce(add, numbers)

#* print(result)

#^ Output:

#^ 100


#~ Yahan:

#^ `add()` → Combination Logic

#^ `numbers` → Iterable

#^ `reduce()` → Final single value


#& ----------------------------------------
#& reduce() with Lambda
#& ----------------------------------------

#~ `reduce()` ke saath Lambda commonly
#~ use kiya jata hai.

#* from functools import reduce

#* numbers = [2, 3, 4, 5]

#* result = reduce(lambda x, y: x * y, numbers)

#* print(result)

#^ Output:

#^ 120


#~ Working:

#^ 2 × 3 = 6

#^ 6 × 4 = 24

#^ 24 × 5 = 120


#& ----------------------------------------
#& Find Product
#& ----------------------------------------

#* from functools import reduce

#* numbers = [1, 2, 3, 4, 5]

#* result = reduce(lambda x, y: x * y, numbers)

#* print(result)

#^ Output:

#^ 120


#~ Yahan sabhi numbers ko
#~ multiply karke single result mila.


#& ----------------------------------------
#& Find Maximum
#& ----------------------------------------

#* from functools import reduce

#* numbers = [25, 10, 45, 30, 60]

#* result = reduce(lambda x, y: x if x > y else y, numbers)

#* print(result)

#^ Output:

#^ 60


#~ Har step par greater value
#~ next value ke saath compare hoti hai.


#& ----------------------------------------
#& Find Minimum
#& ----------------------------------------

#* from functools import reduce

#* numbers = [25, 10, 45, 30, 60]

#* result = reduce(lambda x, y: x if x < y else y, numbers)

#* print(result)

#^ Output:

#^ 10


#& ----------------------------------------
#& reduce() with Initial Value
#& ----------------------------------------

#~ `reduce()` mein hum optional
#~ initial value bhi provide kar sakte hain.

#^ Syntax:

#* reduce(function, iterable, initial_value)


#~ Example:

#* from functools import reduce

#* numbers = [1, 2, 3, 4]

#* result = reduce(lambda x, y: x + y, numbers, 10)

#* print(result)

#^ Output:

#^ 20


#~ Working:

#^ Initial value = 10

#^ 10 + 1 = 11

#^ 11 + 2 = 13

#^ 13 + 3 = 16

#^ 16 + 4 = 20


#~ Final Result:

#^ 20


#& ----------------------------------------
#& reduce() vs map()
#& ----------------------------------------

#^ map()

#~ Har element ko transform karta hai.

#~ Output mein generally
#~ multiple elements hote hain.


#^ reduce()

#~ Multiple elements ko repeatedly
#~ combine karta hai.

#~ Output mein generally
#~ single final value hoti hai.


#? Example:

#^ numbers = [1, 2, 3, 4]


#^ map()

#* list(map(lambda x: x * 2, numbers))

#^ Output:

#^ [2, 4, 6, 8]


#^ reduce()

#* reduce(lambda x, y: x + y, numbers)

#^ Output:

#^ 10


#& ----------------------------------------
#& reduce() vs filter()
#& ----------------------------------------

#^ filter()

#~ Condition ke basis par
#~ elements select karta hai.

#^ Main Purpose:

#~ Select


#^ reduce()

#~ Multiple elements ko
#~ combine karke one result banata hai.

#^ Main Purpose:

#~ Combine


#& ----------------------------------------
#& map() vs filter() vs reduce()
#& ----------------------------------------

#^ map()

#~ Transform each element.

#^ Example:

#~ [1, 2, 3]

#~ × 2

#~ [2, 4, 6]


#^ filter()

#~ Select matching elements.

#^ Example:

#~ [1, 2, 3, 4]

#~ Even

#~ [2, 4]


#^ reduce()

#~ Combine all elements.

#^ Example:

#~ [1, 2, 3, 4]

#~ Sum

#~ 10


#& ----------------------------------------
#& Important Point
#& ----------------------------------------

#~ `reduce()` Python ka normal built-in
#~ function nahi hai.

#~ Ye `functools` module ka function hai.

#~ Isliye import karna zaroori hai:

#* from functools import reduce


#& ----------------------------------------
#& Important Rules
#& ----------------------------------------

#~ `reduce()`:

#^ ✔ `functools` module mein available hai.

#^ ✔ Multiple elements ko combine karta hai.

#^ ✔ Usually single final result return karta hai.

#^ ✔ Lambda ke saath commonly use hota hai.

#^ ✔ Normal function ke saath bhi use
#^   kar sakte hain.

#^ ✔ Optional initial value provide
#^   kar sakte hain.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is reduce()?

#~ `reduce()` is a function from the
#~ `functools` module that repeatedly applies
#~ a function to the elements of an iterable
#~ and reduces them to a single final result.


#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#~ `reduce()` → Multiple values ko
#~ repeatedly combine karke
#~ ek single final value banata hai.

#^ Syntax:

#^ from functools import reduce

#^ reduce(function, iterable)

#^ Optional:

#^ reduce(function, iterable, initial_value)


#^ Remember:

#^ map()    → Transform

#^ filter() → Select

#^ reduce() → Combine


#? Assignment:


#& 🔴 Question 1 – Sum of Numbers

#* Create a list named `numbers`.

#^ [1, 2, 3, 4, 5]

#* Import `reduce()` from `functools`.

#* Use `reduce()` with Lambda.

#^ Add all numbers.

#* Print the result.

#^ Expected Output:

#^ 15

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# result = reduce(lambda x, y : x+y, numbers)
# print(result)



#& 🔴 Question 2 – Product of Numbers

#* Create a list named `numbers`.

#^ [1, 2, 3, 4, 5]

#* Use `reduce()` with Lambda.

#^ Multiply all numbers.

#* Print the result.

#^ Expected Output:

#^ 120

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# result = reduce(lambda x, y : x*y, numbers)
# print(result)


#& 🔴 Question 3 – Sum of Even Numbers

#* Create a list named `numbers`.

#^ [2, 4, 6, 8]

#* Use `reduce()` with Lambda.

#^ Find the total of all numbers.

#* Print the result.

#^ Expected Output:

#^ 20

# from functools import reduce

# numbers = [2, 4, 6, 8]

# result = reduce(lambda x, y : x+y, numbers)
# print(result)



#& 🔴 Question 4 – Add Using Function

#* Create a function named `add()`.

#^ Take two numbers.

#^ Return their sum.

#* Create a list:

#^ [10, 20, 30, 40]

#* Use `reduce()` with the `add()` function.

#* Print the result.

#^ Expected Output:

#^ 100

# from functools import reduce

# lst = [10, 20, 30, 40]

# def add(a, b):
#     return a + b

# result = reduce(add, lst)
# print(result)



#& 🔴 Question 5 – Find Maximum

#* Create a list named `numbers`.

#^ [25, 10, 45, 30, 60]

#* Use `reduce()` with Lambda.

#^ Find the maximum number.

#* Print the result.

#^ Expected Output:

#^ 60

# from functools import reduce

# numbers = [25, 10, 45, 30, 60]

# result = reduce(lambda x, y : x if x > y else y, numbers)
# print(result)



#& 🔴 Question 6 – Find Minimum

#* Create a list named `numbers`.

#^ [25, 10, 45, 30, 60]

#* Use `reduce()` with Lambda.

#^ Find the minimum number.

#* Print the result.

#^ Expected Output:

#^ 10

# from functools import reduce

# numbers = [25, 10, 45, 30, 60]

# result = reduce(lambda x, y : x if x < y else y, numbers)
# print(result)



#& 🔴 Question 7 – Initial Value

#* Create a list named `numbers`.

#^ [1, 2, 3, 4]

#* Use `reduce()` with Lambda.

#^ Add all numbers.

#^ Use `10` as the initial value.

#* Print the result.

#^ Expected Output:

#^ 20

# from functools import reduce

# numbers = [1, 2, 3, 4]

# result = reduce(lambda x, y : x+y, numbers, 10)
# print(result)



#& 🔴 Question 8 – Total Price

#* Create a list named `prices`.

#^ [100, 250, 150, 500]

#* Use `reduce()` with Lambda.

#^ Find the total price.

#* Print the result.

#^ Expected Output:

#^ 1000

# from functools import reduce

# prices = [100, 250, 150, 500]

# result = reduce(lambda x, y : x+y, prices)
# print(result)