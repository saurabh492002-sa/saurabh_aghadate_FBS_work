# 2. Python Program to Concatenate Two Dictionaries Into One

a = {"name": "Saurabh", "age": 24}
b = {"city": "Pune", "course": "AI"}
c = {}

for i in a:
    c[i] = a[i]

for i in b:
    c[i] = b[i]

print(c)