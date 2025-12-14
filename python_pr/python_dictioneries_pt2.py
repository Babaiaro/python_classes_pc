# in this today we cover change items in dictioneries in python

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 2020
print(thisdict)

# as we see in terminal that it changes the value of key on print
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020} like this.
# even there are in list is different and we change it it is gonna be different

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# here we use it like update
# but asa we see that there is no red lights under list

# so this is that for changing 
