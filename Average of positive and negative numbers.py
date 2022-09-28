positive_num=0
no_positive_num=0
negative_num=0
no_negative_num=0
arr=[]
total=0
print("Enter -1 for exit")
while(arr!=-1):
    arr=int(input("Give elemets- "))
    if(arr==-1):
        print("end of program")
        break
    if(arr==0):
        print("Neither positive or negative")
    elif(arr>0):
        positive_num=positive_num+arr
        no_positive_num+=1
        avg=positive_num/no_positive_num
    else:
        negative_num=negative_num+arr
        no_negative_num+=1
        avgneg=negative_num/no_negative_num
        
print("average for Positive ",avg)
print("Average for negative ",avgneg)
