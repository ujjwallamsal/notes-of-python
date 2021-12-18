 modulo
print(8%9) = 8

# arthemetic continued

# 1. powers
print(2**4) = 16

2.can also do root in this way
print(126**0.12)  = 1.12121221

3.order of operation followed in python
print(2+87*3+7)    = 1.7866704944604102

4. can use parantheses to specify orders
print((8-3)+(7*4))   = 33

variable assignment

1.lets create an object called "b" and assign it the number 76
a = 76 it means 76 is assigned to a

2. adding the object 
a = 10
print(a+a) =20

3. reassignment
a = 20
print(a)  = 20

note: / forward slash vs \backward slash

use a to redefine a
a = 20
a = a+a
print(a)  =40

The names you use when creating these labels need to follow a few rules:

1. Names can not start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
4. It's considered best practice (PEP8) that names are lowercase.
5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
or 'I' (uppercase letter eye) as single character variable names.
6. Avoid using words that have special meaning in Python like "list" and "str"

Using variable names can be a very useful way to keep track of different variables in
Python. For example:

Use object names to keep better track of what's going on in your code!
my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
print(my_taxes)   = 10


values and types

values
a = 5#number values
b = "python" #string value
c = 8.5  #float value

types
type( ) is used to find the type of any value / object.

print( type(23) ) # int
print( type(3.14) ) # float
print( type("hello") ) # str
print( type("23") ) # str
print( type("3.24") ) # str
print( type(None) ) # NoneType
print( type(True) ) # bool
print( type(False) ) # bool
print( type([]) ) # list
print( type({}) ) # dict
print( type(hello) ) # NameError: name 'hello' is not defined
print("Still running")
print( type(hello) ) # str but NameError: name 'hello' is not defined


Integer
a = 2
print(a)
# Output: 2
# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String
name = 'John Doe'
print(name)
# Output: John Doe
# Boolean
q = True
print(q)
# Output: True
# Empty value or null data type
x = None
print(x)
# Output: None


a = 8574
print(type(a)) # Output: <type 'int'>
b = 67
print(type(b)) # Output: <type 'int'>
pi = 3.14
print(type(pi)) # Output: <type 'float'>
c = 'A'
print(type(c)) # Output: <type 'str'>
name = 'ujjwal lamsal'
print(type(name)) # Output: <type 'str'>
s = True
print(type(s)) # Output: <type 'bool'>
x = None
print(type(x)) # Output: <type 'NoneType'>

a, b, c = 1, 2, 3
print(a, b, c) # Output: 1 2 3
a, b, c = 6 , 9
print(a, b, c) #ValueError: need more than 2 values to unpac
a, b = 9, 6, 8
print(a, b, c) #ValueError: too many values to unpack


a = b = c = 1 # all three names a, b and c refer to same int o ject with value 1
print(a, b, c) # Output: 1 1 1
b = 2 # b now refers to another int object, one with a value of2
print(a, b, c) # Output: 1 2 1

import keyword
print(keyword.kwlist) ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
