# 8. Write a program to check whether a number is prime or not using recursion.



def check_prime(n, i=1, count=0):

    if i <= n:

        if n % i == 0:
            count += 1

        return check_prime(n, i + 1, count)

    return count


n = int(input("Enter the number : "))

count = check_prime(n)

if count == 2:
    print("True")
else:
    print("False")

# n = 8
# count = 0

# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
# # print(count)
#     else:
#         pass

# if count == 2:
#     print("True")
# else:
#     print("False")
        
    