# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = "FirstBit Soluation"
new_str = ""

for i in str:
    if i == "a":
        new_str += "$"
    else:
        new_str += i
print(new_str)