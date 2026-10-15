# 6. Python Program to Find the Union of two Lists

li1 = [ 10, 30, 20]
li2 = [ 50, 40, 30]
union = []




for i in range(0, len(li1)):
    union += [li1[i]]

for i in range(0, len(li2)):
    found = 0

    for j in range(0, len(li2)):
        if li2[i] == union[j]:
            found = 1

    if found == 0:
        union += [li2[i]]

print(f"Union of Both list : {union}")