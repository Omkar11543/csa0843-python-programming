firstlist=[1,2,4]
secondlist=[1,3,4]
result=[]
i,j=0,0

while i<len(firstlist)and j<len(secondlist):
    if firstlist[i]<secondlist[j]:
        result.append(firstlist[i])
        i=i+1
    else:
        result.append(secondlist[j])
        j=j+1
result=result+firstlist[i:]+secondlist[j:]
print("sorted list:"+str(result))
        
    
