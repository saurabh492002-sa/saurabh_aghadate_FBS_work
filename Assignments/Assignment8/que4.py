# # 4. Sum of all odd numbers between 1 to n

def sumOdd(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            # print(i)
            sum += i
    return sum

n = int(input("Enter the number : "))

res = sumOdd(n)
print(f"Sum of all odd number between 1 to {n} is : {res}")
