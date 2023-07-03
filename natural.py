                       #This code is done by Thiruselvan E
 #The program to find sum of Natural Numbers using recursion in python. Ex:N is 5 then sum=1+2+3+4+5.

def Natural_number(N):
    if(N!=0):
        return N+Natural_number(N-1)           #recursion is used here so it recurse the  code until N becomes 0.
    else:
        return False
    
N=int(input())
result=Natural_number(N)                #funtion call
print(result)