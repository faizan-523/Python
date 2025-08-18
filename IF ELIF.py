marks= int(input("enter yout marks: "))

# This program calculates the grade based on marks using if-elif-else statements
# It assigns grades A, B, C, D, or F based on the marks obtained
# In IF ELIF statements, the first condition that is true will be executed
# If no conditions are true, the else block will be executed

if(marks >= 90):
    grade="A"
elif(marks >= 80 and marks<90):
    grade="B"
elif(marks >= 70 and marks<80):
    grade="C"
elif(marks >= 60 and marks<70):
    grade="D"
else:
    grade="F"

print("Your Grade is: ", grade)
