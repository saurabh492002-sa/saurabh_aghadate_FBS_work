# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.


li = [1,2,3,4,5,6,7,8,9,10]
odd_li = []
even_li = []

for ind in range(len(li)):
    # print(li[ind])
    if li[ind] % 2 == 0:
        even_li += [li[ind]]
    else:
        odd_li += [li[ind]]

print(f"Odd list is : {odd_li}")
print(f"Even list is : {even_li}")
