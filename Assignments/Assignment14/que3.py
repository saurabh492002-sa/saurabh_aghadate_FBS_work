# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set data type.

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_words = set()

for i in words:
    unique_words.add(i)

print("Unique words:", unique_words)

for i in unique_words:
    count = 0

    for j in words:
        if i == j:
            count += 1

    print(i, ":", count)