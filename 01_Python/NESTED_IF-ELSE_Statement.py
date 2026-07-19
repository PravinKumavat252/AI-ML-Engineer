 #! Nested IF-ELSE Statement Kya Hai?

#~ Nested if-else ka matlab hai ek if ya else block ke andar ek aur if-else statement likhna.

#~ Jab ek condition True hone ke baad hume ek aur condition check karni hoti hai, tab hum nested if-else ka use karte hain.


#! Syntax of Nested IF-ELSE Statement in Python:

#~ if condition1:
#~     if condition2:
#~         # Executes if condition2 is True
#~     else:
#~         # Executes if condition2 is False
#~ else:
#~     if condition3:
#~         # Executes if condition3 is True
#~     else:
#~         # Executes if condition3 is False



#^ Assignment

#* WAP to login into Instagram with a valid username and password (enter password only if the username is valid).

username = input('Enter the username : ')
password = input('Enter the password : ')

user = 'rohit'
pas = '12345qwert'

if username == user:
    if password == pas:
        print('Instagram is loading...')
    else:
        print('password is wrong')
else:
    print('Invalid username')



#* WAP to print the middle value of a list only if it is a string.

l = [22,223,23,'xasxf','fwf', 33.4, 8+4j]

if len(l) % 2 == 1:
    char = len(l)//2
    if type(l[char]) == str:
        print(f'the middle value of a list is {l[char]}')
    else:
        print('the middle value of a list is not a string')
else:
    print('list not having muddle value')



#* WAP to check whether the character is a vowel or consonant.

n = input('Enter the character : ')

if 'a' <= n <= 'z' or 'A' <= n <= 'Z':
    if n in 'aeiouAEIOU':
        print(f'{n} is a vowel character')
    else:
        print(f'{n} is a consonant')
else:
    print(f'{n} is not a character')



#* WAP to find the greatest of 4 numbers.

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))
d = int(input('Enter the fourth number : '))

if a > b:
    if a > c:
        if a > d:
            print(f'{a} is a greatest')
        else:
            print(f'{d} is a greatest')
    else:
        if c > d:
            print(f'{c} is a greatest')
        else:
            print(f'{d} is a greatest')
else:
    if b > c:
        if b > d:
            print(f'{b} is a greatest')
        else:
            print(f'{d} is a greatest')
    else:
        if c > d:
            print(f'{c} is a greatest')
        else:
            print(f'{d} is a greatest')



#* WAP to print the value as it is only if the length of the value is even.

n = eval(input('Enter the value :'))

if type(n) == str:
    if len(n) % 2 == 1:
        print(f'{n} is a even length')
    else:
        print(f'{n} is not a even length')
else:
    print(f'{n} is not a string data type')



#* WAP to print the last value of a list only if it is a palindrome string starting with a vowel. 

l = ['madam', 'python', 'level', 'aba']

if l[-1] == l[-1][::-1]:
    if l[-1][0] in 'aeiouAEIOU':
        print(f'{l[-1]} is a palindrome string starting with a vowel.')
    else:
        print(f'{l[-1]} is a palindrome string but not starting with a vowel.')
else:
    print(f'{l[-1]} is not  a palindrome string.')



#* WAP to print the reversed string only if it is starting with a vowel, ending with a consonant, and having a middle value.

n = input('Enter the string : ')

if len(n) % 2 == 1:
    if n[0] in 'aeiouAEIOU':
        if n[-1] not in 'aeiouAEIOU':
            print(f'{n} reversed is {n[::-1]}')
        else:
            print(f'{n} ending with a consonant')
    else:
        print(f'{n} starting with a vowel')
else:
    print(f'{n} having a middle value')
    


#* WAP to find the second greatest of 4 values.

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))
d = int(input('Enter the fourth number : '))

if a > b:
    if a > c:
        if a > d:
            if b > c:
                if b > d:
                    print(f'{b} is a second greatest')
                else:
                    print(f'{d} is a second greatest')
            else:
                if c > d:
                    print(f'{c} is a second greatest')
                else:
                    print(f'{d} is a second greatest')
        else:
            if a > c:
                if a > b:
                    print(f'{a} is a second greatest')
                else:
                    print(f'{b} is a second greatest')
            else:
                if c > b:
                    print(f'{c} is a second greatest')
                else:
                    print(f'{b} is a second greatest')
    else:
        if c > d:
            if c > b:
                if c > a:
                    print(f'{c} is a second greatest')
                else:
                    print(f'{a} is a second greatest')
            else:
                if b > a:
                    print(f'{b} is a second greatest')
                else:
                    print(f'{a} is a second greatest')
        else:
            if d > b:
                if d > c:
                    print(f'{d} is a second greatest')
                else:
                    print(f'{c} is a second greatest')
            else:
                if b > c:
                    print(f'{b} is a second greatest')
                else:
                    print(f'{c} is a second greatest')



#* WAP to find the smallest of 4 numbers.

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))
d = int(input('Enter the fourth number : '))

if a < b:
    if a < c:
        if a < d:
            print(f'{a} is a smallest')
        else:
            print(f'{d} is a smallest')
    else:
        if c < d:
            print(f'{c} is a smallest')
        else:
            print(f'{d} is a smallest')
else:
    if b < c:
        if b < d:
            print(f'{b} is a smallest')
        else:
            print(f'{d} is a smallest')
    else:
        if c < d:
            print(f'{c} is a smallest')
        else:
            print(f'{d} is a smallest')


#* WAP to print the middle character of the given string only if it is an uppercase character.

s = "pyThon Is EASY "

if len(s) % 2 == 1:
    mid = len(s)//2
    if 'A' <= s[mid] <= 'Z':
        print(f'middle character of {s} is {s[mid]}')
    else:
        print(f'{s[mid]} not have middle character in uppercase')
else:
    print(f'{s} not have middle character')