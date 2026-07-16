 #! IF-ELSE Statement Kya Hai?

#~ IF statement Python ka ek decision-making statement hai.
#~ if-else statement ka use tab hota hai jab hume do conditions (True aur False) ke liye alag-alag code execute karna hota hai.

#! Syntax of IF-ELSE Statement in Python:

#~ if condition:
#~     # code to execute if condition is True
#~ else:
#~     # code to execute if condition is False

#^ Assignment

#* WAP to check whether the data is mutable or not.

n = eval(input('Enter the data : '))
if type(n) in [list, set, dict]:
    print(f'{n} is a mutable data type')
else:
    print(f'{n} is a immutable data type')



#* WAP to check whether the given character is a digit or not.

n = eval(input('Enter the digit : '))
if 0 <= n <= 9:
    print(f'{n} is a digit')
else:
    print(f'{n} is a not digit')



#* WAP to check whether the given character is special or not.

n = input('Enter the special character : ')
if n in '!@#$%^&*()_-? ':
    print(f'{n} is a special character')
else:
    print(f'{n} is a not special character')



#* WAP to check whether a list consists of a middle value or not.

n = eval(input('Enter the list : '))
if len(n)%2 == 1:
    print(f'{n} having middle value')
else:
    print(f'{n} not having middle value')



#* WAP to check whether the number is even or odd.

n = int(input('Enter the number : '))
if n%2 == 1:
    print(f'{n} is a odd')
else:
    print(f'{n} is a even')



#* WAP to check whether the given data is mutable or immutable.

n = eval(input('Enter the data : '))
if type(n) in [set, list, dict]:
    print(f'{n} is a mutable data type')
else:
    print(f'{n} is a immutable data type')



#*  WAP to check whether two values are pointing to the same memory or not.

n = int(input('Enter the number of n : '))
m = int(input('Enter the number of m : '))

if id(n) == id(m):
    print(f'{n} and {m} is pointing to the same memory')
else:
     print(f'{n} and {m} is not pointing to the same memory')



#* Consider a tuple of length 2 and check whether the tuple is homogeneous or not.

n = eval(input('Enter the tuple : '))
if type(n) == tuple and len(n) == 2 and type(n[0]) == type(n[1]):
    print(f'tuple of length 2 and the tuple is homogeneous')
else:
    print('a tuple of length 2 and  is not homogeneous')



#* WAP to check whether the string is a palindrome or not.

n = input('Ente the string : ')
if n == n[::-1]:
    print(f'{n} is a palindrome string')
else:
    print(f'{n} is not  a palindrome string')



#* WAP to check whether the number is positive or negative.

n = int(input('Enter the number : '))
if n >= 0:
    print(f'{n} is a positive number')
else:
    print(f'{n} is a negative number')