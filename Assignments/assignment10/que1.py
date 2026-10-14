# 1. Write a program to find sum of all elements of list


li = [10,20,30,40,50]

sum = 0
for ind in range(0, len(li)):
    # print(li[ind])
    sum += li[ind]
print(f"Your list : {li}")
print(f"Sum of all element in the list : {sum}")


