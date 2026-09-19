
#! ==========================================
#! FILE READING METHODS
#! ==========================================


#? What are File Reading Methods?

#~ Python mein file ke andar ka data
#~ read karne ke liye different methods
#~ available hain.

#~ Main reading methods:

#^ 1. read()
#^ 2. readline()
#^ 3. readlines()


#& ----------------------------------------
#& 1. read()
#& ----------------------------------------

#~ `read()` method file ka
#~ complete content read karta hai.

#^ Syntax:

#* file.read()


#& Example

#* file = open("student.txt", "r")

#* data = file.read()

#* print(data)

#* file.close()


#~ Agar file mein:

#^ Pravin
#^ Rahul
#^ Amit

#~ hai, to `read()`:

#^ Pravin
#^ Rahul
#^ Amit

#~ complete content return karega.


#& ----------------------------------------
#& read() with Number
#& ----------------------------------------

#~ `read()` ke andar number bhi
#~ provide kar sakte hain.

#^ Syntax:

#* file.read(n)


#~ `n` batata hai ki kitne
#~ characters read karne hain.


#& Example

#* file = open("student.txt", "r")

#* data = file.read(5)

#* print(data)

#* file.close()


#~ Agar file mein:

#^ "Python Programming"

#~ hai, to:

#^ read(5)

#~ first 5 characters read karega.

#^ Output:

#^ Pytho


#& ----------------------------------------
#& 2. readline()
#& ----------------------------------------

#~ `readline()` method file se
#~ ek time par ek line read karta hai.

#^ Syntax:

#* file.readline()


#& Example

#* file = open("student.txt", "r")

#* data = file.readline()

#* print(data)

#* file.close()


#~ Agar file mein:

#^ Pravin
#^ Rahul
#^ Amit

#~ hai.

#~ First `readline()`:

#^ Pravin


#~ Second `readline()`:

#^ Rahul


#~ Third `readline()`:

#^ Amit


#& ----------------------------------------
#& Multiple readline()
#& ----------------------------------------

#* file = open("student.txt", "r")

#* print(file.readline())

#* print(file.readline())

#* print(file.readline())

#* file.close()


#~ Har `readline()` call
#~ next line par move karta hai.


#& ----------------------------------------
#& 3. readlines()
#& ----------------------------------------

#~ `readlines()` method file ki
#~ all lines ko read karke
#~ ek list return karta hai.

#^ Syntax:

#* file.readlines()


#& Example

#* file = open("student.txt", "r")

#* data = file.readlines()

#* print(data)

#* file.close()


#~ Agar file mein:

#^ Pravin
#^ Rahul
#^ Amit

#~ hai.

#~ Output:

#^ ['Pravin\n', 'Rahul\n', 'Amit']


#~ Yahan `\n` ka matlab hai
#~ New Line.


#& ----------------------------------------
#& read() vs readline() vs readlines()
#& ----------------------------------------

#^ read()

#~ Complete file ka content
#~ ek saath read karta hai.

#^ Return:

#~ String


#^ readline()

#~ Ek time par ek line
#~ read karta hai.

#^ Return:

#~ String


#^ readlines()

#~ All lines ko read karke
#~ list mein return karta hai.

#^ Return:

#~ List


#& ----------------------------------------
#& Text Table
#& ----------------------------------------

#^ Method       Purpose                    Return Type
#* ---------------------------------------------------
#~ read()       Complete content           String
#~ readline()   One line                   String
#~ readlines()  All lines                  List


#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#~ Naam se hi yaad rakho:

#^ read()
#~ → Read everything


#^ readline()
#~ → Read one line


#^ readlines()
#~ → Read all lines


#& ----------------------------------------
#& Important Difference
#& ----------------------------------------

#^ `read()`

#~ File ko complete read karta hai.


#^ `readline()`

#~ One line at a time read karta hai.


#^ `readlines()`

#~ Multiple/all lines ko
#~ list ke form mein return karta hai.


#& ----------------------------------------
#& File Cursor
#& ----------------------------------------

#~ File read karte time Python ek
#~ **file cursor** maintain karta hai.

#~ Cursor batata hai ki file mein
#~ abhi hum kis position par hain.


#? Example:

#* file = open("student.txt", "r")

#* print(file.readline())

#* print(file.readline())

#* file.close()


#~ First `readline()`:

#^ First line


#~ Second `readline()`:

#^ Second line


#~ Kyunki cursor first line ke baad
#~ automatically next line par move ho gaya.


#& ----------------------------------------
#& tell() Method
#& ----------------------------------------

#~ `tell()` method current cursor
#~ position batata hai.

#^ Syntax:

#* file.tell()


#& Example

#* file = open("student.txt", "r")

#* print(file.tell())

#* file.read(5)

#* print(file.tell())

#* file.close()


#~ Starting position:

#^ 0


#~ 5 characters read karne ke baad:

#^ Position → 5


#& ----------------------------------------
#& seek() Method
#& ----------------------------------------

#~ `seek()` method cursor ko
#~ kisi specific position par
#~ move karta hai.

#^ Syntax:

#* file.seek(position)


#& Example

#* file = open("student.txt", "r")

#* file.read(5)

#* file.seek(0)

#* print(file.read())

