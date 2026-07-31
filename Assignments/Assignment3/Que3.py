# WAP to input angles of a triangle and check whether triangle is valid or not.
# Logic (angle1 + angle2 + angle3 == 180)


angle1 = int(input("Enter a 1st angle of triangle : "))
angle2 = int(input("Enter a 2st angle of triangle : "))
angle3 = int(input("Enter a 3st angle of triangle : "))

if angle1 + angle2 + angle3 == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

