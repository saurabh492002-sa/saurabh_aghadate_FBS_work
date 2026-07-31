# Convert the time entered in hh, min and sec into seconds.

hour = int(input("Enter Hour : "))
minute = int(input("Enter Minute : "))
second = int(input("Enter second : "))

hours = hour * 3600
minutes = minute * 60
seconds = second

total_sec = hours + minutes + seconds

print (f"Your Total Second is : {total_sec}")