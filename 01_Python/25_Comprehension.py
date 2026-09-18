 #! 🔵 CHAPTER – COMPREHENSIONS

#& 🔵 1. What is Comprehension?

#~ Comprehension Python ka ek **short and simple way** hai jisse hum kisi existing **iterable** se ek **new collection** create kar sakte hain.

#~ Isme hum **loop, expression aur condition** ko ek compact syntax mein likh sakte hain.

#^ Simple meaning:

#^ **Comprehension = Loop + Expression + Optional Condition**

#? Example:

#^ Normal Loop:

#* numbers = [1, 2, 3, 4]
#* result = []

#* for number in numbers:
#*     result.append(number * 2)

#^ Comprehension:

#* result = [number * 2 for number in numbers]



#& 🔵 2. Why is Comprehension Used?

#~ Comprehension ka use mainly:

#^ 1. New collection create karne ke liye.

#^ 2. Loop ko short way mein likhne ke liye.

#^ 3. Data ko transform karne ke liye.

#^ 4. Data ko condition ke according filter karne ke liye.

#^ 5. Code ko concise banane ke liye.



#& 🔵 3. Importance of Comprehension

#~ Comprehension Python mein important hai kyunki:

#^ 1. **Less Code**
#~ Same task ko normal loop ke comparison mein kam lines mein likh sakte hain.

#^ 2. **Readable Code**
#~ Simple operations ke liye code easy to understand hota hai.

#^ 3. **Data Transformation**
#~ Existing data ke elements ko modify karke new collection bana sakte hain.

#^ 4. **Filtering**
#~ Conditions ke through required elements select kar sakte hain.

#^ 5. **Pythonic Code**
#~ Comprehensions Python mein commonly used aur recommended coding style hain.



#& 🔵 4. Types of Comprehension

#~ Python mein mainly **3 types of Comprehension** use ki jaati hain:

#^ 1. List Comprehension

#^ 2. Set Comprehension

#^ 3. Dictionary Comprehension

#~ Inke alawa **Generator Expression** bhi hota hai, jo similar syntax follow karta hai.



#& 🟢 5. List Comprehension

#~ List Comprehension ka use **new List** create karne ke liye hota hai.

#* Syntax 1 – Basic List Comprehension

#^ `[expression for item in iterable]`

#? Parts:

#^ `expression` → New value

#^ `for item` → Loop variable

#^ `in iterable` → Source data



#* Syntax 2 – List Comprehension with Condition

#^ `[expression for item in iterable if condition]`

#~ Yahan `if` ka use **filtering** ke liye hota hai.



#* Syntax 3 – List Comprehension with `if-else`

#^ `[value_if_true if condition else value_if_false for item in iterable]`

#~ Yahan condition ke according **different value** generate hoti hai.



#* Syntax 4 – Nested List Comprehension

#^ `[expression for item1 in iterable1 for item2 in iterable2]`

#~ Isme ek comprehension ke andar **multiple `for` loops** hote hain.



#& 🟡 6. Set Comprehension

#~ Set Comprehension ka use **new Set** create karne ke liye hota hai.

#* Syntax 1 – Basic Set Comprehension

#^ `{expression for item in iterable}`



#* Syntax 2 – Set Comprehension with Condition

#^ `{expression for item in iterable if condition}`



#* Syntax 3 – Set Comprehension with `if-else`

#^ `{value_if_true if condition else value_if_false for item in iterable}`



#& 🟠 7. Dictionary Comprehension

#~ Dictionary Comprehension ka use **new Dictionary** create karne ke liye hota hai.

#* Syntax 1 – Basic Dictionary Comprehension

#^ `{key: value for item in iterable}`



#* Syntax 2 – Dictionary Comprehension with Condition

#^ `{key: value for item in iterable if condition}`



#* Syntax 3 – Dictionary Comprehension with `if-else`

#^ `{key: value_if_true if condition else value_if_false for item in iterable}`



#* Syntax 4 – Dictionary Comprehension with Two Variables

#^ `{key: value for key, value in iterable}`

#~ Ye tab useful hota hai jab iterable se **key aur value dono** mil rahe ho.



#& 🔴 8. Generator Expression

#~ Generator Expression ka syntax Comprehension jaisa hota hai.

#~ Lekin ye directly complete collection create nahi karta. Ye values ko **one-by-one generate** karta hai.

#* Syntax:

#^ `(expression for item in iterable)`

#* With Condition:

#^ `(expression for item in iterable if condition)`


#& Assignment:


#& 🔴 Question 1 – Double the Numbers

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5]

#* Create a new list named result using List Comprehension.

#^ Multiply each number by 2.

#* Print the result.

#^ Expected Output:

#^ [2, 4, 6, 8, 10]

# lst = [1, 2, 3, 4, 5]
# print([i*2 for i in lst])



#& 🔴 Question 2 – Square of Numbers

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5]

#* Create a new list named squares using List Comprehension.

#^ Find the square of each number.

#* Print the squares.

#^ Expected Output:

#^ [1, 4, 9, 16, 25]

# lst = [1, 2, 3, 4, 5]
# print([i*i for i in lst])



#& 🔴 Question 3 – Convert to Uppercase

#* Create a list named names.

#^ ["Pravin", "Rahul", "Amit", "Vijay"]

#* Create a new list named upper_names using List Comprehension.

#^ Convert every name into uppercase.

#* Print the upper_names.

#^ Expected Output:

