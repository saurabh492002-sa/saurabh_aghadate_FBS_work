# 5. Write a program to print prime numbers between 1 to 100.
# Suppose 23, 17

# count = 0

for i in range (2,100 + 1):

    count = 0

    for div in range(1,100):

        if i % div == 0:
            count += 1

    if count == 2:
        print(i)