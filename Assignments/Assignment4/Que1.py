# WAP to print all even numbers unitl n.

num = int(input("Enter the number : "))

i = 2

while(i <= num):
    print(i)
    i += 2

# for i in range(2,num+1,2):
#     print(i, end = " ")
# print()








 


# check the number is Armstrong or not
# Armstrong number is a number that is equal to the sum of the cubes of its digit

# no = int(input("Enter the number you want to check : "))

# count = len(str(no))
# temp = no
# total = 0

# while no > 0:
#     d = no % 10
#     total = total + (d**count)
#     no = no // 10
# print(total)
# if no == temp:
#     print("The number is Armstrong")
# else:
#     print("The number is not Armstrong")


# give user input start range and end range and print odd no.

# start = int(input("Enter the starting range :"))
# end = int(input("Enter the ending range :"))

# for i in range(start,end):
#     if i % 2 != 0:
#         print(i)

# WAP to print even no using user input in range start and end

# start = int(input("Enter starting range : "))
# end = int(input("Enter ending range : "))

# for i in range(start,end):
#     if i % 2 == 0:
#         print(i)