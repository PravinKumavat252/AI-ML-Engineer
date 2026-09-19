
#! ==========================================
#! with open() – CONTEXT MANAGER
#! ==========================================


#? What is `with open()`?

#~ `with open()` Python mein file ko
#~ safely open aur manage karne ka
#~ simple method hai.

#~ Iska main benefit hai:

#^ File ka kaam complete hone ke baad
#^ file automatically close ho jati hai.


#~ Simple Line:

#~ with open() → Open → Work → Automatically Close


#& ----------------------------------------
#& Why use `with open()`?
#& ----------------------------------------

#~ Normal way mein hume manually
#~ `close()` karna padta hai.

#^ Example:

#* file = open("student.txt", "r")

#* data = file.read()

#* print(data)

#* file.close()


#~ Yahan `close()` manually likhna padta hai.


#~ Lekin `with open()` mein
#~ manually `close()` likhne ki
#~ zarurat nahi hoti.


#& ----------------------------------------
#& Syntax
#& ----------------------------------------

#* with open("filename", "mode") as file:
#*     # File operation


#~ Yahan:

#^ `open()`
#~ → File open karta hai.


#^ `"filename"`
#~ → File ka naam.


#^ `"mode"`
#~ → File mode.


#^ `as file`
#~ → File object ko `file` naam deta hai.


#& ----------------------------------------
#& Example – Read File
#& ----------------------------------------

#* with open("student.txt", "r") as file:
#*     data = file.read()
#*     print(data)


#~ File open hui.

#~ Data read hua.

#~ Block complete hone ke baad
#~ file automatically close ho gayi.


#& ----------------------------------------
#& Example – Write File
#& ----------------------------------------

#* with open("student.txt", "w") as file:
#*     file.write("My name is Pravin.")


#~ File Write mode mein open hui.

#~ Data write hua.

#~ Block complete hone ke baad
#~ file automatically close ho gayi.


#& ----------------------------------------
#& Example – Append File
#& ----------------------------------------

#* with open("student.txt", "a") as file:
#*     file.write("\nPython is easy.")


#~ Existing content safe rahega.

#~ New content file ke end mein
#~ add hoga.


#& ----------------------------------------
#& Checking File is Closed
#& ----------------------------------------

#* with open("student.txt", "r") as file:
#*     print(file.read())

#* print(file.closed)


#^ Output:

#^ True


#~ `closed`

#~ Ye batata hai ki file close hai
#~ ya nahi.


#& ----------------------------------------
#& Normal open() vs with open()
#& ----------------------------------------


#^ Normal Method

#* file = open("student.txt", "r")
#* data = file.read()
#* print(data)
#* file.close()


#^ with open()

#* with open("student.txt", "r") as file:
#*     data = file.read()
#*     print(data)


#~ `with open()` mein
#~ `close()` automatically hota hai.


#& ----------------------------------------
#& Advantages
#& ----------------------------------------

#~ ✔ File automatically close hoti hai.

#~ ✔ Code clean aur short hota hai.

#~ ✔ File resources properly manage hote hain.

#~ ✔ Error aane par bhi file
#~ properly close hone mein help milti hai.

#~ ✔ Real-world Python projects mein
#~ commonly use hota hai.


#& ----------------------------------------
#& Important Rule
#& ----------------------------------------

#~ `with` ke andar file ke
#~ operations indentation ke andar
#~ likhe jate hain.


#* with open("student.txt", "r") as file:
#*     print(file.read())


#~ Ye correct hai.


#~ `with` ke bahar:

#* print(file.read())


#~ generally file already closed hogi,
#~ isliye file operation nahi karna chahiye.


#& ----------------------------------------
#& File Modes with with open()
#& ----------------------------------------

#^ Read

#* with open("student.txt", "r") as file:
#*     print(file.read())


#^ Write

#* with open("student.txt", "w") as file:
#*     file.write("Hello Python")


#^ Append

#* with open("student.txt", "a") as file:
#*     file.write("\nHello Python")


#& ----------------------------------------
#& Easy Memory Trick
#& ----------------------------------------

#~ Bas ye pattern yaad rakho:

#^ with open() as file:
#^     work


#~ Meaning:

#^ Open
#^   ↓
#^ Work
#^   ↓
#^ Automatically Close


#& ----------------------------------------
#& Important Points
#& ----------------------------------------

#~ ✔ `with open()` is a Context Manager.

#~ ✔ File automatically close hoti hai.

#~ ✔ `close()` manually call karne ki
#~ zarurat nahi hoti.

#~ ✔ Indentation important hai.

#~ ✔ Read, Write aur Append modes
#~ ke saath use kar sakte hain.


#& ----------------------------------------
#& Interview Definition
#& ----------------------------------------

#? What is `with open()`?

#~ `with open()` is a safe and convenient
#~ way to handle files in Python.

#~ It automatically closes the file
#~ after the block of code is completed.


#& ==========================================
#& FINAL CONCEPT
#& ==========================================

#^ Normal:

#~ open → work → close manually


#^ with open():

#~ open → work → automatically close


#~ Best practice:

#* with open("file.txt", "r") as file:
#*     data = file.read()


#? Assignment:


#& 🔴 Question 1 – Read File

#* Open `student.txt` using `with open()`.

#* Read the complete file using `read()`.

#* Print the content.

#~ File automatically close honi chahiye.

# with open("student.txt", "r") as file:
#     data = file.read()
#     print(data)



#& 🔴 Question 2 – Read First Line

#* Open `student.txt` using `with open()`.

#* Use `readline()` to read the first line.

#* Print the line.

# with open("student.txt", "r") as file:
#     data = file.readline()
#     print(data)



#& 🔴 Question 3 – Read All Lines

#* Open `student.txt` using `with open()`.

#* Use `readlines()`.

#* Print the list of lines.

# with open("student.txt", "r") as file:
#     data = file.readlines()
#     print(data)



#& 🔴 Question 4 – Write Data

#* Open `student.txt` using `with open()`
#* in Write mode.

#* Write:

#^ "Name: Pravin"

#* Do not use `close()`.

# with open("student.txt", "w") as file:
#     file.write("Name: Pravin")



#& 🔴 Question 5 – Write Multiple Lines

#* Open `student.txt` using `with open()`
#* in Write mode.

#* Write:

#^ "Name: Pravin"
#^ "Course: MSc AI/ML"
#^ "Marks: 85"

#* Do not use `close()`.

# with open("student.txt", "w") as file:
#     file.write("Name: Pravin\n Course: MSc AI/ML \n Marks: 85")
    

 
#& 🔴 Question 6 – Append Data

#* Open `student.txt` using `with open()`
#* in Append mode.

#* Add:

#^ "Python Programming"

#* Do not use `close()`.

# with open("student.txt", "a") as file:
#     file.write("\nPython Programming")



#& 🔴 Question 7 – Check File Closed

#* Open `student.txt` using `with open()`.

#* Print the file content.

#* Outside the `with` block,

#* Check whether the file is closed
#* using `file.closed`.

#^ Expected Output:

#^ True

# with open("student.txt", "r") as file:
#     data = file.read()
#     print(data)

# print(file.closed)



#& 🔴 Question 8 – Complete File Handling

#* Open `student.txt` using `with open()`.

#* Read the complete file.

#* Print the content.

#* Print the current cursor position
#* using `tell()`.

#* Outside the `with` block,
#* print `file.closed`.

#^ Your program should show:

#^ File Content
#^ Cursor Position
#^ True

# with open("student.txt", "r") as file:
#     data = file.read()
#     print(data)

#     print(file.tell())

# print(file.closed)