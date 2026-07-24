 #! Loop Kya Hai?

#~ Loop ek programming concept hai jiska use ek hi code ko baar-baar execute (repeat) karne ke liye kiya jata hai jab tak di hui condition True rahe.



#! Loop Ka Use Kyu Karte Hai?

#~ Loop ka use tab karte hai jab hume same kaam baar-baar karna ho.
#~ Agar loop use nahi karenge to hume same code ko baar-baar likhna padega.



#! Loop ke Benefits :-

#~ Code chhota hota hai.
#~ Time bachata hai.
#~ Repeated work automatically hota hai.
#~ Code readable hota hai.



#! While Loop Kya Hai

#~ While Loop ek aisa loop hai jo jab tak condition True hoti hai tab tak code ko baar-baar execute karta hai.
#~ Jaise hi condition False hoti hai, loop stop ho jata hai.



#! Syntax of While Loop in Python:

# initialization (mandatory)

# while condition:
#     # Loop Body
#     statement(s)

#     updation (mandatory)


#^ Assignment

#* Print numbers from 1 to 10.

i = 1

while i <= 10:
    print(i)
    i += 1



#* Print numbers from 10 to 1.

i = 10

while i > 0:
    print(i)
    i -= 1



#* Print all even numbers from 1 to 50.

i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1



#* Print all odd numbers from 1 to 50.

i = 1

while i <= 50:
    if i % 2 == 1:
        print(i)
    i += 1



#* Print the multiplication table of a given number.

n = int(input('Enter the number : '))
i = 1

while i <= 10:
    print(f'{n} * {i} = {n*i}')
    i += 1 



#* Print numbers from 1 to N.

n = int(input('Enter the number : '))
i = 1

while i <= n:
    print(i)
    i += 1



#* Print numbers from N to 1.

n = int(input('Enter the number : '))

while n >= 1:
    print(n)
    n -= 1



#* Print the first 20 natural numbers.

i = 1

while i <= 20:
    print(i)
    i += 1



#* Print the first 20 even numbers.

i = 1

while i <= 40:
    if i % 2 == 0:
        print(i)
    i += 1



#* Print the first 20 odd numbers.

i = 1

while i <= 40:
    if i % 2 == 1:
        print(i)
    i += 1



#* Find the sum of numbers from 1 to N.

n = int(input('Enter the number : '))
sum = 0

while 1 <= n:
    sum = n + sum
    n -=  1

print(sum)



#* Find the sum of even numbers from 1 to N.

n = int(input('Enter the number : '))
sum = 0

while n >= 1:
    if n % 2 == 0:
        sum = n + sum
    n -= 1

print(sum) 



#* Find the sum of odd numbers from 1 to N.

n = int(input('Enter the number : '))
sum = 0

while n >= 1:
    if  n % 2 == 1:
        sum = n + sum
    n -= 1

print(sum)


#* Find the product of numbers from 1 to N.

n = int(input('Enter the number : '))
product = 1

while n >= 1:
    product = n * product
    n -= 1

print(product)



#* Find the factorial of a given number.

n = int(input('Enter the number : '))
fact = 1

while n >= 1:
    fact = n * fact
    n -= 1

print(fact)



#* Count how many numbers are printed from 1 to N.

n = int(input('Enter the number : '))
count = 0

while n >= 1:
    count = count + 1
    print(count)
    n -= 1

print(f"The count of numbers from 1 to N is: {count}")



#* Take 10 numbers from the user and find their sum.

sum = 0
i = 1

while i <= 10:
    n = int(input('Enter the number : '))
    sum += n
    i += 1

print(f"The sum of the numbers is: {sum}")



#* Take 5 numbers from the user and find their average.

sum = 0
count = 0
i = 1

while i <= 5:
    n = int(input('Enter the numer : '))
    sum = n + sum
    count = count + 1
    i += 1

print(f"The average of the numbers is: {sum/count}")



#* Count positive and negative numbers from user input (stop when user enters 0).

count_p = 0
count_n = 0
n = 1

while n > 0 or n < 0:
    n = int(input('Enter the number : '))
    if n > 0:
        count_p = count_p + 1
    elif n < 0:
        count_n = count_n + 1

print(f'Count positive numbers from user input is {count_p}')
print(f'Count negative numbers from user input is {count_n}')



#* Find the largest number from 10 user inputs.

largest = 0
i = 1

while i <= 10:
    n = int(input('Enter the number : '))
    if n > largest:
        largest = n
    i += 1

print(f'the largest number from 10 user inputs is {largest}')



#* Count the digits of a number.

count = 0
i = int(input('Enter the number : '))

if i == 0:
    count = 1
else:
    while i > 0:
        i = i // 10
        count = count + 1

    print(f'Count the digits of a number is {count}')



#* Find the sum of digits.

i = int(input('Enter the number : '))
sum = 0

while i > 0:
    add = i % 10
    sum = sum + add
    i = i // 10

print(f'the sum of digits is {sum}')



#* Find the product of digits.

i = int(input('Enter the number : '))
product = 1

while i > 0:
    digit = i % 10
    product = product * digit
    i = i // 10

