# WAP to print all numbers in a range divisible by a given number.



num = int(input("Enter the number : "))

for i in range (1, num+1):
    if num % i == 0:
        print(i, end = " ")
print()