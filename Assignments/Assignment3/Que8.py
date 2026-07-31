# Wrire a program to prompt user has entered correct userID and password.
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed. (Something like captcha)


import random

userid = input("Enter the User_Id : ")
password = input("Enter the Password : ")

if userid == "saurabh" and password == "sa@2002":
    captcha = random.randint(1000,9999)
    print(f"Your Captcha is {captcha}")
    user  = int(input("Enter Your Captcha :"))
    if user == captcha:
        print("User Login Successfully...")
    else:
        print("Opps Invalid Captcha...")
else:
    print("User is Invalid")