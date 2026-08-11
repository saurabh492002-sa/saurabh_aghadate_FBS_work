# 2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)


p = int(input("Enter the Principal : "))
r = int(input("Enter the Rate : "))
t = int(input("Enter the Time : "))

si = (p * t * r) / 100

print(f"Simple Interest is : {si}")