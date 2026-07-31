# WAP to check if given number Strong Number.
# sum of factorial is == number


num = int(input("Enter the number : "))


sum = 0
temp = num

while(temp > 0):
    digit = temp % 10   #Take the last digit
    # print(digit)

    fact = 1

    for i in range(1, digit + 1):
        fact *= i
        # print(fact)

    sum += fact    #Add the factorial to the total
    temp //= 10    #Remove the last digit


if num == sum:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not strong number.")








