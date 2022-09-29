X=int(input("enter the first number"))
Y=int(input("enter the second number"))
Z=int(input("enter the third number"))
l=[]
l.append(X)
l.append(Y)
l.append(Z)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print("the combination number is ",l[i],l[j],l[k]) 
