
# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

 

li = [ 10, 20, 30, 40]
li2 = []

for i in li:
    li2 += [i]

print(li)
print(li2)