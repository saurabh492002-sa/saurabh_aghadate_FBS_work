# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the Python set.


numbers = [2, 5, 3, 8, 6]

num_set = set(numbers)

max_product = 0
num1 = 0
num2 = 0

for i in num_set:
    for j in num_set:
        if i != j:
            product = i * j

            if product > max_product:
                max_product = product
                num1 = i
                num2 = j

print("Numbers:", num1, num2)
print("Maximum Product:", max_product)