# 11. Write a program to print all numbers which are divisible by m and n in the
# list.


li = [10, 18, 12, 20, 14, 15, 16, 22]
li2 = []

m = int(input("Enter the number :"))
n = int(input("Enter the number : "))
for i in li:
    if i % m == 0 and i % n == 0:
        li2 += [i]
        print(i)
print(li2)