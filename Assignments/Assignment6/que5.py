


for i in range(1,6):
    for j in range(1, 6 - i):
        print(" ", end = " ")
    # print()

    for j in range(1, i + 1):
        print("*", end = " ")
    # print()

    k = i + 1

    for j in range(1, i):
        print("*", end = " ")
        k += 1

    print() 


# for i in range (1,6):
#     for j in range (1, 6 - i):
#         print (" ", end = " ")

#     for j in range (1, i + 1):
#         print ("*", end = " ")


#     k = i + 1

#     for j in range (1, i):
#         print ("*", end = " ")
#         k += 1

#     print()