# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


# a. 1+ 2 + 3 + 4+..... + n

def sumSeries():

    n = int(input("Enter the number : "))

    sum = 0

    for i in range(1,n+1):
        sum += i
    return sum

res = sumSeries()
print(f"The sum of series is : {res}")




# b. 1!+ 2! + 3! + 4!+..... + n!


def sumFact():
    sum = 0
    fact = 1

    n = int(input("Enter the number : "))

    for i in range(1, n + 1):
        fact *= i
        sum += fact
    return sum

res = sumFact()
print(f"Sum of factorial of series is : {res}")

 


# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumPower():
    sum = 0
    power = 1
    n = int(input("Enter the number : "))

    for i in range(1, n + 1):
        power = i**i
        sum += power
    return sum

res = sumPower()
print(f"Sum of series is : {res}")