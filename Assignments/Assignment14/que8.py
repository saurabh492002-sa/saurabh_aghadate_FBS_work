# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = []

for word in words:

    found = False

    for group in groups:

        first = group[0]

        if len(word) == len(first):

            count1 = {}
            count2 = {}

            for i in word:
                if i in count1:
                    count1[i] += 1
                else:
                    count1[i] = 1

            for i in first:
                if i in count2:
                    count2[i] += 1
                else:
                    count2[i] = 1

            if count1 == count2:
                group.append(word)
                found = True
                break

    if found == False:
        groups.append([word])

print(groups)