# WAP to calculate total salary of employee based on basic, da = 10% of basic, ta = 12% of basic, hra = 15% of basic.


salary = int(input("Enter Salary :"))

da = salary * 10 / 100

ta = salary * 12 / 100

hra = salary * 15 / 100
       
total_salary = da + ta + hra + salary

print(f"Total Salary is : {total_salary}")

