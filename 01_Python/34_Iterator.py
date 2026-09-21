
#! ==========================================
#! ITERATORS IN PYTHON
#! ==========================================


#? What is an Iterator?

#~ Iterator ek aisa object hai jo
#~ collection ke elements ko
#~ one by one access karta hai.

#~ Simple Line:

#~ Iterator → Elements ko one by one
#~ access karne wala object.


#& ----------------------------------------
#& Real Life Example
#& ----------------------------------------

#~ Socho tumhare paas ek book hai.

#~ Book mein multiple pages hain.

#~ Tum ek saath saare pages nahi padhte.

#~ Page 1 → Page 2 → Page 3 → Page 4

#~ Ek-ek page ko sequence mein read karte ho.

#~ Iterator bhi collection ke elements ko
#~ ek-ek karke access karta hai.


#& ----------------------------------------
#& Why do we use Iterator?
#& ----------------------------------------

#~ Iterator ka use:

#^ 1. Elements ko one by one access karne ke liye.

#^ 2. Large data ko efficiently process karne ke liye.

#^ 3. Memory ko efficiently use karne ke liye.

#^ 4. Sequential data processing ke liye.


#& ----------------------------------------
#& Iterable vs Iterator
#& ----------------------------------------


#? Iterable

#~ Iterable wo object hai jiske elements
#~ ko one by one iterate kiya ja sakta hai.

#^ Examples:

#~ list
#~ tuple
#~ string
#~ set
#~ dictionary


#? Iterator

#~ Iterator wo object hai jo
#~ elements ko one by one
#~ return karta hai.


#~ Simple Difference:

#^ Iterable
#~ → Jiske upar iteration kar sakte hain.


#^ Iterator
#~ → Jo elements ko one by one return karta hai.


#& ----------------------------------------
#& iter()
#& ----------------------------------------

#~ Kisi iterable ko iterator mein
#~ convert karne ke liye
#~ `iter()` function use karte hain.


#^ Syntax:

#* iterator = iter(iterable)


#& Example

#* numbers = [10, 20, 30]

#* iterator = iter(numbers)

#~ Ab `iterator` ek iterator object hai.


#& ----------------------------------------
#& next()
#& ----------------------------------------

#~ Iterator ke next element ko
#~ access karne ke liye
#~ `next()` function use hota hai.


#^ Syntax:

#* next(iterator)


#& Example

#* numbers = [10, 20, 30]

#* iterator = iter(numbers)

#* print(next(iterator))

#* print(next(iterator))

#* print(next(iterator))


#^ Output:

#^ 10
#^ 20
#^ 30


#~ Har `next()` call par
#~ next element return hota hai.


#& ----------------------------------------
#& Iterator Working
#& ----------------------------------------

#* numbers = [10, 20, 30]

#* iterator = iter(numbers)


#~ First:

#* next(iterator)

#^ 10


#~ Second:

#* next(iterator)

#^ 20


#~ Third:

#* next(iterator)

#^ 30


#~ Iterator apni current position
#~ remember karta hai.


#& ----------------------------------------
#& StopIteration
#& ----------------------------------------

#~ Jab iterator ke saare elements
#~ complete ho jate hain aur hum
#~ dobara `next()` call karte hain,

#~ Python `StopIteration` exception
#~ raise karta hai.


#& Example

#* numbers = [10, 20]

#* iterator = iter(numbers)

#* print(next(iterator))

#* print(next(iterator))

#* print(next(iterator))


#^ Output:

#^ 10
#^ 20

#~ Uske baad:

#^ StopIteration


#& ----------------------------------------
#& Iterator with for Loop
#& ----------------------------------------

#~ `for` loop internally iterator ka
#~ use karta hai.


#* numbers = [10, 20, 30]

#* for i in numbers:
#*     print(i)


#~ Python internally approximately:

#^ iter()
#^   ↓
#^ next()
#^   ↓
#^ next()
#^   ↓
#^ next()
#^   ↓
#^ StopIteration


#~ Isliye hume normally
#~ `iter()` aur `next()` manually
#~ use karne ki zarurat nahi hoti.


#& ----------------------------------------
#& Creating Our Own Iterator
#& ----------------------------------------

#~ Python mein hum apna custom
#~ iterator bhi create kar sakte hain.


#~ Custom iterator banane ke liye
#~ class mein mainly:

#^ `__iter__()`

#^ `__next__()`

#~ methods use hote hain.


#& ----------------------------------------
#& __iter__()
#& ----------------------------------------

#~ `__iter__()` method iterator object
#~ return karta hai.


#^ Basic Syntax:

#* def __iter__(self):
#*     return self


#& ----------------------------------------
#& __next__()
#& ----------------------------------------

#~ `__next__()` method next value
#~ return karta hai.


#^ Basic Syntax:

#* def __next__(self):
#*     # return next value


#~ Jab values complete ho jayein,

