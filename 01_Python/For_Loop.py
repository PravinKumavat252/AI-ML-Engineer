 #! What is a For Loop? 

#~ For loop ek control statement hai jo kisi block of code ko baar-baar execute karne ke liye use hota hai. 
#~ Ye ek sequence (jaise list, tuple, string, range, set, ya dictionary) ke har element par ek-ek karke iterate (chalna) karta hai.


#! Why do we use a For Loop? (For Loop kyu use karte hain?)

#& Hum for loop ka use isliye karte hain kyunki:

#~ Ek hi code ko baar-baar likhne ki zarurat nahi padti.
#~ Code chhota aur readable ban jata hai.
#~ Jab hume pata ho ki loop kitni baar chalega.
#~ Kisi list, string ya dusri sequence ke har element par kaam karna ho.


#! Syntax of For Loop (For Loop ka Syntax)

# for variable in sequence:
#     # block of code to be executed



#^ Assignment:

#* Print numbers from 1 to 10.

for i in range(1, 11):
    print(i)



#* Print numbers from 10 to 1.

for i in range(10, 0, -1):
    print(i)



#* Print all even numbers from 1 to 50.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)



#* Print all odd numbers from 1 to 50.

for i in range(1, 51):
    if i % 2 == 1:
        print(i)



#* Print the multiplication table of a given number.

n = int(input('Enter the number :'))

for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')



# Find the sum of numbers from 1 to N.

n = int(input('Enter the number : '))
sum = 0

for i in range(1, n+1):
    sum = sum + i

print(f'the sum of numbers from 1 to {n} is {sum}')



#* Find the product of numbers from 1 to N.

n = int(input('Enter the number : '))
product = 1

for i in range(1, n+1):
    product = product * i

print(f'the product of numbers from 1 to {n} is {product}')



#* Count from 100 to 1.

for i in range(100, 0, -1):
    print(i)



#* Print all multiples of 5 from 1 to 100.

for i in range(1, 101):
    if i % 5 == 0:
        print(i)



#* Print all multiples of 7 from 1 to 100.

for i in range(1, 101):
    if i % 7 == 0:
        print(i)



#* Print squares of numbers from 1 to 10.

for i in range(1, 11):
    print(i * i)



#* Print cubes of numbers from 1 to 10.

for i in range(1, 11):
    print(i ** 3)



#* Print numbers divisible by both 3 and 5 from 1 to 100.

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)



#* Count how many numbers are divisible by 4 from 1 to 100.

count = 0

for i in range(1, 101):
    if i % 4 == 0:
        count += 1

print(f'numbers are divisible by 4 from 1 to 100 is {count}')



#* Print the first N natural numbers.

n = int(input('Enter the number : '))

for i in range(1, n+1):
    print(i)



#* Print each character of a string.

s = input('Enter the string : ')

for i in s:
    print(i)



#* Count the total characters in a string.

s = input('Enter the string : ')
count = 0

for i in s:
    count += 1
 
print(f"the total characters in a '{s}' is {count}")



#* Count vowels in a string.

s = input('Enter the string : ')
count = 0

for i in s:
    if i in 'aeiouAEIOU':
        count += 1

print(f"Total vowels in a '{s}' is {count}")



#* Count consonants in a string.

s = input('Enter the string : ')
count = 0

for i in s:
    if i not in 'aeiouAEIOU':
        count += 1

print(f"Total consonants in a '{s}' is {count}")



#* Count digits in a string.

s = input("Enter a string: ")
count = 0

for i in s:
    count += 1

print(f"Count digits in a '{s}' is {count}")



#* Count uppercase letters.

s = input("Enter a string: ")
count = 0

for i in s:
    if 'A'<= i <= 'Z':
        count += 1

print(f"Count uppercase letters in '{s}' is {count}")



#* Count lowercase letters.

s = input("Enter a string: ")
count = 0

for i in s:
    if 'a'<= i <= 'z':
        count += 1

print(f"Count lowercase letters in '{s}' is {count}")



#* Reverse a string using a for loop.

s = input('Enter the string : ')
out = ''

for i in s:
    out = i + out

print(out)



#* Check whether a character exists in a string.

s = input('Enter the string : ')
check = input('Enter the character :')
count = 0

for i in s:
    if check == i:
        count += 1
    
