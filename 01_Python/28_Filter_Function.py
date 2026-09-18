 #! ==========================================
#! filter() Function
#! ==========================================


#? What is filter()?

#~ `filter()` Python ka ek built-in function hai
#~ jo iterable ke elements mein se
#~ sirf un elements ko select karta hai
#~ jo given condition ko satisfy karte hain.

#~ Simple Line:

#~ Filter → Condition Check → Matching Elements


#& ----------------------------------------
#& Why do we use filter()?
#& ----------------------------------------

#~ `filter()` ka use mainly:

#^ • Unwanted elements ko remove karne ke liye.
#^ • Specific condition satisfy karne wale
#^  elements ko select karne ke liye.
#^ • Data ko filter karne ke liye.
#^ • Large collection mein required data
#^   find karne ke liye.


#& ----------------------------------------
#& Syntax
#& ----------------------------------------

#* filter(function, iterable)


#~ Yahan:

#^ function → Condition check karta hai.

#^ iterable → Jiske elements ko filter
#^             karna hai.


#~ Simple Formula:

#^ Iterable → Condition → Selected Elements


#& ----------------------------------------
#& Simple Example
#& ----------------------------------------

#* numbers = [1, 2, 3, 4, 5, 6]

#* result = filter(lambda x: x % 2 == 0, numbers)

#* print(list(result))

#^ Output:

#^ [2, 4, 6]


#~ Yahan:

#^ `lambda x: x % 2 == 0`
#~ → Check karta hai number even hai ya nahi.

#^ `filter()`
#~ → Sirf even numbers ko select karta hai.


#& ----------------------------------------
#& How filter() Works?
#& ----------------------------------------

#~ Suppose:

#^ numbers = [1, 2, 3, 4, 5]

#~ Condition:

#^ x % 2 == 0

#~ Python har element ko check karega:

#^ 1 → False → Remove

#^ 2 → True  → Keep

#^ 3 → False → Remove

#^ 4 → True  → Keep

#^ 5 → False → Remove

#^ Final Result:

#^ [2, 4]


#& ----------------------------------------
#& filter() with Normal Function
#& ----------------------------------------

#* def is_even(x):
#*     return x % 2 == 0

#* numbers = [1, 2, 3, 4, 5, 6]

#* result = filter(is_even, numbers)

#* print(list(result))

#^ Output:

#^ [2, 4, 6]


#~ Yahan:

#^ `is_even()` → Condition

#^ `numbers` → Iterable

#^ `filter()` → Matching elements select karega.


#& ----------------------------------------
#& filter() with Lambda
#& ----------------------------------------

#~ `filter()` ke saath Lambda function
#~ commonly use kiya jata hai.

#* numbers = [10, 15, 20, 25, 30]

#* result = filter(lambda x: x > 20, numbers)

#* print(list(result))

#^ Output:

#^ [25, 30]


#~ Yahan condition hai:

#^ x > 20

#~ Isliye sirf 20 se greater
#~ numbers select hue.


#& ----------------------------------------
#& Filter Even Numbers
#& ----------------------------------------

#* numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#* result = filter(lambda x: x % 2 == 0, numbers)

#* print(list(result))

#^ Output:

#^ [2, 4, 6, 8]


#& ----------------------------------------
#& Filter Odd Numbers
#& ----------------------------------------

#* numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#* result = filter(lambda x: x % 2 != 0, numbers)

#* print(list(result))

#^ Output:

#^ [1, 3, 5, 7]


#& ----------------------------------------
#& Filter Numbers Greater Than 50
#& ----------------------------------------

#* numbers = [20, 45, 60, 75, 30, 90]

#* result = filter(lambda x: x > 50, numbers)

#* print(list(result))

#^ Output:

#^ [60, 75, 90]


#& ----------------------------------------
#& Filter Strings
#& ----------------------------------------

#* names = ["Pravin", "Amit", "Rahul", "Om"]

#* result = filter(lambda x: len(x) > 4, names)

#* print(list(result))

#^ Output:

#^ ['Pravin', 'Rahul']


#~ Yahan:

#^ `len(x) > 4`
#~ → Sirf 4 characters se longer
#~ names select honge.


#& ----------------------------------------
#& filter() Returns What?
#& ----------------------------------------

#~ Python 3 mein `filter()` directly
#~ list return nahi karta.

#~ Ye ek **filter object** return karta hai.

