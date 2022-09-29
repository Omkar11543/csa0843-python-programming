M=int(input("enter the starting number"))
N=int(input("enter the ending number"))
K=int(input("enter the number should be skipped between M and N"))
if(M>N or M<0 or N<0 or  K<0 or M==N):
    print("invalid input")
else:
    for i in range(M,N+1,K+1):
        print(i)
