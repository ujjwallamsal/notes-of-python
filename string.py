# Accessing characters in Python
String1 = "Python Programming"
print(String1) #python programming
# Printing First character
print("\nFirst character of String is: ")
print(String1[0]) #p
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1]) #g

# slicing string
a = "ujjwal"
print("/nslicing character from 1:3")
print(a[1:3]) #jj

b = "pythonprogramming"
print(b[-5:-3]) #mm

c = "welcome to my world"
print("\nSlicing characters between " +
"3rd and 2nd last character: ")
print(c[3:-2]) #come to my wor

# Deleting/Updating from a String

# a = "welcome to my first programming"
# # updating a character
# a[3] = "u" 
# print(a)  # error

a = "ujjwal"
# print(a)   #ujjwal
a = "lamsal"
print(a)  #lamsal

#deleting a character
# a = "python"
# b = del a[0]
# print(b)

# String1 = "Hello, I'm a Python Developer"
# print("Initial String: ")
# print(String1)
# # Deleting a character
# # of the String
# del String1[2]
# print("\nDeleting character at 2nd Index: ")
# print(String1)  #error because 'str' object doesn't support item deletion

# # Deleting Entire String

# string1 = "Hello, I'm a Python Developer"
# del string1
# print(string1) #error because 'str' object doesn't support item deletion

# Escape Sequencing

# Python Program for
# Escape Sequencing
# of String
# Initial String
String1 = '''I'm a "Python Developer"'''
print("Initial String with use of Triple Quotes: ")
print(String1) #I'm a "Python Developer"
# Escaping Single Quote
String1 = 'I\'m a "Python Developer"'
print("\nEscaping Single Quote: ")
print(String1)  #I'm a "Python Developer"
# Escaping Double Quotes
String1 = "I'm a \"Python Developer\""
print("\nEscaping Double Quotes: ")
print(String1)  #I'm a "Python Developer"
# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Programs\\"
print("\nEscaping Backslashes: ")
print(String1)  #C:\Python\Programs\


# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Python', 'for', 'web development')
print("Print String in default order: ")
print(String1) #Python for web development
# Positional Formatting
String1 = "{1} {0} {2}".format('python', 'for', 'data science')
print("\nPrint String in Positional order: ")
print(String1) #for python data science
# Keyword Formatting
String1 = "{l} {f} {g}".format(g='python', f='for', l='machine learning')
print("\nPrint String in order of Keywords: ")
print(String1)  #machine learning for python

# use of f-strings
# Python3 program introducing f-string
val = 'python'
lang = 'language'
print(f"{val} is a programming {lang}") #python is a programming language

name = 'ujjwal'
age = 19
print(f"Hello, My name is {name} and I'm {age} years old.") #Hello, My name is ujjwal and I'm 19 years old.

# String Concatenation in Python

# using + operator 
var1 = "ujjwal"
var2 = "lamsal"
#+ operator is used to combine string
var3 = var1+ var2
print(var3) #ujjwallamsal

# using join() method
a = "ujjwal"
b = "lamsal"
c = " ".join([a,b])
print(c) #ujjwal lamsal

# using ','
var1 = "hello world"
var2 = "python programming"
print(var1 , var2)  #hello world python programming

# Iterating Through a string
#    Using simple iteration and range()

a = "ujjwallamsal"
for ele in a:
    print(ele , end=" ") #u j j w a l l a m s a l
print("\n") #       

# Using enumerate() function
a = "ujjwal lamsal"
for i , v in enumerate(a):
    print(v) 
# u
# j
# j
# w
# a
# l

# l
# a
# m
# s
# a
# l

  
# iterate character in reverse order
string = "python"
# slicing the string in reverse fashion
for ele in string[::-1]:
    print(ele , end = " ")  #n o h t y p

string2 = "python programming"
ran = len(string2)
for ele in reversed(range(0 , ran)):
    print(string2[ele])
# g
# n
# i
# m
# m
# a
# r
# g
# o
# r
# p

# n
# o
# h
# t
# y
# p

#Iteration over particular set of element
a = "python programming"
# string_name[start:end:step]
for ele in a[1:4:2]:
    print(ele , end=" ")  #y h


# string membership test
a = "program"
b = "a" in a
print(b) #true
print("a" not in a) #false


