# 2. Python Program to Merge Two list and sort it.

li1 = [20, 45, 76]
li2 = [12, 87, 31]

li3 = li1 + li2
# print(li3)

for i in range(len(li3)):
    for j in range(i + 1, len(li3)):
        if li3[i] > li3[j]:
            li3[i], li3[j] = li3[j], li3[i]

print(li3)