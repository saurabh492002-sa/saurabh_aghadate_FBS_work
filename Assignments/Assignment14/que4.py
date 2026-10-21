# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.


a = [2, 4, 3, 5, 7, 8]

target = int(input("Enter the value : "))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], a[j])