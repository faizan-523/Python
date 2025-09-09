#Recursion in Python
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# A recursive function must have a base case to stop the recursion, otherwise it will continue indefinitely.
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print("The factorial of", num, "is", factorial(num)) # it will print the factorial of the number