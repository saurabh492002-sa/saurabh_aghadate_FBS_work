# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.


no = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input("Entr the number : "))

for i in range(len(no)):
    for j in range(i + 1, len(no)):
        for s in range(j + 1, len(no)):

            if no[i] + no[j] + no[s] == target:
                print(no[i], no[j], no[s])