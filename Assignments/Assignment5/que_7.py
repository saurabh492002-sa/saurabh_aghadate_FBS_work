# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

# a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter the number : "))

sum = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += fact
print("Sum : ", sum)



# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

# Method 1

n = int(input("Enter the number : "))
sum = 0
for i in range(1, n + 1):
    power = 1
    for j in range(1, i + 1):
        power *= n
    sum += power
print("Sum = ", sum)

n = int(input("Enter the number : "))

# Method 2

sum = 0
for i in range(1, n + 1):
    sum += n ** i

print("Sum = ", sum)


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter the number of terms: "))

sum = 0
term = 1

for i in range(1, n + 1):
    sum += term
    term *= 2

print("Sum =", sum)
    # print(i)


# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter the number : "))

sum = 0

for i in range(1, 11):
    res = (a ** i) / i
    sum += res

print("Sum : ", sum)


# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
# x is the number entered by the user.
# n is the number of terms to calculate.

x = int(input("Enter the number : "))
n = int(input("Enter the number : "))

sum = 0

for i in range(1, n + 1):
    res = (x ** i) / (2 * i - 1)

    if i % 2 == 0:
        sum -= res
    else:
        sum += res

print(sum)

