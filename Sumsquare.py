list=[1,2,3,4,5]

def sumsquare(list):
  odd=0
  even=0
  for i in list:
     if i%2==0:
            even=even+i**2
     else:
        odd=odd+i**2
  list=[odd,even]
  return(list)
print(sumsquare(list))
