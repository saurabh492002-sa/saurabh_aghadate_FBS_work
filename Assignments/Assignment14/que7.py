# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

miss1 = set()
miss2 = set()

for i in set1:
    if i not in set2:
        miss1.add(i)

for i in set2:
    if i not in set1:
        miss2.add(i)

print("Missing in set2", miss2)
print("Missing in set1", miss1)