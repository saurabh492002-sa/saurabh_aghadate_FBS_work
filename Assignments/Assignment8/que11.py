# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.


def countDigits(n):
    count = 0

    while n > 0:
        count += 1
        n = n // 10

    return count


def calculateSum(n, count):
    sum = 0

    while n > 0:
        d = n % 10
        sum += d ** count
        n = n // 10

    return sum


def checkArmstrong(original, sum):
    if original == sum:
        return True
    else:
        return False


n = int(input("Enter the number : "))

count = countDigits(n)
sum = calculateSum(n, count)
result = checkArmstrong(n, sum)

if result:
    print(f"{n} is Armstrong number")
else:
    print(f"{n} is not Armstrong number")