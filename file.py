# f = open('C:\\GrowthHungry\\GH\\text.txt', 'r', encoding='utf-8')
# for line in f:
#     print(line, end="")
#
# f.close()

# f = open("C:\\GrowthHungry\GH\text.txt")
# print(f.readlines())
# f.close()
#
# f = open('C:\\GrowthHungry\\GH\\text.txt', 'r', encoding='utf-8')
# for line in f:
#     print(line, end="")
# f.close()

# file = open("text.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("C:\GrowthHungry\GH\text.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# file = open("text.txt", "r")
# content = file.read()
# print(content)
# file.close()
#
# with open("C:\\GrowthHungry\\GH\\text.txt", "r") as f:
#     print(f.read())

# with open(r"C:\GrowthHungry\GRowthHunger\text.txt", "r") as f:
#     print(f.read())
# import os
# print(os.getcwd())

# here we can learn that how to open the file
file = open("texts.txt","r")
contents = file.read()
print(contents)
file.close()

# the next task is how to write in file

with open("texts.txt","a") as file:
    contents = "Now the file has more contents"
    file.write(contents)

with open("texts.txt","r") as file:
    print(file.read())

# ok allright so there are one more interesting function like create a file
# lets try that one too

# file = open("newtext.txt","x")

#alright this done

# the next thing that we need to learn is how ot delete that file
#this also the simple looks like

import os
os.remove("newtext.txt")
# yeah it deletes
