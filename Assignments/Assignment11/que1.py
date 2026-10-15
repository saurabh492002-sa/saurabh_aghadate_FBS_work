# 1. Python Program to Put Even and Odd  element of a list into two Different List.


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Even = []
Odd = []

for i in li:
    # print(i)
    if i % 2 == 0:
        Even += [i]
    else:
        Odd += [i]

print(f"Your List is : {li} \nYour Even list is : {Even} \nYour Odd list is {Odd}")


# def evenOdd(li):
#     Even = []
#     Odd = []

#     for i in li:
#         if i % 2 == 0:
#             Even += [i]
#         else:
#             Odd += [i]

#     return Even, Odd


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Even, Odd = evenOdd(li)

# print(f"Your List is : {li}")
# print(f"Your Even list is : {Even}")
# print(f"Your Odd list is : {Odd}")