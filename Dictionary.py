info= {
    "Name": "Faizan",
    "age": 19,
    "Department": "CS",
    "Marks": [90, 87, 93, 79],
    "CGPA": 3.5
}
#in dictionary we can store string lists and integer also at same time
# Dictionary is a collection of key-value pairs
# In dictionary on left side we have key and on right side we have value
# Key is unique and value can be anything like string, integer, list, etc.

print(info)
print(type(info))

print(info["Name"])
print(info["CGPA"])
print(info["Marks"])

info["Name"]= "Muhammad"
print(info)

print(info.keys())
print(info.values())

sub={"subjects": ["Database","Programming","MVC"]}
info.update(sub)

print(info)