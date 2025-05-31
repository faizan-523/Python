grade=("A", "B", "C", "A", "A")
print(grade)

#tuple is Immutable we can not append sort or something etc  if we want to do something 
#first we should convert tuple into list

grade_list = list(grade)
grade_list.append("B")

grade_list.sort()

print("Updated & Sorted Grades:", grade_list)