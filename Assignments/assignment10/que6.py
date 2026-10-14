# 6. Write a program to remove duplicates from the list.

li = [10, 22, 67, 42, 97, 22, 32, 84, 12, 67]
new_li = []

for i in li:
    found = 0
    for j in new_li:
        if i == j:
            found = 1

    if found == 0:
        new_li += [i]

print(new_li)