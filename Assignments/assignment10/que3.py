# 3. Write a program to find the second largest element in the list.


li = [14,52,74,64,14,86,75,47]

max = li[0]
second_max = li[0]
for ind in range(1, len(li)):
    if max < li[ind]:
        max = li[ind]
        max = li[ind]
    elif li[ind] > second_max and li[ind] != max:
        second_max = li[ind]

print(f"Second max element is : {second_max}")