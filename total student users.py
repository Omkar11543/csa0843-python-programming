total=int(input("enter the total users"))
if(total<=0):
    print("value error")
    exit()
staff=int(input("enter the total staff users "))
if(staff<=0):
    print("value error")
    exit()
a=staff/3
stud=total-staff-a
print("the total student users are",stud)
