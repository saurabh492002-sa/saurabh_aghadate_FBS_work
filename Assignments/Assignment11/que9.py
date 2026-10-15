# 9. Write a program to create three lists of numbers, their squares and cubes

li = [1,2,3,4,5,6]
square_li = []
cubes_li = []

for i in li:
    # print(i)
    square = [i * i]
    square_li += square

    cube = [i ** 3]
    cubes_li += cube

print(li)
print(square_li)
print(cubes_li)
