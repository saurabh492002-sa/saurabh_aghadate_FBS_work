# 3. Python Program to Detect if Two Strings are Anagrams

# a = "listen"
# b = "silent"
a = input("Enter the first string. : ")
b = input("Enter the second string. : ")

if len(a) != len(b):
    print("Not Anagram")
else:
    count = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count += 1
                break

    if count == len(a):
        print("Anagram")
    else:
        print("Not Anagram")