#* raise StopIteration


#& ----------------------------------------
#& Custom Iterator Example
#& ----------------------------------------

#* class Numbers:

#*     def __init__(self):
#*         self.num = 1

#*     def __iter__(self):
#*         return self

#*     def __next__(self):

#*         if self.num <= 5:
#*             value = self.num
#*             self.num += 1
#*             return value

#*         else:
#*             raise StopIteration


#* numbers = Numbers()

#* for i in numbers:
#*     print(i)


#^ Output:

#^ 1
#^ 2
#^ 3
#^ 4
#^ 5


#& ----------------------------------------
#& Important Iterator Methods
#& ----------------------------------------

#^ iter()

#~ Iterable ko iterator mein convert karta hai.


#^ next()

#~ Iterator ka next element return karta hai.


#^ __iter__()

#~ Iterator object return karta hai.


#^ __next__()

#~ Next value return karta hai.


#^ StopIteration

#~ Iteration complete hone par
#~ iteration stop karta hai.


#& ----------------------------------------
#& Advantages of Iterator
#& ----------------------------------------

#~ ✔ One-by-one data processing

#~ ✔ Memory efficient

#~ ✔ Large data ke liye useful

#~ ✔ Sequential processing

#~ ✔ Custom iteration possible


#& ----------------------------------------
#& Important Points
#& ----------------------------------------

#~ ✔ List ek Iterable hai.

#~ ✔ `iter()` iterable ko iterator banata hai.

#~ ✔ `next()` next element deta hai.

#~ ✔ Iterator current position remember karta hai.

#~ ✔ Elements complete hone par
#~ `StopIteration` hota hai.

#~ ✔ `for` loop internally iterator
#~ ka use karta hai.


#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#^ Iterable

#~ Data jisko iterate kar sakte hain.


#^ iter()

#~ Iterable → Iterator


#^ next()

#~ Iterator → Next Value


#^ StopIteration

#~ No More Values


#& ----------------------------------------
#& Quick Revision
#& ----------------------------------------

#^ Iterable
#~ list, tuple, string, set, dictionary


#^ Iterator
#~ One-by-one values provide karta hai.


#^ iter()
#~ Iterator create karta hai.


#^ next()
#~ Next value deta hai.


#^ __iter__()
#~ Iterator return karta hai.


#^ __next__()
#~ Next value return karta hai.


#^ StopIteration
#~ Iteration end karta hai.


#& ==========================================
#& INTERVIEW DEFINITION
#& ==========================================

#? What is an Iterator?

#~ An Iterator is an object that allows
#~ us to access elements of an iterable
#~ one at a time using `next()`.


#? What is the difference between
#? Iterable and Iterator?

#~ Iterable → Jiske elements ko
#~ iterate kar sakte hain.

#~ Iterator → Jo elements ko
#~ one by one return karta hai.


#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#^ Iterable
#*      ↓
#^ iter()
#*      ↓
#^ Iterator
#*      ↓
#^ next()
#*      ↓
#^ Value
#*      ↓
#^ next()
#*      ↓
#^ Value
#*      ↓
#^ StopIteration


#? Assignment:


# #& 🔴 Question 1 – Create an Iterator

# #* Create a list:

# #^ [10, 20, 30, 40]

# #* Convert the list into an iterator
# #* using `iter()`.

# #* Print the iterator.

# #* Use `next()` to print all elements.

# # lst = [10, 20, 30, 40]

# # iterator = iter(lst)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))



# #& 🔴 Question 2 – next()

# #* Create a list:

# #^ ["Python", "Java", "SQL"]

# #* Create an iterator using `iter()`.

# #* Use `next()` three times.

# #* Print each value.

# #^ Expected Output:

# #^ Python
# #^ Java
# #^ SQL

# # lst = ["Python", "Java", "SQL"]

# # iterator = iter(lst)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))



# #& 🔴 Question 3 – Iterator Position

# #* Create a list:

# #^ [1, 2, 3, 4, 5]

# #* Create an iterator.

# #* Use `next()` two times.

# #* Print the returned values.

# #* Use `next()` again and print the result.

# # lst = [1, 2, 3, 4, 5]

# # iterator = iter(lst)
# # next(iterator)
# # next(iterator)
# # print(next(iterator))
# # next(iterator)
# # print(next(iterator))



# #& 🔴 Question 4 – Iterator with while Loop

# #* Create a list:

# #^ [10, 20, 30, 40, 50]

# #* Create an iterator using `iter()`.

# #* Use `next()` inside a `while` loop.

# #* Print every element.

# #~ Stop the iteration when
# #~ `StopIteration` occurs.

# lst = [10, 20, 30, 40, 50]

# iterator = iter(lst)

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break



# #& 🔴 Question 5 – Iterator with for Loop

# #* Create a list:

# #^ ["Pravin", "Rahul", "Amit", "Vijay"]

