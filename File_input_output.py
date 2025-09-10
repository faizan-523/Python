#File input and output in Python
#Opening a file
file= open('demo.txt', 'r')  # 'r' for read mode

#Reading from a file
line1 = file.readline()
print(line1) #it print 1st line
data = file.read()
print(data) #it print remaining lines
print(type(data)) #it print data type
print(len(data)) #it print length of data

#Once we read all lines, the cursor is at the end of the file 
#After reading, if we try to read again, it will return an empty string

file.close()

#Writing to a file
file = open('demo.txt', 'a')  # 'a' for append mode
#Append means it will add data at the end of the file 
#we should use 'w' mode to overwrite the file but it will delete all previous data

file.write("\n Now i am doing file handling in python")

file.close()

#We can also write and read from a file simultaneously using 'r+' or 'w+' or 'a+' modes
file = open('demo.txt', 'r+')
value= file.read()
print(value)

file.write("\n Python is great language")
file.close()

#Using 'with' statement to handle files
#It automatically takes care of closing the file
with open('demo.txt', 'r') as file:
    content = file.read()
    print(content)