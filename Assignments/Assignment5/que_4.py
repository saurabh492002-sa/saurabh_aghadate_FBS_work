# 4. WAP to print Armstrong number within a given range 

num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

for i in range(num1, num2 + 1):

    temp = i
    sum = 0
    count = 0

    while(temp > 0):
        count += 1
        temp //= 10

    temp = i

    while(temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp //= 10

    if(i == sum):
        print(i)