#* numbers = [1, 2, 3, 4]

#* result = filter(lambda x: x > 2, numbers)

#* print(result)

#^ Output:

#^ <filter object at ...>


#~ Actual values dekhne ke liye
#~ `list()` use karte hain.

#* print(list(result))

#^ Output:

#^ [3, 4]


#& ----------------------------------------
#& filter() with Tuple
#& ----------------------------------------

#* numbers = (10, 15, 20, 25, 30)

#* result = filter(lambda x: x >= 20, numbers)

#* print(tuple(result))

#^ Output:

#^ (20, 25, 30)


#~ `filter()` kisi bhi iterable ke
#~ saath use ho sakta hai.


#& ----------------------------------------
#& filter() vs map()
#& ----------------------------------------

#^ map()

#~ Har element par operation perform karta hai.

#~ Main purpose:

#^ Transform / Modify


#^ filter()

#~ Condition ke basis par elements
#~ select karta hai.

#~ Main purpose:

#^ Select / Filter


#? Example:

#^ numbers = [1, 2, 3, 4, 5]


#^ map()

#* list(map(lambda x: x * 2, numbers))

#^ Output:

#^ [2, 4, 6, 8, 10]


#^ filter()

#* list(filter(lambda x: x > 3, numbers))

#^ Output:

#^ [4, 5]


#& ----------------------------------------
#& filter() vs List Comprehension
#& ----------------------------------------

#^ filter()

#* list(filter(lambda x: x % 2 == 0, numbers))


#^ List Comprehension

#* [x for x in numbers if x % 2 == 0]


#~ Dono se same type ka result
#~ mil sakta hai.

#~ `filter()` mein condition function ke
#~ through di jaati hai.

#~ List Comprehension mein condition
#~ directly likhte hain.


#& ----------------------------------------
#& Important Point
#& ----------------------------------------

#~ `filter()` ka main purpose
#~ elements ko transform karna nahi hai.

#~ Iska main purpose hai:

#^ **Condition ke basis par
#^ elements ko select karna.**


#? Example:

#^ [10, 20, 30, 40]

#~ Condition:

#^ x > 20

#~ Result:

#^ [30, 40]


#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#~ `filter()` ko yaad rakho:

#^ FILTER = Select


#~ Simple Formula:

#^ Input → Condition → Selected Data


#^ Example:

#^ [1, 2, 3, 4, 5]

#^ Condition → Even

#^ Result → [2, 4]


#& ----------------------------------------
#& Important Rules
#& ----------------------------------------

#~ `filter()`:

#^ ✔ Built-in Python function hai.

#^ ✔ Condition/function leta hai.

#^ ✔ Iterable leta hai.

#^ ✔ Sirf condition satisfy karne wale
#^   elements ko select karta hai.

#^ ✔ Python 3 mein filter object return karta hai.

#^ ✔ Values dekhne ke liye `list()` use
#^   kar sakte hain.

#^ ✔ Lambda ke saath commonly use hota hai.


#& ----------------------------------------
#& Quick Revision
#& ----------------------------------------

#~ `filter()` ek built-in function hai
#~ jo condition ke basis par iterable
#~ se required elements select karta hai.

#^ Syntax:

#^ filter(function, iterable)

#^ Returns:

#^ Filter Object

#^ Values ke liye:

#^ list(filter(...))


#^ Main Use:

#^ Select / Filter Elements


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is filter()?

#~ `filter()` is a built-in Python function
#~ that selects elements from an iterable
#~ based on a given condition and returns
#~ a filter object containing the matching
#~ elements.


#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#~ filter() = Condition Based Selection

#^ Syntax:

#^ filter(function, iterable)

#^ Simple Formula:

#^ Iterable → Condition → Selected Elements


#^ Remember:

#^ map()    → Transform

#^ filter() → Select


#? Assignment:


#& 🔴 Question 1 – Even Numbers

#* Create a list named `numbers`.

#^ [1, 2, 3, 4, 5, 6]

#* Use `filter()` with Lambda.

#^ Store only even numbers.

#* Print the result as a list.

#^ Expected Output:

#^ [2, 4, 6]

# numbers = [1, 2, 3, 4, 5, 6]

# result = list(filter(lambda x : x % 2 == 0, numbers))
# print(result)



#& 🔴 Question 2 – Odd Numbers

#* Create a list named `numbers`.

