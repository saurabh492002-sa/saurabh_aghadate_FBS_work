# WAP to check whether the triangle is equilateral, isosceles or scalene triangle.
# equilateral = 3 side are same (a=b=c)
# isosceles = 2 side same 1 diff (a=b or a=c or b=c)
# scalene = 3 are diff (a!=b, a!=c and B!=c)


side1 = int(input("Enter the first side of triangle = "))
side2 = int(input("Enter the second side of triangle = "))
side3 = int(input("Enter the third side of triangle = "))


if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")




