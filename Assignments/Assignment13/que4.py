# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).


a = int(input("Enter the number. : "))

dic = {}

for i in range(1, a + 1):
    dic[i] = i * i

print(dic)