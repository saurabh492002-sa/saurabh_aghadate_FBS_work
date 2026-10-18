# 14. Python Program to count the occurrences of ach word in a string.

a = input("Enter the string : ")

words = []
word = ""

for i in a:
    if i == " ":
        words.append(word)
        word = ""
    else:
        word += i

words.append(word)

for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count += 1

    already = False

    for k in range(i):
        if words[i] == words[k]:
            already = True

    if already == False:
        print(words[i], ":", count)