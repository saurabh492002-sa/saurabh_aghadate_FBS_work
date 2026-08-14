# 6. Write a program to print first n prime numbers.


n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2

while count < n:

    factor = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1

    if factor == 2:
        print(num)
        count += 1

    num += 1