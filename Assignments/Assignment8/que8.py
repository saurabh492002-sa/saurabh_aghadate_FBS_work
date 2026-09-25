# 8. Write a program find reverse of a number.


def reverseNo():
    n = int(input("Enter the number :"))

    rev = 0 

    while (n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    return rev

res = reverseNo()
print(f"Reverse of a number is : {res}")