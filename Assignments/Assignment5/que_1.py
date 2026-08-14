# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


# userid = ("Saurabh@123")
# pas = ("1234")


for i in range(1,4):

    userid = ("Saurabh123")
    pas = 1234

    id = input("Enter the UserID :")
    password = int(input("Enter the password :"))

    if id == userid:
        print("Congratulation your Login Sucess")
        break
    
    else:
        print("Login Fail \nYou entered wrong UserID and Password") 
        # print("Try Again...")

else:
    print("You login... Multiple time plese try After some time")