#^ ['PRAVIN', 'RAHUL', 'AMIT', 'VIJAY']

# lst = ["Pravin", "Rahul", "Amit", "Vijay"]
# print([i.upper() for i in lst])



#& 🔴 Question 4 – Add 10

#* Create a list named numbers.

#^ [5, 10, 15, 20, 25]

#* Create a new list named result using List Comprehension.

#^ Add 10 to every number.

#* Print the result.

#^ Expected Output:

#^ [15, 20, 25, 30, 35]

# lst = [5, 10, 15, 20, 25]
# print([i+10 for i in lst])



#& 🔴 Question 5 – Length of Names

#* Create a list named names.

#^ ["Pravin", "Rahul", "Amit", "Vijay"]

#* Create a new list named lengths using List Comprehension.

#^ Find the length of every name.

#* Print the lengths.

#^ Expected Output:

#^ [6, 5, 4, 5]

# lst = ["Pravin", "Rahul", "Amit", "Vijay"]
# print([len(i) for i in lst])



#& 🔴 Question 6 – Even Numbers

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#* Create a new list named even_numbers using List Comprehension.

#^ Store only even numbers.

#* Print the even_numbers.

#^ Expected Output:

#^ [2, 4, 6, 8, 10]

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i for i in lst if i % 2 == 0])



#& 🔴 Question 7 – Numbers Greater Than 50

#* Create a list named numbers.

#^ [20, 45, 60, 75, 30, 90, 40]

#* Create a new list named result using List Comprehension.

#^ Store only numbers greater than 50.

#* Print the result.

#^ Expected Output:

#^ [60, 75, 90]

# lst = [20, 45, 60, 75, 30, 90, 40]
# print([i for i in lst if i > 50])


#& 🔴 Question 8 – Even Numbers and Square

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5, 6]

#* Create a new list named result using List Comprehension.

#^ Select only even numbers.

#^ Find the square of those numbers.

#* Print the result.

#^ Expected Output:

#^ [4, 16, 36]

# lst = [1, 2, 3, 4, 5, 6]
# print([i**2 for i in lst if i % 2 == 0])


#& 🔴 Question 9 – Unique  

#* Create a list named numbers.

#^ [1, 2, 2, 3, 3, 4, 5]

#* Create a Set named squares using Set Comprehension.

#^ Find the square of each number.

#^ Duplicate values should automatically be removed.

#* Print the squares.

#^ Expected Output:

#^ {1, 4, 9, 16, 25}

# lst = [1, 2, 2, 3, 3, 4, 5]
# print({i*i for i in lst})



#& 🔴 Question 10 – Even Numbers Set

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#* Create a Set named even_numbers using Set Comprehension.

#^ Store only even numbers.

#* Print the even_numbers.

#^ Expected Output:

#^ {2, 4, 6, 8, 10}

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print({i for i in lst if i % 2 == 0})



#& 🔴 Question 11 – Number and Square

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5]

#* Create a dictionary named squares using Dictionary Comprehension.

#^ Number → Key

#^ Square → Value

#* Print the squares.

#^ Expected Output:

#^ {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# lst = [1, 2, 3, 4, 5]
# print({i : i*i for i in lst})



#& 🔴 Question 12 – Student Marks

#* Create a dictionary named students.

#^ {"Pravin": 75, "Rahul": 85, "Amit": 65, "Vijay": 90}

#* Create a new dictionary named passed_students using Dictionary Comprehension.

#^ Store only students whose marks are 70 or above.

#* Print the passed_students.

#^ Expected Output:

#^ {'Pravin': 75, 'Rahul': 85, 'Vijay': 90}

# dic = {"Pravin": 75, "Rahul": 85, "Amit": 65, "Vijay": 90}
# print({i : dic[i] for i in dic if dic[i] >= 70})



#& 🔴 Question 13 – Increase Salary

#* Create a dictionary named employees.

#^ {"Pravin": 30000, "Rahul": 35000, "Amit": 40000}

#* Create a new dictionary named updated_salary using Dictionary Comprehension.

#^ Increase every employee's salary by 5000.

#* Print the updated_salary.

#^ Expected Output:

#^ {'Pravin': 35000, 'Rahul': 40000, 'Amit': 45000}

# dic = {"Pravin": 30000, "Rahul": 35000, "Amit": 40000}
# print({i : dic[i] + 5000 for i in dic})



#& 🔴 Question 14 – Even Number Dictionary

#* Create a list named numbers.

#^ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#* Create a dictionary named even_squares using Dictionary Comprehension.

#^ Store only even numbers.

#^ Number → Key

#^ Square → Value

#* Print the even_squares.

#^ Expected Output:

#^ {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print({i : i*i for i in s if i % 2 == 0})



#& 🔴 Question 15 – Student Result System

#* Create a dictionary named students.

#^ {"Pravin": 85, "Rahul": 62, "Amit": 45, "Vijay": 78, "Karan": 35}

#* Create a new dictionary named results using Dictionary Comprehension.

#^ If marks are 50 or above → "Pass"

#^ Otherwise → "Fail"

#* Print the results.

#^ Expected Output:

#^ {'Pravin': 'Pass', 'Rahul': 'Pass', 'Amit': 'Fail', 'Vijay': 'Pass', 'Karan': 'Fail'}

dic = {"Pravin": 85, "Rahul": 62, "Amit": 45, "Vijay": 78, "Karan": 35}
print({i : "Pass" if dic[i] >= 50 else "Fail" for i in dic})