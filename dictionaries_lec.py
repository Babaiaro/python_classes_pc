phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938477564
phonebook["Jill"] = 938477475
print(phonebook)

phonebook = {
    "John": 938477566,
    "Jack": 938477475,
    "Jill": 938477475
}
print(phonebook)

phonebook = {"John": 938477566, "Jack": 938477475, "Jill": 938477475}
for name, number in phonebook.items():
    print("Phone number of %s id %d" % (name, number))

phonebook = {
    "John": 938477475,
    "Jack": 938477475,
    "Jill": 938477475
}
del phonebook["Jill"]
print(phonebook)


phonebook = {
    "John": 938477475,
    "Jack": 938477475,
    "Jill": 938477475
}
phonebook.pop("Jill")
print(phonebook)
print(phonebook)


