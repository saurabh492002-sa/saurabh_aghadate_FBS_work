# WAP to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)


num = int(input("Enter the number : "))

temp = num
sum = 0
count = 0

while(temp > 0):
    count += 1
    temp //= 10
# print(count)

temp = num

while(temp > 0):
    digit = temp % 10
    # sum = sum + digit ** count
    sum += digit ** count
    temp //= 10

if(num == sum):
    print(f"{num} is Armstrong number.")
else:
    print(f"{num} is not Armstrong number.")