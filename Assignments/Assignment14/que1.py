# 1. Write a Python program to find elements in a given set that are not in another set.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

result = set()

for i in a:
    if i not in b:
        result.add(i)

print("Element thats not in another set : ", result)