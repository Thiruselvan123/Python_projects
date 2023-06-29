           #To find prime number or not using functions#
def prime_number(N,flag):        #fuction defintion 
    for i in range(2,N):         #reason we choose 2 is bcoz 1 is neiher prime nor composite
        if(N%i==0):              #check whether the number is a divided with other factor.
            flag=1
    return flag



N=int(input("Enter a Number"))
flag=0
result=prime_number(N,flag)
if(N==1):
    print("1 is neither prime nor composite")
elif(result==0):
    print(f"{N} is a prime number")
else:
     print(f"{N} is not a  prime number")
