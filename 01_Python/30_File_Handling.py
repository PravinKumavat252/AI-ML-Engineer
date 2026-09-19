
#! ==========================================
#! FILE HANDLING IN PYTHON
#! ==========================================


#? What is File Handling?

#~ File Handling ka matlab hai
#~ Python program ke through
#~ files ko create, open, read, write,
#~ update aur close karna.


#~ Simple Line:

#~ File Handling → File ke saath kaam karna


#& ----------------------------------------
#& Why do we use File Handling?
#& ----------------------------------------

#~ File Handling ka use mainly:

#^ 1. Data ko permanently store karne ke liye.
#^ 2. Existing data ko read karne ke liye.
#^ 3. New data file mein write karne ke liye.
#^ 4. Existing data ko update karne ke liye.
#^ 5. Large amount of data ko manage karne ke liye.


#& ----------------------------------------
#& Why Files are Important?
#& ----------------------------------------

#~ Variables mein stored data temporary hota hai.

#~ Program close hone ke baad
#~ variable ka data normally lost ho jata hai.

#~ Lekin file mein data save karne par
#~ data permanently store ho sakta hai.


#? Example:

#^ Variable:

#* name = "Pravin"

#~ Program close hone ke baad
#~ variable ka data memory se remove ho sakta hai.


#^ File:

#* student.txt

#~ Data file mein save karne par
#~ baad mein dobara read kiya ja sakta hai.


#& ----------------------------------------
#& Types of Files
#& ----------------------------------------

#~ Python mein mainly two types ki
#~ files ke saath kaam kiya jata hai.


#^ 1. Text File

#~ Text file mein normal readable
#~ characters aur text store hota hai.

#^ Examples:

#~ `.txt`
#~ `.csv`
#~ `.py`
#~ `.html`


#^ 2. Binary File

#~ Binary file data ko
#~ binary format mein store karti hai.

#^ Examples:

#~ `.jpg`
#~ `.png`
#~ `.mp3`
#~ `.mp4`
#~ `.pdf`


#& ----------------------------------------
#& File Handling Process
#& ----------------------------------------

#~ File ke saath kaam karne ka
#~ basic process:

#^ Open
#^   ↓
#^ Read / Write
#^   ↓
#^ Close


#~ Simple:

#^ Open → Work → Close


#& ----------------------------------------
#& open() Function
#& ----------------------------------------

#~ Python mein file open karne ke liye
#~ `open()` function use hota hai.


#^ Syntax:

#* open("filename", "mode")


#~ Example:

#* file = open("student.txt", "r")


#~ Yahan:

#^ `student.txt`
#~ → File ka name


#^ `"r"`
#~ → File open karne ka mode


#& ----------------------------------------
#& File Object
#& ----------------------------------------

#~ `open()` function file ko open karke
#~ ek **file object** return karta hai.


#* file = open("student.txt", "r")

#~ Yahan:

#^ `file`
#~ → File object


#~ Is file object ke through
#~ hum file ke data par operations
#~ perform kar sakte hain.


#& ----------------------------------------
#& File Modes
#& ----------------------------------------

#~ File mode batata hai ki
#~ file ke saath kya operation karna hai.


#^ Main File Modes:

#^ `r` → Read

#^ `w` → Write

#^ `a` → Append

#^ `x` → Create

#^ `b` → Binary

#^ `t` → Text


#& ----------------------------------------
#& 1. Read Mode – "r"
#& ----------------------------------------

#~ `r` mode ka use file ka
#~ existing data read karne ke liye hota hai.


#^ Syntax:

#* file = open("student.txt", "r")


#~ Agar file exist nahi karti,
#~ to `FileNotFoundError` aa sakta hai.


#& ----------------------------------------
#& 2. Write Mode – "w"
#& ----------------------------------------

#~ `w` mode ka use file mein
#~ data write karne ke liye hota hai.


#^ Syntax:

#* file = open("student.txt", "w")


#~ Agar file exist nahi karti:

