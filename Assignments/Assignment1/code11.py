# Find the area and circumference of circle.
# Area = 3.14r**2
# (c**2) / (4 * 3.14)

radius = float(input("Enter the Radius :"))

area = 3.14 * (radius**2)

circumference = 2 * 3.14 * radius

print(f"Area of Circle is : {area:.2f} and Circumference of Circle is {circumference:.2f}")