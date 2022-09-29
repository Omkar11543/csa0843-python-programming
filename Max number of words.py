def max_words(my_list):
    max=0
    empty=[]
    for i in my_list:
        current=len(i.split(' '))
        if(current>max):
            max=current
    return max
listofsentences=[]
sizeoflist=int(input("may i know the size of list:"))
print("start entering sentences limit is:",sizeoflist)
for i in range(1,sizeoflist+1):
  newsentence=input()
listofsentences.append(newsentence)
print("the sentence with max words that are:",max_words(listofsentences))
