Num=float(input("Enter the starting number:"))
Secondnumber=int(input("Max number of line printed:"))
for i in range(Secondnumber):
    for j in range(i+1):
        print('%.1f'%Num,end=" ")
        Num=Num+0.1
    print()
