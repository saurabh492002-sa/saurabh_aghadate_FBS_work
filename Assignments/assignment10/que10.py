# # 10. Write a program to remove all occurrences of a given element in the list.


li = [10, 20, 10, 30, 40, 20]

new_li = []

element = int(input("Enter the element : "))

for i in li:
    if i != element:
        new_li += [i]

print(new_li)

 