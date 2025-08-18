print("For Loop in Python")

print("Printing table of number which user will enter")

print("Enter a number:")
num = int(input()) #it will take input from user and convert it to integer
print("Table of", num, "is:")
# For Loop in Python to print the table of a number
# The loop will run from 1 to 10
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

