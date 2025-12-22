import sys

name = "Tutorials point"
print("Initial reference count: ", sys.getrefcount(name))


other_name = "Tutorials point"
print("Reference count after assignment:", sys.getrefcount(name))

string_sum = name + 'Python'
print("Reference count after concentration:", sys.getrefcount(name))

list_of_names = [name, name, name]
print("Reference count after creating a list with 'name' three times:", sys.getrefcount(name))

del other_name 
print("Reference count after deleting 'other name':", sys.getrefcount(name))

del list_of_names
print("Reference count after deleting the list;", sys.getrefcount(name))