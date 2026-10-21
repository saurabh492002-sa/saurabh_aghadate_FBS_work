# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

words = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(words[0])):

    chars = set()

    for word in words:
        if i < len(word):
            chars.add(word[i])

    if len(chars) == 1:
        prefix += words[0][i]
    else:
        break

print("Longest common prefix:", prefix)