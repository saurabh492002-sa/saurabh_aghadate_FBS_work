# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.


li = [2, 3, 4, 5, 6, 7]
new_li = []

for ind in range(len(li)):
    cube = li[ind] ** 3
    new_li += [cube]

print(f"Your list is : {li}")
print(f"New list is : {new_li}")