# in this time we use a remove items for discitonaries

# as we did it looks like the same that is used .pop and some new lke del and .clear

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)

#this .pop() is typically removes item which are specifically key names


# there are one more interesting thing that .popitem() is removes the last inserted item to dic

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# as we see in terminal that {'brand': 'Ford', 'model': 'Mustang'} there are year has been disappeared


# the next one is that del. yeah this uses for specifiacally for the key name ;like as pop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# thia also able to delete dic completely

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)

# for to empty the dictinary we can use .clear

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)


# so there are one of my favourite is that loop the dic
# berfore i have used this one but i could not identify that i is dic

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:

    print(x)

    # is shows that all key names in dic

# and there are one more fun thing is pritn all values in dic
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(thisdict[x])


# so there are we could also return the values with .values()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.values():
    print(x)

# so with this we have finished the loop

# and then next are copy dic
# there are method that we can copy
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964

}

mydict = thisdict.copy()
print(mydict)

# so them there are only two types looks like that .copy() and then dict()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)