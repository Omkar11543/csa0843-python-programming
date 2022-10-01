m=int(input("enter the first value"))
n=int(input("enterthe second value"))
for number in range(m,n+1):
    factor=0
    for i in range(1,number):
        if number%i==0:
            factor=i
        
            print(number)
