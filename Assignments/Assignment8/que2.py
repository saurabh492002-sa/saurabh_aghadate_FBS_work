# 2. Write a program to calculate area of circle


def areaCircle():
    return 3.14 * (r ** 2)

r = int(input("Enter the radius : "))

res = areaCircle()
print(f"Area of circle is : {res}")