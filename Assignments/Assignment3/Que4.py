# WAP to input all sides of a triangle and check whether triangle is valid or not.
# Logic - sum of the length of two sides is strictly greater than the lenth of third side.

side1 = int(input("Enter the first side of triangle = "))
side2 = int(input("Enter the second side of triangle = "))
side3 = int(input("Enter the third side of triangle = "))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("Triangle is valid")
else:
    print("Invalid Triangle")