width = input("enter width of rectangle")
width = float(width)
height = input("enter height of rectangle")
height = float(height)
area = width * height
circum = 2 *  (width + height)
print("area of rectangle is", area)
print("circumference of rectangle is", circum)




def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if choice == '1':
           print(number1, "+", number2, "=", add(number1, number2))
        elif choice == '2':
           print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == '3':
           print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == '4':
           print(number1, "/", number2, "=", divide(number1, number2))
        break
    else: 
         print("Entered input is invalid")




r = 5
Area = 3.141 * r * r
print(Area)
Perimeter = 2 * 3.141 * r
print(Perimeter)

celsius = 20
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)

a = 12
b = 6
sum = a + b
diff = a - b
mul = a * b
div = a / b
print(sum)
print(diff)
print(mul)
print(div)

a = input("enter first line of poem: ")
b = input("enter second line of poem: ")
c = input("enter third line of poem: ")
d = input("enter fourth line of poem: ")
e = input("enter fifth line of the poem: ")
f = input("enter sixth line of the poem: ")
print(a+b+c+d+e)