print(f'the product of digits is {product}')



#* Reverse a number.

i = int(input('Enter the number : '))
t = i
revers = 0

while i > 0:
    digit = i % 10
    revers = (revers * 10) + digit 
    i = i // 10

print(f'{t} reverse number is {revers}') 



# Check whether a number is a palindrome.

i = int(input('Enter the number : '))
t = i
num = 0

while i > 0:
    digit = i % 10
    num = (num * 10) + digit
    i = i // 10

if t == num:
    print(f'{num} is a palindrome number')
else:
    print(f'{num} is not a palindrome number')



#* Find the largest digit.

i = int(input('Enter the number : '))
largest = 0

while i > 0:
    digit = i % 10
    if digit > largest:
        largest = digit
    i = i // 10

print(f'the largest digit is {largest}')



#* Find the smallest digit.

i = int(input('Enter the number : '))
smallest = 9

while i > 0:
    digit = i % 10
    if digit < smallest:
        smallest = digit
    i = i // 10

print(f'the smallest digit is {smallest}')



#* Print each digit separately.

i = int(input('Enter the number : '))

while i > 0:
    digit = i % 10
    print(digit)
    i = i // 10



#* Count the frequency of a given digit.

i = int(input('Enter the number : '))
t = int(input('Enter the digit : '))
count = 0

while i > 0:
    digit = i % 10
    if digit == t:
        count = count + 1
    i = i // 10

print(f'the frequency of a {t} digit is {count}')



#* Check whether a number is an Armstrong number.

i = int(input('Enter the number : '))
t = i
sum = 0

while i > 0:
    digit = i % 10
    sum = sum + (digit ** 3)
    i = i // 10

if sum == t:
    print(f'{sum} is a Armstrong number')
else:
    print(f'{sum} is not a Armstrong number')



#* Check whether a number is prime.

i = int(input('Enter the number : '))
t = i - 1
count = 0

while t > 1:
    if i % t == 0:
        count += 1
    t -= 1

if count == 0:
    print(f'{i} is a prime number')
else:
    print(f'{i} is not a prime number')



#* Print all prime numbers between 1 and N.

n = int(input('Enter the number : '))
i = 1
count = 0

while i < n:
    m = i - 1

    while m > 1:
        if i % m == 0:
            count += 1
        m -= 1

    if count == 0:
        print(i)
    i += 1



#* Print Fibonacci series up to N terms.

n = int(input('Enter the number : '))
i = 1
a = 0
b = 1

while i <= n:
    print(a)
    c = a + b
    a, b = b, c
    i += 1



#* Find the GCD (HCF) of two numbers.

n = int(input('Enter the number : '))
i = int(input('Enter the number : '))
m =2

if i > n:
    t = n
else:
    t = i

while m <= t:
    if (n % m == 0) and (i % m == 0):
        gcd = m
    m += 1

print(f'the GCD (HCF) of two numbers is {gcd}')



#* Find the LCM of two numbers.

n = int(input('Enter the number : '))
i = int(input('Enter the number : '))
m = 2

if i > n:
    t = n
else:
    t = i

while t >= m:
    if (n % m == 0) and (i % m == 0):
        lcm = m
    t -= 1

print(f'the LCM of two numbers is {lcm}')



#* Check whether a number is a perfect number.

i = int(input('Enter the number : '))    
t = i - 1
sum = 0

while t > 0:
    if i % t == 0:
        sum = sum + t
    t -= 1

if sum == i:
    print(f'{sum} is a perfect number')
else:
    print(f'{sum} is not a perfect number')



#* Check whether a number is a strong number.

i = int(input('Enter the number : '))
t = i
strong = 0

while i > 0:
    digit = i % 10
    fact = 1
    temp = digit

    while temp > 0:
        fact = fact * temp
        temp = temp - 1
    strong = strong + fact
    i = i // 10

if strong == t:
    print(f'{strong} is a strong number')
else:
    print(f'{strong} is not a strong number')



#* Check whether a number is a neon number.

i = int(input('Enter the number : '))
t = i
square = i * i
sum = 0

while square > 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10

if sum == t:
    print(f'{sum} is a neon number')
else:
    print(f'{sum} is not a neon number')



#* Find the sum of factorials of digits.

num = int(input('Enter the number : '))
original = num
total_sum = 0

while num > 0:
    digit = num % 10          
    fact = 1              
    temp = digit

    while temp > 0:
        fact = fact * temp
        temp = temp - 1
    total_sum = total_sum + fact   
    num = num // 10   

print(f'Sum of factorials of digits of {original} = {total_sum}')



#* Check whether a number is a spy number.

num = int(input('Enter the number : '))
original = num

sum_digits = 0
product_digits = 1   

while num > 0:
    digit = num % 10          
    sum_digits = sum_digits + digit
    product_digits = product_digits * digit
    num = num // 10           

if original == 0:
    sum_digits = 0
    product_digits = 0

if sum_digits == product_digits:
    print(f'{original} is a Spy Number!')
else:
    print(f'{original} is not a Spy Number.')    