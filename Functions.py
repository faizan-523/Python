#Functions in Python
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.

def sum(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The sum is:", sum(num1, num2))

# You can also define a function without parameters
def hello():
    print("Hello, World!")

hello() #it will print Hello, World! because we called the function

# Functions can also return values
def multiply(x, y):
    return x * y

result = multiply(num1, num2)
print("The product is:", result)

