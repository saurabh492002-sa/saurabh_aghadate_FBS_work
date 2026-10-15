# 3. Python Program to Sort the List According to the Second Element in Sublist

# li = [10, 20, [30, [40, 50],60],70, 80]

# print(li[1])
# print(li[2][0])
# print(li[2][1][0])


li = [[1, 50], [2, 20], [3, 40], [4, 10]]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i][1] > li[j][1]:
            li[i], li[j] = li[j], li[i]

print(li)