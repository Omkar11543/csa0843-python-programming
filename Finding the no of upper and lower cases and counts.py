UP=0
LW=0
count=0
arr=[]
print("Enter * to quit")
while(arr!='*'):
    arr=input("Enter the element= ")
    if(arr>='A' and arr<='Z'):
        UP+=1
    elif(arr>='a' and arr<='z'):
        LW+=1
    elif(arr>='0' and arr<='9'):
        count+=1
    if(arr=='!' and arr=='@' and arr=='#' and arr=='$' and arr=='%' and arr=='^' and arr=='&' and arr=='(' and arr==')' and arr=='_' and arr=='-' and arr=='+' and arr=='=' and arr=='~' and arr=='`'):
        print("SPECIAL CHARACTERS ARE NOT ALLOWDED")
        exit()
print("Number of upper case=",UP)
print("Number of lower case= ",LW)
print("Number of numbers= ",count)
