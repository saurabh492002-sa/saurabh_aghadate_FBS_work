# 6. Python Program to Multiply All the Items in a Dictionary


dic = {"a" : 3, "b" : 2, "c" : 1, "d" : 5}

mul = 1

for i in dic:
    mul *= dic[i]

print("Multiplication of all items is : ", mul)