if count > 0:
    print(f"'{check}' exists in a '{s}'")
else:
    print(f"'{check}' does not exist in a '{s}'")



#* Count how many times a character appears.

# s = input('Enter the string : ')
# check = input('Enter the character :')
# count = 0

# for i in s:
#     if check == i:
#         count += 1
    
# if count > 0:
#     print(f"{count} times a '{check}' appears in a '{s}'")
# else:
#     print(f"'{check}' does not appear in a '{s}'")



#* Print all elements of a list.

# lst = [10, 20, 30, 40, 50]

# for i in lst:
#     print(i)



# Find the sum of list elements.

# lst = [5, 10, 15, 20, 25]
# sum = 0

# for i in lst:
#     sum = sum + i

# print(f'the sum of list elements is {sum}')



#* Find the largest element.

# lst = [45, 12, 89, 23, 67]
# largest = lst[0]

# for i in lst:
#     if largest < i:
#         largest = i

# print(f'the largest element of the list is {largest}')



#* Find the smallest element.

# lst = [45, 12, 89, 23, 67]
# smallest = lst[0]

# for i in lst:
#     if smallest > i:
#         smallest = i

# print(f'the smallest element of the list is {smallest}')



#* Count even numbers in a list.

# lst = [2, 5, 8, 11, 14, 17, 20]
# count = 0

# for i in lst:
#     if i % 2 == 0:
#         count += 1

# print(f'Count even numbers in a list is {count}')



#* Count odd numbers in a list.

# lst = [2, 5, 8, 11, 14, 17, 20]
# count = 0

# for i in lst:
#     if i % 2 == 1:
#         count += 1

# print(f'Count odd numbers in a list is {count}')



#* Print elements at even indexes with index.

# lst = [100, 200, 300, 400, 500, 600]

# for i in range(len(lst)):
#     if i % 2 == 0:
#         print(f"Index {i}: {lst[i]}")



#* Print elements at odd indexes.

# lst = [100, 200, 300, 400, 500, 600]

# for i in range(len(lst)):
#     if i % 2 == 1:
#         print(f"Index {i}: {lst[i]} ")



#* Reverse a list using a for loop.

# lst = [1, 2, 3, 4, 5, 6]
# out = []

# for i in lst:
#     out = [i] + out

# print(f"Reversed list: {out}")



#* Count occurrences of a given number.

# lst = [5, 2, 7, 5, 9, 5, 1, 5]
# num = 5
# count = 0

# for i in lst:
#     if i == num:
#         count += 1

# print(f"The number {num} occurs {count} times in the list.")



# *
# **
# ***
# ****
# *****

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end =' ')
#     print(' ')



# *****
# ****
# ***
# **
# *

# for i in range(6, 0, -1):
#     for j in range(1, i):
#         print('*', end = ' ')
#     print(' ')



#* 1
#* 12
#* 123
#* 1234
#* 12345

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end = ' ')
#     print(' ')



#* A
#* AB
#* ABC
#* ABCD
#* ABCDE

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(chr(64+j), end = ' ')
#     print()



#* 1
#* 22
#* 333
#* 4444
#* 55555

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end = ' ')
#     print()



# *****
# *****
# *****
# *****
# *****

# for i in range(1, 6):
#     for j in range(1, 6):
#         print('*', end = ' ')
#     print()



#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, 6):
#     for j in range(5 - i):
#         print(' ', end = ' ')
#     for k in range(i):
#         print('*', end = ' ')
#     print()



# *****
#  ****
#   ***
#    **
#     *

# for i in range(5, 0, -1):
#     for j in range(5-i):
#         print(' ', end = ' ')
#     for k in range(i):
#         print('*', end = ' ')
#     print()



# *
# ***
# *****
# *******
# *********

# for i in range(1, 6):
#     for j in range(2 * i - 1):
#         print('*', end = ' ')
#     print()



#* 1
#* 2 3
#* 4 5 6
#* 7 8 9 10

# n = 1
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(n, end = ' ')
#         n += 1
#     print(' ')



#* Find the factorial of a number using a for loop.

# n = int(input('Enter the number : '))
# factorial = 1

# for i in range(1, n+1):
#     factorial *= i

# print(f'the factorial of a {n} using a for loop is {factorial}')