#~ → New file create ho sakti hai.


#~ Agar file already exist karti hai:

#~ → Existing content overwrite ho sakta hai.


#~ Important:

#^ `w` → Old content ko overwrite kar sakta hai.


#& ----------------------------------------
#& 3. Append Mode – "a"
#& ----------------------------------------

#~ `a` mode ka use existing file ke
#~ end mein new data add karne ke liye hota hai.


#^ Syntax:

#* file = open("student.txt", "a")


#~ Existing data normally preserve rehta hai.

#~ New data end mein add hota hai.


#& ----------------------------------------
#& 4. Create Mode – "x"
#& ----------------------------------------

#~ `x` mode ka use new file create
#~ karne ke liye hota hai.


#^ Syntax:

#* file = open("student.txt", "x")


#~ Agar file already exist karti hai,
#~ to error aa sakta hai.


#& ----------------------------------------
#& 5. Binary Mode – "b"
#& ----------------------------------------

#~ `b` mode binary data ke liye
#~ use hota hai.


#^ Example:

#* open("image.jpg", "rb")


#~ `rb`

#^ r → Read

#^ b → Binary


#& ----------------------------------------
#& 6. Text Mode – "t"
#& ----------------------------------------

#~ `t` mode text files ke liye
#~ use hota hai.


#^ Example:

#* open("student.txt", "rt")


#~ `rt`

#^ r → Read

#^ t → Text


#~ Text mode default bhi hota hai.


#& ----------------------------------------
#& Reading a File
#& ----------------------------------------

#~ File read karne ke liye
#~ `read()` method use kar sakte hain.


#* file = open("student.txt", "r")

#* data = file.read()

#* print(data)

#* file.close()


#~ Yahan:

#^ `read()`
#~ → File ka content read karta hai.


#^ `close()`
#~ → File ko close karta hai.


#& ----------------------------------------
#& Closing a File
#& ----------------------------------------

#~ File ka kaam complete hone ke baad
#~ file ko close karna important hai.


#^ Syntax:

#* file.close()


#~ Example:

#* file = open("student.txt", "r")

#* data = file.read()

#* print(data)

#* file.close()


#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#~ File modes yaad rakhne ka simple way:

#^ `r` → Read

#^ `w` → Write

#^ `a` → Add

#^ `x` → Create

#^ `b` → Binary

#^ `t` → Text


#& ----------------------------------------
#& Important Points
#& ----------------------------------------

#~ ✔ `open()` file open karta hai.

#~ ✔ `read()` file ka data read karta hai.

#~ ✔ `write()` file mein data write karta hai.

#~ ✔ `close()` file close karta hai.

#~ ✔ `r` → Read

#~ ✔ `w` → Write / Overwrite

#~ ✔ `a` → Add at the end

#~ ✔ `x` → Create new file


#& ----------------------------------------
#& Quick Revision
#& ----------------------------------------

#^ File Handling

#~ File ke data ko
#~ read, write, append aur manage karna.


#^ Basic Process:

#~ Open → Read/Write → Close


#^ Basic Syntax:

#* file = open("filename", "mode")


#^ Example:

#* file = open("student.txt", "r")

#* data = file.read()

#* print(data)

#* file.close()


#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#~ File Handling ka main purpose hai
#~ files ke through data ko
#~ permanently store aur manage karna.

#^ Remember:

#^ open()  → File Open
#^ read()  → Data Read
#^ write() → Data Write
#^ close() → File Close


#^ File Modes:

#^ r → Read
#^ w → Write
#^ a → Append
#^ x → Create
#^ b → Binary
#^ t → Text


#? Assignment:


#& 🔴 Question 1 – Create and Write

#* Create a file named `student.txt`.

#* Open the file in Write mode.

#* Write:

#^ "My name is Pravin."

#* Close the file.

# file = open("student.txt", "w")
# data = file.write("My name is Pravin.")
# file.close()



#& 🔴 Question 2 – Write Multiple Lines

#* Create a file named `student.txt`.

