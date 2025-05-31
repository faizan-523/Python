string1 = input("Enter any string to check if it is a palindrome: ")
print(string1)

string2 = ''.join(reversed(string1))

if string1 == string2:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
