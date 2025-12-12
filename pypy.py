mylist = ["a", "b", "c", "d", "d", "a"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

def my_function(x):
    return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "c", "d", "d", "a"])
print(mylist)