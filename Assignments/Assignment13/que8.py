# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary


a = input("Enter a string : ")
dic = {}

words = a.split()

for i in words:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)