#* Check whether a number is prime.

# n = int(input('Enter the number : '))
# count = 0

# for i in range(2, n):
#     if n % i == 0:
#         count += 1

# if count > 0:
#     print(f'{n} is not a prime number')
# else:
#     print(f'{n} is a prime number')



#* Print all prime numbers between 1 and N.

# n = int(input('Enter the number : '))

# for i in range(2, n+1):
#     count = 0
#     for j in range(2, i):
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         print(i)
    


#* Check whether a number is a perfect number.

# n = int(input('Enter the number : '))
# sum = 0

# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i

# if sum == n:
#     print(f'{n} is a perfect number')
# else:
#     print(f'{n} is not a perfect number')



#* Print the Fibonacci series up to N terms using a for loop.

# n = int(input('Enter the number of terms: '))
# a, b = 0, 1

# for i in range(1, n+1):
#     print(a)
#     c = a + b
#     a, b = b, c


#* Print unique elements in a list using a for loop.

# lst = [10, 20, 10, 30, 40, 20, 50, 60, 30, 70, 80, 50, 90, 100, 10]
# out = []

# for i in lst:
#     if i not in out:
#         out.append(i)

# print(out)



#* Check whether a string is a palindrome.

# n = input('Enter the string : ')
# out = ''
# for i in n:
#     out = i + out

# if out == n:
#     print(f'{out} is a palindrome string')
# else:
#     print(f'{out} is not a palindrome string')



#* Find the frequency of every character in a string.

# n = input('Enter the string : ')
# out = {}

# for i in n:
#     if i in out:
#         out[i] += 1
#     else:
#         out[i] = 1

# print(out)



#* Remove duplicate elements from a list using a for loop.

# lst = [10, 20, 30, 20, 40, 10, 50, 30]
# out = []

# for i in lst:
#     if i not in out:
#         out.append(i)

# print(out)



#* Find the second largest element in a list.

# lst = [15, 45, 22, 89, 67, 89, 12, 99]
# largest = 0
# second_largest = 0

# for i in lst:
#     if i > largest:
#         largest, second_largest = i, largest
#     elif (i < largest) and (i > second_largest):
#         second_largest = i

# print(f'{second_largest} element in a list')



#* Merge two lists using a for loop.

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]

# for i in b:
#     if i not in a:
#         a.append(i)

# print(a)



#* Find common elements between two lists.

# a = [10, 20, 30, 40, 50]
# b = [40, 50, 60, 70, 80]
# out = []

# for i in a:
#     if i in b:
#         out.append(i)

# print(out)



#* Print all Armstrong numbers between 1 and N.

# n = int(input('Enter the number : '))



#* Print all Armstrong numbers between 1 and N.

# n = int(input('Enter the number : '))

# for i in range(1, n+1):
#     power = len(str(i))
#     sum = 0

#     for j in str(i):
#         digit = int(j)
#         sum = sum + (digit ** power)

#     if sum == i:
#         print(f'{sum} is a Armstrong number')



#* Generate the first N Armstrong numbers.

# n = int(input('Enter the number of Armstrong numbers to generate: '))
# count = 0

# for i in range(1, 100000000):
#     power = len(str(i))
#     sum = 0

#     for j in str(i):
#         digit = int(j)
#         sum = sum + (digit ** power)

#     if sum == i:
#         print(f'{sum} is a Armstrong number')
#         count += 1

#     if count == n:
#         break


#* Print all keys of a dictionary.

# d = {'name': 'Pravin', 'age': 22, 'city': 'Ahmedabad'}

# for i in d:
#     print(i)



#* Print all values of a dictionary.

# d = {'name': 'Pravin', 'age': 22, 'city': 'Ahmedabad'}

# for i in d:
#     print(d[i])



#* Print all key-value pairs.

# d = {'name': 'Pravin', 'age': 22, 'city': 'Ahmedabad'}

# for i in d:
#     print(f'{i} : {d[i]}')



#* Count the total number of key-value pairs in a dictionary.

# d = {'name': 'Pravin', 'age': 22, 'city': 'Ahmedabad'}
# count = 0
# for i in d:
#     count += 1

# print(f"the total number of key-value pairs in a dictionary is {count}")

#* Check whether a given key exists in a dictionary.

