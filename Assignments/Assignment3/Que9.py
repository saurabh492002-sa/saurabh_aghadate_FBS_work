# Input 5 Subject marks from user and display grade(eg. First class, Second class ..)



sub1 = int(input("Enter the first subject marks : "))
sub2 = int(input("Enter the second subject marks : "))
sub3 = int(input("Enter the third subject marks : "))
sub4 = int(input("Enter the fourth subject marks : "))
sub5 = int(input("Enter the fifth subject marks : "))

total = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total / 500) * 100

if percentage >= 35:
    if percentage >= 50:
        if percentage >= 70:
            if percentage >= 85:
                print("Class A")
            else:
                print("Class A")
        else:
            ("Class B")
    else:
        print("Class C")
else:
    print("Your are Fail...")


 
