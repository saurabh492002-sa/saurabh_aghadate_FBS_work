# WAP to check if given number is prime number or not.
# suppose 23


num = int(input("Enter the number : "))

if num > 1:
    for i in range(2,num // 2 + 1):
        print(i)
        if num % i == 0:
            print(f"{num} is not prime number.")
            break
    else:
        print(f"{num} is prime number.")


else:
    print(f"{num} is negetive number.")


# num = int(input("Enter the number : "))
# # num = 23

# if num > 1:

#     for i in range (2, num // 2 + 1):
#         print(i)
#         if num % i == 0:
#             print(f"{num} is not prime number")
#             break
#     else:
#         print(f"{num} is prime number")

# else:
#     print (f"{num} is not prime number")