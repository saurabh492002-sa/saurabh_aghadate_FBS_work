# WAP to check if person is eligible to marry or not (male age >= 21 and female age >= 18)


gender = input("Enter the Gender : (m/f) = ")
age = int(input("Enter the Age : "))

if gender == "m":
    if age >= 21:
        print("Boy eligible for marrage")
    else:
        print("Opps.. Bor are not eligible for marrage")
else:
    if age >= 18:
        print("Girl eligible for marrage")
    else:
        print("Opps.. Girl not eligible for marrage")