# logical operators on string
str1 = ''
str2 = 'python'
# repr is used to print the string along with the quotes
# Returns str1
print(repr(str1 and str2))
# Returns str1
print(repr(str2 and str1))
# Returns str2
print(repr(str1 or str2))
# Returns str2
print(repr(str2 or str1))
str1 = 'for'
# Returns str2
print(repr(str1 and str2))
# Returns str1
print(repr(str2 and str1))
# Returns str1
print(repr(str1 or str2))
# Returns str2
print(repr(str2 or str1))
str1='geeks'
# Returns False
print(repr(not str1))
str1 = ''
# Returns True
print(repr(not str1))

# Splitting a String in Python
line = "Python \nJavascript \nC++"
print(line.split()) #['Python', 'Javascript', 'C++']
print(line.split(' ', 1)) #['Python', '\nJavascript \nC++']

# string method
# 1. find("string",beg,end)
a = "python"
print(a)

# 2.rfind("string" ,beg,end)
a = "python for python programming"
b = "python"
print(a.rfind("python", 1 , 3))  #-1

print(a.find("for",1,2))#-1

# 4.endswith(“string”, beg, end)
str = "python"
str1 = "pythonforpythonportal"
# using startswith() to find if str
# starts with str1
if str1.startswith(str):
    print ("str1 begins with : " + str)#str1 begins with : python
else : 
    print ("str1 does not begin with : "+ str)
# using endswith() to find
# if str ends with str1
if str1.endswith(str):
    print ("str1 ends with : " + str)
else :
    print ("str1 does not end with : " + str)#str1 does not end with : python
    

# 6. isupper(“string”)
str = "Python Programming"
str1 = "Web Development"
# checking if all characters in str are upper cased
if str.isupper() :
    print ("All characters in str are upper cased")
else :
    print ("All characters in str are not upper cased")#All characters in str are not upper cased
# checking if all characters in str1 are lower cased
if str1.islower() :
    print ("All characters in str1 are lower cased")
else :
    print ("All characters in str1 are not lower cased")#All characters in str are not upper cased

# 10. title()
a = "Python programming is good"
b = a.lower();
print("the lower case converted is: " + b) #the lower case converted is: Python programming is good
b = a.upper();
print("the upper case converted is: " + b) #the upper case converted is: PYTHON PROGRAMMING IS GOOD

b = a.swapcase();
print("the swapcase converted is : " + b) #the swapcase converted is : pYTHON PROGRAMMING IS GOOD

b = a.title();
print("the tittle converted is: " + b) #the tittle converted is: Python Programming Is Good

#11.len()
a = "python"
print(len(a)) #6

#12.count("string",beg,end)
str = "python for Automation and Scripting"
# Printing length of string using len()
print (" The length of string is : ", len(str));
# Printing occurrence of "python" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""python"" is : ",end="") # The length of string is :  35
print (str.count("python",0,15))#Number of appearance of python is : 1

# 15. rjust()
str = "Python is the coolest programming language in the world"
# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))
# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))
# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))


a = "python programming"
b = "1234"
# checking if all str has all alphabet
if (a.isalpha()):
    print("all character are alphabet in string")
else:
    print("all character are not in alphabet") #all character are not in alphabet

# checking if b has all numbers
if (b.isalnum()):
    print("all character are number in b") #all character are number in b
else:
    print("all character are not in numbers")

# checking if b has all spaces
if(b.isspace()):
    print("all character are space in b")
else:
    print("all character are not in space b") #all character are not in space b

# 19.join()
str = "-"
str1 = ("django" , "is", "used", "in", "backend programming")
print ( str.join(str1)) #django-is-used-in-backend programming

# 22.rstrip()
str = "---helloworld---"
# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') ) # String after stripping all '-' is : helloworld
# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') ) # String after stripping all leading '-' is : helloworld---
# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') ) #String after stripping all trailing '-' is : ---helloworld

# 27.replace()
str = "C++ is a programming language"
str1 = "C++"
str2 = "Python"
# using replace() to replace str2 with str1 in str
# only changes 2 occurrences
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) #The string after replacing strings is : Python is a programming language 

# 29. split()
text = 'python for artificial intelligence'
# Splits at space
print(text.split())
word = 'python, for, artificial,intelligence'
# Splits at ','
print(word.split(','))
word = 'python:for:machine:learning'
# Splitting at ':'
print(word.split(':'))
word = 'CatBatSatFatOr'
# Splitting at t
print(word.split('t'))

# 30. partition()
string = "python is best"
# 'is' separator is found
print(string.partition('is '))
# 'not' separator is not found
print(string.partition('bad '))
string = "python is good, isn't it"
# splits at first occurrence of 'is'
print(string.partition('is'))
