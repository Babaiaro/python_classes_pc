# list comprehensions

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_length = []
for word in words:
    if word != "the":
        word_length.append(len(word))

print(word_length)
print(words)
print(words)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_length = [len(word) for word in words if word != "the"]
print(word_length)
print(words)

numbers = [34.5, -2.35, 542.554, -445.25, 5454, -2542, 5454]
newlist = [int(num) for num in numbers if num > 0]
print(newlist)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)



