info= {
    "Name": "Faizan",
    "age": 19,
    "Department": "CS",
    "Marks": [90, 87, 93, 79],
    "CGPA": 3.5
}

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