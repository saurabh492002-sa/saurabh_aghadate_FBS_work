# Convert temp from Celsius to Fahrenheit. (c/5 = (F-32)/9)

celsius = float(input("Enter The Temperature :"))

fahrenheit = (9 / 5 * celsius) + 32

print(f"Fahrenheit is : {fahrenheit} C")