# d = {'name': 'Pravin', 'age': 22, 'city': 'Ahmedabad'}
# key = input('Enter the key : ')

# if key in d:
#     print(f'{key} exists in the dictionary')
# else:
#     print(f'{key} does not exist in the dictionary')



#* Find the sum of all values in a dictionary.

# d = {'Math': 80, 'Science': 75, 'English': 90}
# sum = 0

# for i in d:
#     sum = sum + d[i]

# print(f'the sum of all values in a dictionary is {sum}')



#* Find the maximum value in a dictionary.

# d = {'A': 45, 'B': 90, 'C': 78, 'D': 65}
# max = 0

# for i in d:
#     if d[i] > max:
#         max = d[i]

# print(f'the maximum value in a dictionary is {max}')



#* Find the minimum value in a dictionary.

# d = {'A': 45, 'B': 90, 'C': 78, 'D': 65}
# min = 100

# for i in d:
#     if d[i] < min:
#         min = d[i]

# print(f'the minimum value in a dictionary is {min}')



#* Count how many values are even and how many are odd.

# d = {'a': 10, 'b': 15, 'c': 22, 'd': 31, 'e': 40}
# count_e = 0
# count_o = 0

# for i in d:
#     if d[i] % 2 == 0:
#         count_e += 1
#     else:
#         count_o += 1

# print(f"The even value is {count_e} and odd value is {count_o}")



#* Print only those key-value pairs where the value is greater than 50.

# d = {'A': 40, 'B': 55, 'C': 70, 'D': 25}
# out = {}

# for i in d:
#     if d[i] > 50:
#         out[i] = d[i]

# print(out)


#* Create a new dictionary where every value is squared.

# d = {'a': 2, 'b': 3, 'c': 4}
# out = {}

# for i in d:
#     out[i] = d[i] * d[i]

# print(out)



#* Print all keys whose values are even.

# d = {'Math': 80, 'Science': 75, 'English': 90, 'Hindi': 61}

# for i in d:
#     if d[i] % 2 == 0:
#         print(i)



#* Reverse the dictionary (swap keys and values).

# d = {'a': 10, 'b': 20, 'c': 30}
# out = {}

# for i in d:
#     out[d[i]] = i

# print(out)



#* Remove all key-value pairs whose value is less than 30.

# d = {'A': 10, 'B': 35, 'C': 25, 'D': 60}
# out = {}

# for i in d:
#     if d[i] < 30:
#         out[i] = d[i]

# print(out)



#* Find the key having the highest value.

# d = {'Ram': 85, 'Shyam': 92, 'Mohan': 78}
# highest = 0

# for i in d:
#     print(d[i])
#     if d[i] > highest:
#         highest = d[i]

# print(f"the key having the highest value is {highest}")


#* Count the frequency of each character in a string using a dictionary.

# n = input('Enter the string : ')
# d = {}

# for i in n:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# print(d)



#* Count the frequency of each element in a list using a dictionary.

# lst = [10, 20, 10, 30, 20, 10, 40, 30, 20]
# d = {}

# for i in lst:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# print(d)



#* Merge two dictionaries (if the same key exists, add their values).

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 5, 'c': 15, 'd': 25}

# for i in d1:
#     if i in d2:
#         d1[i] += d2[i]
#     else:
#         d1[i] = d1[i]

# for i in d2:
#     if i not in d1:
#         d1[i] = d2[i]
#     else:
#         d1[i] = d1[i]

# print(d1)



#* Find duplicate values in a dictionary.

# d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

# for i in d:
#     for j in d:
#         if i != j and d[i] == d[j]:
#             if i < j:  
#                 print(f"Duplicate value: {d[i]} for keys '{i}' and '{j}'")



#* Create a dictionary from two lists (one list contains keys and the other contains values) using a for loop.

# lst1 = ['name', 'age', 'city']
# lst2 = ['Pravin', 22, 'Ahmedabad']
# d = {}

# for i in range(len(lst1)):
#     d[lst1[i]] = lst2[i]

# print(d)



#* Write a Python program to take the details of N employees from the user.

n = int(input("Enter the number of employees: "))
out = {}

for i in range(1, n+1):
    key = input('Enter the department : ')
    value = input('Enter the name : ')

    if key not in out:
        out[key] = [value]
    else:
        out[key].append(value)

print(out)
