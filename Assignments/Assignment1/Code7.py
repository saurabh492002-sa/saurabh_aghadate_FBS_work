#  Program to find the Roots of Quadratic Equation

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b**2 - 4*a*c

root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)

print("Root 1 =", root1)
print("Root 2 =", root2)