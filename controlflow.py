#  if statement
# i = 10
# if i<15:
#     print("10 is less than 15")  #10 is less than 15
# print("i am not if")  #i am not if

# if-else

# i = 20
# if (i < 15):
#     print("i is smaller than 15")
#     print("i'm in if Block")
# else:
#     print("i is greater than 15")
#     print("i'm in else Block")
# print("i'm not in if and not in else Block")+
# # i is greater than 15
# # i'm in else Block
# # i'm not in if and not in else Block

# if else in list comprehension(for later)

# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

# Initializing list
List = [367, 111, 562, 945, 6726, 873]
# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]
# Displaying new list
print(newList)

# 3.nested-if
i = 10
if (i==10):
    #first if statement
    if(i<15):
        print("i is smaller than 15") #i is smaller than 15 
# nested -if statement
# will only be executed if statement above
# it is true
if(i<12):
    print("i is smaller than 12 too") #i is smaller than 12 too
else:
    print("i is greater than 15")

# 4. if-elif-else ladder
i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif(i == 20):
    print("i is 20") #i is 20
else:
    print("i is not present")

# 5. Chaining comparison operators
x = 5
print(1 < x < 10) #true
print(10 < x < 20 ) #false
print(x < 10 < x*10 < 100) #true
print(10 > x <= 9) #true
print(5 == x > 4) #true

# 6. for loop

l = ["python" , "for" , "machine learning"]
for i in l:
    print(i , end=" ") #python for machine lerning

#iterating over a tuple(immutable)
t = ("python", "for", "machine learning")
for i in t:
    print(i , end=" ") #python for machine learning

# Iterating over a string
s = "python"
for l in s:
    print(l , end=" ") #p y t h o n

#Iterating over dictionary
d = {'a': 100, 'b': 200, 'c': 300}
for i in d:
    print(f"{i} : {d[i]}")
    print()
# a : 100    

# b : 200

# c : 300

# Loop Control Statements

#continue
for letter in 'pythonformachinelearning':
    if letter == 'e' or letter == 'u':
        continue
print(f'Current Letter : {letter}') #current letter: g

#break
for letter in 'pythonformachinelearning':
    if letter == 'e' or letter == 'u':
        break
print(f'Current Letter : {letter}') #curent letter : e

for letter in 'python':
    pass
print(f'Last Letter : {letter}') #n

# range() function
for i in range(10):
    print(i , end=" ") #0 1 2 3 4 5 6 7 8 9
print() 

l = [10 , 20 ,30 ,40]
for i in range(len(l)):
    print(i , end=" ") #0 1 2 3
print()

#performing sum of first 10 numbers
sum = 0
for i in range(1 , 10):
    sum = sum+1
print("the sum of first 10 number is: " , sum) #9

#for loop with else

#python program to demonstrate
# for - else loop

for i in range(1 ,4):
    print(i)
else:#executed because no break in for
    print("no break")  #no break

for i in range(1,4):
    print(i)  #1
    break
else:#not executed as there is a break
    print("no break")


# 7. while loop
# python program to illustare 
# while loop
count = 0
while(count<3):
    count= count +1
    print("hello there") 
# hello there
# hello there
#hello there

a = [1 , 2 , 3 , 4 ,5]
b = 1
while b < len(a):
    b=b+1
    print(f"{i}")
#1
#1
#1
#1

# Loop Control Statement
# continue
# i = 0
# a = "pythonofsoftwarefoundation"
# while i <len(a):
#     if a[i]=="e" or a[i] =="s":
#         i+=1
#     continue
# print(f'current letter:(a[i])')
# i +=1



# break the loop as soon it sees 'e'
# or 's'
# i = 0
# a = 'pythonsoftwarefoundation'
# while i < len(a):
#     if a[i] == 'e' or a[i] == 's':
#         i += 1
#         break
# print(f'Current Letter :{a[i]}')
# i += 1

# An empty loop
a = 'pythonsoftwarefoundation'
i = 0
while i < len(a):
    i += 1
    pass
print(f'Value of i : {i}') #24

#while loop with else

i = 0
while i <4:
    i+=1
    print(i)
else:
    print("no break") #no break

# a = int(input('Enter a number (-1 to quit): '))
# while a != -1:
#     a = int(input('Enter a number (-1 to quit): '))


#break
s = 'pythonsoftwarefoundation'
# using for loop
for letter in s:
    print(letter)
    if letter=='e' or letter =='s':
        break
print("out of loop") #out of loop
print()

i = 0
#using while loop
while True:
    print(s[i])
    if s[i]=='e' or s[i] =='s':
        break
    i +=1
print("out of loop") #out of loop

for i in range(1 , 10):
    if i ==6:
        continue
    else:
        print(i , end = " ") #1 2 3 4 5 7 8 9

a = 10
b = 20
if(a<b):
    pass
else:
    print("b<a")