#* Open the file in Write mode.

#* Write:

#^ "Name: Pravin"
#^ "Course: MSc AI/ML"
#^ "University: Monark University"

#* Close the file.

# file = open("student.txt", "w")
# data = file.write("""Name: Pravin,
# Course: MSc AI/ML,
# University: Monark University""")
# file.close()



#& 🔴 Question 3 – Read a File

#* Create a file named `student.txt`.

#^ Store:

#^ "Python is easy to learn."

#* Open the file in Read mode.

#* Read the complete content.

#* Print the content.

#* Close the file.

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()



#& 🔴 Question 4 – Read Student Details

#* Create a file named `student.txt`.

#* Write:

#^ "Name: Pravin"
#^ "Age: 23"
#^ "Course: MSc AI/ML"

#* Open the file in Read mode.

#* Read and print the complete content.

#* Close the file.

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()



#& 🔴 Question 5 – Append Data

#* Create a file named `student.txt`.

#* Write:

#^ "Name: Pravin"

#* Close the file.

#* Open the same file in Append mode.

#* Add:

#^ "Course: MSc AI/ML"

#* Close the file.

#* Open the file in Read mode.

#* Print the complete content.

# file = open("student.txt", "w")
# file.write("Name: Pravin, \n")
# file.close()

# file = open("student.txt", "a")
# file.write("Course: MSc AI/ML")
# file.close()

# file = open("student.txt", "r")
# print(file.read())
# file.close()



#& 🔴 Question 6 – Add Multiple Students

#* Create a file named `students.txt`.

#* Write:

#^ "Pravin"
#^ "Rahul"
#^ "Amit"

#* Close the file.

#* Open the file in Append mode.

#* Add:

#^ "Vijay"

#* Close the file.

#* Read and print the complete file.

# file = open("student.txt", "w")
# file.write("""Pravin 
# Rahul  
# Amit \n""")
# file.close()

# file = open("student.txt", "a")
# file.write("Vijay")
# file.close()

# file = open("student.txt", "r")
# print(file.read())
# file.close()



#& 🔴 Question 7 – Overwrite File

#* Create a file named `data.txt`.

#* Write:

#^ "Old Data"

#* Close the file.

#* Open the same file in Write mode.

#* Write:

#^ "New Data"

#* Close the file.

#* Read and print the file.

#^ Expected Output:

#^ New Data

# file = open("data.txt", "w")
# file.write("Name : Pravin")
# file.close()

# file = open("data.txt", "w")
# file.write("Name : Pravin Kumavat")
# file.close()

# file = open("data.txt", "r")
# print(file.read())
# file.close()



#& 🔴 Question 8 – Create a New File

#* Create a file named `new_file.txt`.

#* Open the file using Create mode.

#* Write:

#^ "File Created Successfully"

#* Close the file.

#* Open the file in Read mode.

#* Print the content.

# file = open("new_file.txt", "w")
# file.write("File Created Successfully")
# file.close()

# file = open("new_file.txt", "r")
# print(file.read())
# file.close()



#& 🔴 Question 9 – Count Characters

#* Create a file named `message.txt`.

#* Write:

#^ "Python Programming"

#* Read the content of the file.

#* Find the number of characters using `len()`.

#* Print the character count.


#^ Expected Output:

#^ 18

# file = open("message.txt", "w")
# file.write("Python Programming")
# file.close()

# file = open("message.txt", "r")
# data = file.read()
# print(data)
# print(len(data))
# file.close()



#& 🔴 Question 10 – Student File

#* Create a file named `student.txt`.

#* Write:

#^ "Name: Pravin"
#^ "Marks: 85"
#^ "Result: Pass"

#* Close the file.

#* Open the file in Read mode.

#* Read and print the complete content.

#* Close the file.

# file = open("student.txt", "w")
# file.write("""Name: Pravin
# Marks: 85
# Result: Pass""")
# file.close()

# file = open("student.txt", "r")
# print(file.read())
# file.close()