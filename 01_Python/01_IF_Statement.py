 #! IF Statement Kya Hai?

#~ IF statement Python ka ek decision-making statement hai.
#~ Jab hume kisi condition ko check karna hota hai aur condition True hone par hi code execute karna hota hai, tab hum if statement ka use karte hain.

#! Syntax of IF Statement in Python:

#~ if condition:
#~     # code to execute if condition is True

#^ Assignment

#* WAP to print the square of a number only if it is even.

n = int(input('Enter the number : '))
if n%2 == 0:
 print(n)



#* WAP to check whether the character is a vowel or not.

n = input('Enter the Character : ')
if n in 'aeiouAEIOU':
 print(f'{n} is a vowel character')



#* WAP to print the ASCII value of a character only if it is uppercase.

n = input('Enter the Character : ')
if 'A'<= n <= 'Z':
  print(ord(n))



#* WAP to print the cube of a number only if it is divisible by 9 or 6.

n = int(input('Enter the number : '))
if 9%n == 0 and 6%n == 0:
 print(n*n) 



#* WAP to check whether the given integer is a 3-digit number.

n = int(input('Enter the number : '))
if 99 < n < 1000:
 print(f'{n} is a three digit number')



#* WAP to check whether the last digit of a given number is 5.

n = int(input('Enter the number : '))
if n%10 == 5:
 print(f'{n} have last digit of a given number is 5')



#* WAP to check whether the given data is float.

n = eval(input('Enter the data : '))
if type(n) == float:
 print(f'{n} having float data type')



#* WAP to check whether the data is single value data.

n = eval(input('Enter the data : '))
if type(n) in (int, float, bool, complex):
 print(f'{n} having single value data type')



#* WAP to check whether the given character is a digit or not.

n = eval(input('Enter the data : '))
if 0 <= n <= 9:
 print(f'{n} is a digit')



#* WAP to check whether the given integer is a multiple of 3.

# n = int(input('Enter the integer number : '))
# if n%3 == 0:
#     print(f'{n} is a multiple of 3')
