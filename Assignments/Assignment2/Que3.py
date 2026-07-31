# Convert distant given in feet and inches into meter and centimeter.
# 1 foot (ft) = 0.3048 meter (m)
# 1 inch (in) = 2.54 centimeters (cm)

feet = int(input("Enter the Feet :"))
inches = int(input("Enter the Inches :"))

meter = feet * 0.3048

centimeter = inches * 2.54

print(f"Feet into Meter = {meter} and Inches into Centimeter = {centimeter}")
