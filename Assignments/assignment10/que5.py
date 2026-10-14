# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


li = [10, 22, 67, 42, 97, 32, 84, 12, 67]
n = int(input("Enter the number : "))

count = 0
for ind in range(len(li)):
    # print(li[ind])
    if n == li[ind]:
        count += 1

if count > 0:
    print(f"{n} is present in list.")
    print(f"{count} time present")
else:
    print(f"{n} is not present in list.")