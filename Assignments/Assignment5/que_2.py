# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


no_student = int(input("Enter the number of students : "))

sum_percentage = 0

for i in range(1, no_student + 1):

    m1 = int(input("Enter the the 1st sub marks. : "))
    m2 = int(input("Enter the the 2st sub marks. : "))
    m3 = int(input("Enter the the 3st sub marks. : "))
    m4 = int(input("Enter the the 4st sub marks. : "))
    m5 = int(input("Enter the the 5st sub marks. : "))

    obtain = m1 + m2 + m3 + m4 + m5
    total = 500

    percentage = obtain / total * 100
    sum_percentage += percentage

    print(f"Total Percentage is {percentage}")

avarage = sum_percentage / no_student

print(f"Avarage is {avarage}")