# #* Create an iterator.

# #* Use a `for` loop to print
# #* every element from the iterator.

# # lst = ["Pravin", "Rahul", "Amit", "Vijay"]

# # iterator = iter(lst)

# # for i in iterator:
# #     print(i)



# #& 🔴 Question 6 – Handle StopIteration

# #* Create a list:

# #^ [100, 200, 300]

# #* Create an iterator.

# #* Use `next()` four times.

# #* Handle `StopIteration`
# #* using `try-except`.

# #~ Print:

# #^ "Iteration Completed"

# #~ when the iterator has no
# #~ more values.

# # lst = [100, 200, 300]

# # try:
# #     iterator = iter(lst)
# #     next(iterator)
# #     next(iterator)
# #     next(iterator)
# #     next(iterator)

# # except StopIteration:
# #     print("Iteration Completed")



# #& 🔴 Question 7 – Custom Number Iterator

# #* Create a class named `Numbers`.

# #* Create:

# #^ `__iter__()`

# #^ `__next__()`

# #* Generate numbers from `1` to `5`.

# #* Use a `for` loop to print them.

# #^ Expected Output:

# #^ 1
# #^ 2
# #^ 3
# #^ 4
# #^ 5

# # class Numbers:

# #     def __init__(self):
# #         self.num = 1

# #     def __iter__(self):
# #         return self

# #     def __next__(self):
# #         if self.num <= 5:
# #             value = self.num
# #             self.num += 1
# #             return value

# #         else:
# #             raise StopIteration

# # n = Numbers()
# # for i in n:
# #     print(i)



# #& 🔴 Question 8 – Custom Even Number Iterator

# #* Create a class named `EvenNumbers`.

# #* Create:

# #^ `__iter__()`

# #^ `__next__()`

# #* Generate even numbers from
# #* `2` to `10`.

# #* Use a `for` loop to print them.

# #^ Expected Output:

# #^ 2
# #^ 4
# #^ 6
# #^ 8
# #^ 10

# class EvenNumbers:

#     def __init__(self):
#         self.num = 2

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.num <= 10:
#             value = self.num
#             self.num += 2
#             return value

#         else:
#             raise StopIteration

# e = EvenNumbers()
# for i in e:
#     print(i)



#& 🔴 Question 11 – Check Iterable

#* Create a list:

#^ [10, 20, 30, 40]

#* Use `iter()` to create an iterator.

#* Use `next()` to print the first value.

#* Use `next()` again to print the second value.

#* Print the remaining values using a `for` loop.

#^ Expected Output:

#^ 10
#^ 20
#^ 30
#^ 40

# lst = [10, 20, 30, 40]

# iterator = iter(lst)
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)



#& 🔴 Question 12 – String Iterable

#* Create a string:

#^ "Python"

#* Use `iter()` to create an iterator.

#* Use `next()` three times.

#* Print each returned character.

#^ Expected Output:

#^ P
#^ y
#^ t

#* Then use a `for` loop to print
#* the remaining characters.

# s = "Python"

# iterator = iter(s)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)



#& 🔴 Question 13 – Tuple Iterable

#* Create a tuple:

#^ (100, 200, 300, 400)

#* Convert the tuple into an iterator
#* using `iter()`.

#* Use `next()` two times.

#* Print both values.

#* Use a `for` loop to print
#* the remaining values.

#^ Expected Output:

#^ 100
#^ 200
#^ 300
#^ 400

# t = (100, 200, 300, 400)

# iterator = iter(t)
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)



#& 🔴 Question 14 – Dictionary Iterable

#* Create a dictionary:

#^ {"name": "Pravin", "age": 23, "course": "AI/ML"}

#* Create an iterator using `iter()`.

#* Use `next()` two times.

#* Print the returned values.

#* Use a `for` loop to print
#* the remaining key.

#^ Expected Output:

#^ name
#^ age
#^ course

dic = {"name": "Pravin", "age": 23, "course": "AI/ML"}

# iterator = iter(dic)
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)


#? Try to access both key and value

# iterator = iter(dic)
# key = next(iterator)
# print(key, dic[key])

# key = next(iterator)
# print(key, dic[key])

# for i in iterator:
#     print(i, dic[i])


#& 🔴 Question 15 – Iterable vs Iterator

#* Create a list:

#^ [1, 2, 3, 4, 5]

#* Store the list in a variable named `numbers`.

#* Create an iterator:

#^ iterator = iter(numbers)

#* Print:

#^ type(numbers)

#* Print:

#^ type(iterator)

#* Use `next()` two times.

#* Print both values.

#* Use a `for` loop to print
#* the remaining values.

#~ Understand the difference between:

#^ Iterable → `numbers`

#^ Iterator → `iterator`

# numbers = [1, 2, 3, 4, 5]

# iterator = iter(numbers)
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)

# print(type(numbers))
# print(type(iterator))