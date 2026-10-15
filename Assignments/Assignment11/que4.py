# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

 

def bubbleSort(li):

    for i in range(1, len(li)):
        for j in range(0, len(li) - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


li = [30, 20, 70, 60, 80, 20, 90]

print(f"Before sorting : {li}")
bubbleSort(li)
print(f"After sorting : {li}")
print(f"Second Largest : {li[-2]}")