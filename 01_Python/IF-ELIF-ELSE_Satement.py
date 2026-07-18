 #! IF-ELIF-ELSE Statement Kya Hai?

#~ if-elif-else statement ka use tab hota hai jab hume 2 se zyada conditions check karni hoti hain aur unme se sirf ek condition ke hisaab se code execute karna hota hai.

#~ "Agar pehli condition True hai to uska code chalega. Agar nahi, to doosri condition check hogi. Agar wo bhi False hai, to teesri condition check hogi. Agar koi bhi condition True nahi hui, to else block execute hoga."


#! Syntax of IF-ELIF-ELSE Statement in Python:

#~ if condition1:
#~     # Executes if condition1 is True
#~     statement1

#~ elif condition2:
#~     # Executes if condition2 is True
#~     statement2

#~ elif condition3:
#~     # Executes if condition3 is True
#~     statement3

#~ else:
#~     # Executes if all conditions are False
#~     statement4

#^ Assignment

#* WAP to check whether the character is uppercase, lowercase, digit, or special character.

n = input('Enter the Character : ')

if 'A' <= n <= 'Z':
    print(f'{n} is a Upper Character')
elif 'a' <= n <= 'z':
    print(f'{n} is a Lower Character')
elif '0' <= n <= '9':
    print(f'{n} is a Digit')
else:
    print(f'{n} is a Special Character')



#* WAP to check whether the given integer is a single digit, two digits, three digits, or more than three digits.

n = int(input('Enter the number : '))

if  0 <= n <= 9:
    print(f'{n} is a Single Digit')
elif 9 < n <= 99:
    print(f'{n} is a Two Digit')
elif 99 < n <= 999:
    print(f'{n} is a Three Digit') 
else:
    print(f'{n} is a More than Three Digit')



#* WAP to check in which quadrant the given points are lying.

n = float(input('Enter the x coordinate : '))
m = float(input('Enter the y coordinate : '))

if n > 0 and m > 0:
    print(f'The point ({n}, {m}) lies in the First quadrant')
elif n < 0 and m > 0:
    print(f'The point ({n}, {m}) lies in the Second quadrant')
elif n < 0 and m < 0:
    print(f'The point ({n}, {m}) lies in the Third quadrant')
elif n > 0 and m < 0:
    print(f'The point ({n}, {m}) lies in the Fourth quadrant')  
else:
    print(f'The point ({n}, {m}) lies on the Axis')



#* WAP to find the greatest of 3 numbers.

n = int(input('Enter the first number : '))
m = int(input('Enter the second number : '))
p = int(input('Enter the third number : '))

if n > m and n > p:
    print(f'{n} is a gretest number')
elif m > n and m > p:
    print(f'{m} is a greatest number')
elif p > n and p > m:
    print(f'{p} is a greatest number')
else:
    print(f'all three numbers are same')



#* WAP to find the smallest of 3 numbers.

n = int(input('Enter the first number : '))
m = int(input('Enter the second number : '))
p = int(input('Enter the third number : '))

if n < m and n < p:
    print(f'{n} is a smallest number')
elif m < n and m < p:
    print(f'{m} is a smallest number')
elif p < n and p < m:
    print(f'{p} is a smallest number')
else:
    print('all three numbers are same')



#* WAP to check the relation between two integer numbers.

n = int(input('Enter the first number : '))
m = int(input('Enter the second number : '))

if n > m:
    print(f'{n} is greater than {m}')
elif m > n:
    print(f'{m} is greater than {n}')
else:
    print('both two have the same value')



#* Consider a character input:
#* If it is uppercase, convert it into lowercase
#* If it is lowercase, convert it into uppercase
#* If it is a digit, print the remainder when it is divided by 3
#* Else if it is a special character, print its ASCII value

n = input('Enter the character : ')

if 'A' <= n <= 'Z':
    print(f'{n} is a lowercase of {chr(ord(n) + 32)}')
elif 'a' <= n <= 'z':
    print(f'{n} is a uppercase of {chr(ord(n) - 32)}')
elif '0' <= n <= '9':
    print(int(n)%3)
else:
    print(f'ASCII value of the {n} character is a {ord(n)}')



#* WAP to print:
#* "Fizz" if the given number is a multiple of 3
#* "Buzz" if the given number is a multiple of 5
#* "FizzBuzz" if the given number is a multiple of both 3 and 5

n = int(input('Enter the number : '))

if n % 3 == 0:
    print(f'{n} is a Fizz')
elif n % 5 == 0:
    print(f'{n} is a Buzz')
elif n % 3 == 0 and n % 5 == 0:
    print(f'{n} is a FizzBuzz')
else:
    print(f'{n} is not multiple of 3 or 5')



#* WAP to calculate the electricity bill based on the following conditions:
#* 0–100 units → ₹5 per unit
#* 101–200 units → ₹7 per unit
#* Above 200 units → ₹10 per unit

n = int(input('Enter the units : '))

if 0 <= n <= 100:
    print(f'₹5 per unit based on {n} is {n*5}')
elif 100 < n <= 200:
    print(f'₹7 per unit based on {n} is {n*7}')
else:
    print(f'₹10 per unit based on {n} is {n*10}')



#* WAP to display the grade of a student based on the following marks:
#* 90–100 → Grade A
#* 80–89 → Grade B
#* 70–79 → Grade C
#* 60–69 → Grade D
#* 35–59 → Grade E
#* Below 35 → Fail

n = int(input('Enter your marks :'))

if 90 <= n <= 100:
    print(f'Your marks is {n} and your grade is A')
elif 80 <= n <= 89:
    print(f'Your marks is {n} and your grade is B')
elif 70 <= n <= 79:
    print(f'Your marks is {n} and your grade is C')
elif 60 <= n <= 69:
    print(f'Your marks is {n} and your grade is D')
elif 35 <= n <= 59:
    print(f'Your marks is {n} and your grade is E')
else:
    print(f'Your marks is {n} and you are Fail')