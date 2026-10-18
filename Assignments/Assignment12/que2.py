# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String


n = 6
# p = "Pythonn"
p = str(input("Enter the string..."))
new = ""

for i in range(len(p)):
    if i == n:
        continue
    else:
        new += p[i]


print(f"Your String : {p}")
print(f"New String : {new}")