#* file.close()


#~ `seek(0)` cursor ko
#~ file ke beginning par le jata hai.


#& ----------------------------------------
#& read() + seek()
#& ----------------------------------------

#* file = open("student.txt", "r")

#* print(file.read(5))

#* file.seek(0)

#* print(file.read())

#* file.close()


#~ First `read(5)`:

#^ First 5 characters


#~ `seek(0)`:

#^ Cursor → Beginning


#~ Second `read()`:

#^ Complete file


#& ----------------------------------------
#& Important Points
#& ----------------------------------------

#~ ✔ `read()` → Complete content

#~ ✔ `read(n)` → n characters

#~ ✔ `readline()` → One line

#~ ✔ `readlines()` → All lines as list

#~ ✔ `tell()` → Current cursor position

#~ ✔ `seek()` → Cursor position change


#& ----------------------------------------
#& Quick Revision
#& ----------------------------------------

#^ read()

#~ File → String


#^ readline()

#~ One Line → String


#^ readlines()

#~ All Lines → List


#^ tell()

#~ Current Cursor Position


#^ seek()

#~ Move Cursor


#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#~ File Reading Methods:

#^ read()       → Complete file
#^ readline()   → One line
#^ readlines()  → All lines
#^ tell()       → Cursor position
#^ seek()       → Move cursor


#? Assignment:


#& 🔴 Question 1 – Read Complete File

#* Create a file named `student.txt`.

#* Write:

#^ "My name is Pravin."

#* Open the file in Read mode.

#* Use `read()` to read the complete content.

#* Print the content.

#* Close the file.

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()


#& 🔴 Question 2 – Read Student Details

#* Create a file named `student.txt`.

#* Write:

#^ "Name: Pravin"
#^ "Course: MSc AI/ML"
#^ "Marks: 85"

#* Open the file in Read mode.

#* Use `read()` to read the complete content.

#* Print the content.

#* Close the file.

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()



#& 🔴 Question 3 – Read Specific Characters

#* Create a file named `message.txt`.

#* Write:

#^ "Python Programming"

#* Open the file in Read mode.

#* Use `read(6)`.

#* Print the result.

#^ Expected Output:

#^ Python

# file = open("message.txt", "r")
# data = file.read(6)
# print(data)
# file.close()



#& 🔴 Question 4 – Read First Line

#* Create a file named `students.txt`.

#* Write:

#^ "Pravin"
#^ "Rahul"
#^ "Amit"

#* Open the file in Read mode.

#* Use `readline()`.

#* Print the result.

#^ Expected Output:

#^ Pravin

# file = open("student.txt", "r")
# data = file.readline()
# print(data)
# file.close()



#& 🔴 Question 5 – Read Multiple Lines

#* Create a file named `students.txt`.

#* Write:

#^ "Pravin"
#^ "Rahul"
#^ "Amit"

#* Open the file in Read mode.

#* Use `readline()` three times.

#* Print each line.

# file = open("student.txt", "r")
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# file.close()



#& 🔴 Question 6 – Read First Two Lines

#* Create a file named `students.txt`.

#* Write:

#^ "Pravin"
#^ "Rahul"
#^ "Amit"
#^ "Vijay"

#* Open the file in Read mode.

#* Use `readline()` to read only
#* the first two lines.

#* Print both lines.

# file = open("student.txt", "r")
# data1 = file.readline()
# data2 = file.readline()
# print(data1)
# print(data2)
# file.close()



#& 🔴 Question 7 – Read All Lines

#* Create a file named `students.txt`.

#* Write:

#^ "Pravin"
#^ "Rahul"
#^ "Amit"

#* Open the file in Read mode.

#* Use `readlines()`.

#* Print the result.

#^ Expected Output:

#^ ['Pravin\n', 'Rahul\n', 'Amit']

# file = open("student.txt", "r")
# data = file.readlines()
# print(data)
# file.close()



#& 🔴 Question 8 – Count Number of Lines

#* Create a file named `students.txt`.

#* Write:

#^ "Pravin"
#^ "Rahul"
#^ "Amit"
#^ "Vijay"

#* Open the file in Read mode.

#* Use `readlines()`.

#* Find the number of lines using `len()`.

#* Print the number of lines.

#^ Expected Output:

#^ 4

# file = open("student.txt", "r")
# data = file.readlines()
# print(len(data))
# file.close()



#& 🔴 Question 9 – Check Cursor Position

#* Create a file named `message.txt`.

#* Write:

#^ "Python Programming"

#* Open the file in Read mode.

#* Print the current cursor position.

#* Read 6 characters.

#* Print the cursor position again.

#^ Expected Output:

#^ 0
#^ 6

# file = open("message.txt", "r")
# print(file.tell())
# file.read(6)
# print(file.tell())
# file.close()


#& 🔴 Question 10 – Use seek()

#* Create a file named `message.txt`.

#* Write:

#^ "Python Programming"

#* Open the file in Read mode.

#* Read the first 6 characters.

#* Use `seek(0)`.

#* Read the complete file again.

#* Print both results.

#^ Expected Output:

#^ Python
#^ Python Programming

# file = open("message.txt", "r")
# print(file.read(6))
# file.seek(0)
# print(file.read())
# file.close()