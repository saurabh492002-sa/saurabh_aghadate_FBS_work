# 9. Write a program to check if entered number is a palindrome or not.


def checkPalindrome():

    n = int(input("Enter the number : "))
    store = n

    rev = 0 

    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    # print(rev)

    if store == rev:
        print("True")
    else:
        print("False")

checkPalindrome()