#^ [1, 2, 3, 4, 5, 6, 7]

#* Use `filter()` with Lambda.

#^ Store only odd numbers.

#* Print the result as a list.

#^ Expected Output:

#^ [1, 3, 5, 7]

# numbers = [1, 2, 3, 4, 5, 6, 7]

# result = list(filter(lambda x : x % 2 == 1, numbers))
# print(result)



#& 🔴 Question 3 – Greater Than 50

#* Create a list named `numbers`.

#^ [20, 45, 60, 75, 30, 90]

#* Use `filter()` with Lambda.

#^ Store only numbers greater than 50.

#* Print the result as a list.

#^ Expected Output:

#^ [60, 75, 90]

# numbers = [20, 45, 60, 75, 30, 90]

# result = list(filter(lambda x : x > 50, numbers))
# print(result)



#& 🔴 Question 4 – Positive Numbers

#* Create a list named `numbers`.

#^ [-5, 10, -2, 20, 0, 15]

#* Use `filter()` with Lambda.

#^ Store only positive numbers.

#* Print the result as a list.

#^ Expected Output:

#^ [10, 20, 15]

# numbers = [-5, 10, -2, 20, 0, 15]

# result = list(filter(lambda x : x > 0, numbers))
# print(result)



#& 🔴 Question 5 – Pass Students

#* Create a dictionary named `students`.

#^ {"Pravin": 75, "Rahul": 45, "Amit": 85, "Vijay": 35}

#* Create a function named `is_passed()`.

#^ Return `True` if marks are 50 or above.

#^ Otherwise return `False`.

#* Use `filter()` to find passed students.

#* Print the result.

# students = {"Pravin": 75, "Rahul": 45, "Amit": 85, "Vijay": 35}

# def is_passed(x):

#     return students[x] >= 50

# result = list(filter(is_passed, students))
# print(result)



#& 🔴 Question 6 – Long Names

#* Create a list named `names`.

#^ ["Pravin", "Amit", "Rahul", "Vijay", "Om"]

#* Create a function named `is_long_name()`.

#^ Return `True` if the name has more than 4 characters.

#* Use `filter()` to select the names.

#* Print the result as a list.

#^ Expected Output:

#^ ['Pravin', 'Rahul', 'Vijay']

# names = ["Pravin", "Amit", "Rahul", "Vijay", "Om"]

# def is_long_name(x):

#     return len(x) > 4

# result = list(filter(is_long_name, names))
# print(result)



#& 🔴 Question 7 – Salary Filter

#* Create a list named `salaries`.

#^ [25000, 40000, 55000, 30000, 70000]

#* Use `filter()` with Lambda.

#^ Store salaries greater than 40000.

#* Print the result as a list.

#^ Expected Output:

#^ [55000, 70000]

# salaries = [25000, 40000, 55000, 30000, 70000]

# result = list(filter(lambda x : x > 40000, salaries))
# print(result)



#& 🔴 Question 8 – Names Starting with P

#* Create a list named `names`.

#^ ["Pravin", "Rahul", "Pooja", "Amit", "Priya"]

#* Use `filter()` with Lambda.

#^ Store names starting with `"P"`.

#* Print the result as a list.

#^ Expected Output:

#^ ['Pravin', 'Pooja', 'Priya']

# names = ["Pravin", "Rahul", "Pooja", "Amit", "Priya"]

# result = list(filter(lambda x : x[0] == "P", names))
# print(result)



#& 🔴 Question 9 – Numbers Divisible by 5

#* Create a list named `numbers`.

#^ [10, 12, 15, 22, 25, 30, 33]

#* Use `filter()` with Lambda.

#^ Store numbers divisible by 5.

#* Print the result as a list.

#^ Expected Output:

#^ [10, 15, 25, 30]

# numbers = [10, 12, 15, 22, 25, 30, 33]

# result = list(filter(lambda x : x % 5 == 0, numbers))
# print(result)



#& 🔴 Question 10 – Age Filter

#* Create a list named `ages`.

#^ [12, 18, 25, 15, 30, 16]

#* Use `filter()` with Lambda.

#^ Store ages that are 18 or above.

#* Print the result as a list.

#^ Expected Output:

#^ [18, 25, 30]

# ages = [12, 18, 25, 15, 30, 16]

# result = list(filter(lambda x : x >= 18, ages))
# print(result)