def diff_position(string1,string2):
	A=string1.replace('  ',' ')
	B=string2.replace('  ',' ')
	if(len(A)<len(B)):
		length=len(A)
	else:
		length=len(B)
	count=0
	for i in range(length):
		if(A[i]!=B[i]):
			count=count+1
	print(length-count)
string1=str(input("string1="))
string2=str(input("string2="))
diff_position(string1,string2)
