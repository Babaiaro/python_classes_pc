# so as named this page for nested dictionaries
# as we have learn before there were classes like child and parent which are consists types of list in them

# this is like we can call create the dictionaries that contains dicitonanries

my_list_cars = {
    "toyota" : {
        "name": "Toyota",
        "brand": "supra",
        "year": 1999
    },
    "Mersedez":{
        "name": "Mersedes",
        "model": "s500",
        "year": 1995
        "color":"green"

    },
    "BMW":{
        "name": "BMW",
        "model": "M5",
        "year": 2015
    },
    "Tesla":{
        "name": "Tesla",
        "model": "Cybertruck",
        "year": 2025
    }
}

# or there are different type that it like first create a dic then add them to the dic

Freighliner={
    "name": "Freighliner",
    "model":"Cascadia",
    "year": 2025
}

Volvo = {
    "name": "Volvo",
    "model": "Vnl 860",
    "year": 2025
}

Kenworth = {
    "name": "Kenworth",
    "model": "T860",
    "year": 2025
}

myCompany = {
    "Freight" : Freighliner,
    "Volvo" : Volvo,
    "Kenworth" : Kenworth,
}
print(myCompany["Volvo"]["model"])

# ok here a loop dic

for x, object in myCompany.items():
    print(x)
    # Freight
    # Volvo
    # Kenworth this is how it prints

for z in object:

    print(z + ":", object[z])
