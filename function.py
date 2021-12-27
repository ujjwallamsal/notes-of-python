# creating a function
def fun():
    print("welcome to python")
fun()


# arguments of function
def oddeven(x):
    if (x % 2==0):
        print("it is even") #even
    else:
        print("it is odd")
oddeven(2)


#types of arguments
# 1. default arguments
def myfun(x , y=90):
    print(x)  #10
    print(y)  #90
myfun(10)

#keyword arguments
def student(firstname, lastname):
    print(firstname, lastname) #python programming
student(firstname='Python', lastname='Programming')
student(lastname='Development', firstname='Web') #web development

#variable length arguments
def myfun(*argv):
    for arg in argv:
        print(arg)
myfun(1, "to" , 3)
# *args will be a tuple containing all values that are passed in.

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='Python', mid='is the best', last='Programming language')

#docstring
def evenOdd(x):
    """Function to check if the number is even or odd"""
    if (x % 2 == 0):
        print("even")
    else:
       print("odd")
print(evenOdd.__doc__)

#return statement
def sum(num , num1):
    "this function returns the sum"
    return num1+num
print(sum(1 , 2))  #3

def myFun(x):
    x[0] = 20
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

def myFun(x):
    x = [20, 30, 40]
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

def swap(x, y):
    temp = x
    x = y
    y = temp
x = 2
y = 3
swap(x, y)
print(x)
print(y)

# Python Function within Functions
def f1():
    s = 'I love Python'
    def f2():
        print(s)
    f2()
f1()
# Global and Local Variables
def f():
    s = "I love Python"
    print(s)
f()

#global variable
def f():
    print("Inside Function", s)
s = "I love Python"
f()
print("Outside Function", s)

# global and local variable same name
def f():
    s = "Me too."
    print(s)
s = "I love Python"
f()
print(s)

# global keyword
def f():
    global s
    s+= " and javascript"
    print(s) #great and java script
    global w
    w = "python"
    print(w) # python
w = "python is great"
s = 'great'
f()

#Using global and local variables
a = 1
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)

# Python Modules

# create a simple module
def add(x, y):
    return (x+y)
def subtract(x, y):
    return (x-y)

# Import Module in Python – Import statement
# import calc
# print(calc.add(10, 2))
# from  import add, subtract
# print(add(10,2))
# print(subtract(10,2))

from math import sqrt, factorial
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))

import math as m
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(m.sqrt(16)) #4.0
print(m.factorial(6)) #720

# math Module
import math
print(math.pi) #3.141592653589793

# area of circle
import math
r = 4
pie = math.pi
print(pie*r*r)  #50.26548245743669

# Finding the ceiling and the floor value
import math
a = 2.3
# returning the ceil of 2.3
print ("The ceil of 2.3 is : ", end="")
print (math.ceil(a))
# returning the floor of 2.3
print ("The floor of 2.3 is : ", end="")
print (math.floor(a))

# Finding the factorial of the number
import math
a = 5
# returning the factorial of 5
print("The factorial of 5 is : ", end="")
print(math.factorial(a)) #120

# Finding the GCD
import math
a = 15
b = 5
# returning the gcd of 15 and 5
print ("The gcd of 5 and 15 is : ", end="")
print (math.gcd(b, a)) #5

# Finding the absolute value
import math
a = -10
# returning the absolute value.
print ("The absolute value of -10 is : ", end="")
print (math.fabs(a)) #10.0

# Finding the power of a number
print ("The value of 3**4 is : ",end="")
# Returns 81
print (pow(3,4))

# Finding the Logarithm
import math

# returning the log of 2,3
print ("The value of log 2 with base 3 is : ", end="")
print (math.log(2,3))
# returning the log2 of 16
print ("The value of log2 of 16 is : ", end="")
print (math.log2(16))
# returning the log10 of 10000
print ("The value of log10 of 10000 is : ", end="")
print (math.log10(10000))

# Finding the Square root
import math
# print the square root of 0
print(math.sqrt(0))
# print the square root of 4
print(math.sqrt(4))
# print the square root of 3.5
print(math.sqrt(3.5))

# Finding sine, cosine, and tangent
import math
a = math.pi/6
# returning the value of sine of pi/6
print ("The value of sine of pi/6 is : ", end="")
print (math.sin(a))
# returning the value of cosine of pi/6
print ("The value of cosine of pi/6 is : ", end="")
print (math.cos(a))
# returning the value of tangent of pi/6
print ("The value of tangent of pi/6 is : ", end="")
print (math.tan(a))

# random module
# import random
# # prints a random value from the list
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))

# random.choice()
# import random
# prints a random value from the list
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))
# # prints a random item from the string
# string = "python"
# print(random.choice(string))
# # prints a random item from the tuple
# tuple1 = (1, 2, 3, 4, 5)
# print(random.choice(tuple1))

# random.random()
from random import random
lst = []
for i in range(10):
    lst.append(random())
# Prints random items
    print(lst)
# random.randint()

import random

# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']
print("Original list : ")
print(sample_list)
# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)