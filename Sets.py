collection= {1,2,2,3,4,"Hi","Hello"}
#set ignore duplicate values and have no order

print(collection)
print(type(collection))
print(len(collection))

collection.add("ab")
print(collection)

collection.remove("ab")
print(collection)

collection.clear()
print(collection)
print(len(collection))

set1={1,2,3,5,7,9,3}
set2={2,3,5,7}

print(set1.union(set2))
print(set1.intersection(set2))