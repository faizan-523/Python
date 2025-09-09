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

#There are 2 types of functions:
#Built-in functions: These are functions that are already defined in Python, like print(), input(), len(), etc.
#User-defined functions: These are functions that you define yourself, like the sum() and multiply

Students = ["Faizan", "Waleed", "Ali", "Ahmed"]
print(len(Students))  # This will print the number of students in the list

def Printlist(list):
    for item in list:
        print(item)

Printlist(Students) # This will print each student's name in the list

