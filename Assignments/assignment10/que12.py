# 12. Write a program to create three lists of numbers, their squares
# and cubes


li = [1,2,3,4,5]
squares = []
cubes = []

for i in li:
    squares += [i * i]
    cubes += [i * i * i]

print(f"Your List : {li}")

print(f"List Squares : {squares}")

print(f"List Cubes : {cubes}")