# 5. Sum of all prime numbers between 1 to n.


n = int(input("Enter the number : "))

def primeNo(n):
    sum = 0
    for i in range(2, n + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            sum += i

    return sum

res = primeNo(n)
print("Sum of prime number is:", res)


# n = int(input("Enter the number : "))
# sum = 0
# for i in range(2, n + 1):
#     count = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1

#     if count == 2:
#         sum += i
# print(f"Sum of prime number is {sum}")
