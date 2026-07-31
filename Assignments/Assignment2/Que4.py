# WAP to calculate area of triangle and rectangle
# area of triangle = (base × height) / 2
# Area of Rectangle = Length × Width


height = int(input("Enter the Triangle Height :"))
base = int(input("Enter the Triangle Base :"))
# height = int(input("Enter the Triangle Height :"))
area_triangle = (base * height) / 2

print(f"The Area of Triangle is : {area_triangle}")

length = int(input("Enter the Length of Rectangle :"))
width = int(input("Enter the Width of Rectangle :"))
area_rectangle = length * width

print(f"The Area of Rectangle is : {area_rectangle}")

print(f"The Area of Triangle is : {area_triangle} and The Area of Rectangle is : {area_rectangle}")