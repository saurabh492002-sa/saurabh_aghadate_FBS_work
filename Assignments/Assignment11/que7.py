# 7. Python Program to Find the Intersection of Two Lists



li1 = [10, 20, 30, 40, 50]
li2 = [20, 30, 40]
intersection = []

for ind in range(0, len(li1)):
    # print(li1[ind])
    for j in range(0, len(li2)):
        if li1[ind] == li2[j]:
            intersection += [li1[ind]]

print(intersection)
