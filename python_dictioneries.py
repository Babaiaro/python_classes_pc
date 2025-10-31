thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# this is just a dictionary with curly bracets and key and value there

# here we would choose one item in dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["model"])
# here we can also like to check the lenght of dictionary too
print(len(thisdict))
# this is how we can choose item in dictionary
# as we said before it if the key for that value to choose

# also there are we have one more interesting topic that it is not possible to duplicate a key

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "year": 2020,
# }
# print(thisdict)


# next is there are we can create a data type for ex. model: S Y Cyber

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ["red", "blue", "green"]
}
print(type(thisdict))

# also we can use dictionary with round bracket too.
thisdict = dict(name = "Bob", age = "20", country = "United States")
print(thisdict)

# SOO access dictionary items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = thisdict.get("model")
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,

}
x= car.keys()
# as we see if we call .keys it can get key that we use on dict
print(x)

car["Color"] = "red"
print(x)

# the same with value
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,

}
x= car.values()
# as we see if we call .keys it can get key that we use on dict
print(x)

car["year"] = "2020"
print(x)
