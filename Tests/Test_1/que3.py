# 3. Write a program to accept distance in km and convert it into meters and
# centimeters both.

distance = float(input("Enter the Distance in km : "))

meters = distance * 1000
centimeters = distance * 100000

print(f"Distance = {distance}km, Meters = {meters}, Centimeters = {centimeters}")
