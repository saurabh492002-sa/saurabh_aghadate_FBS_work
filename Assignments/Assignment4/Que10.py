# WAP to check if given number is Perfect Number.
# suppose 6 = 1 + 2 + 3 = 6

num = int(input("Enter the number : "))

sum = 0

for i in range(1, num // 2 + 1):
    if num % i == 0:
        sum += i
if sum == num:
    print(f"{num} is perfect number")
        # print(i)
else:
    print(f"{num} is not perfect number")
# print(sum)
    
