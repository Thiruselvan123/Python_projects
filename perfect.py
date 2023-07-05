N=int(input("Enter the number : "))
sum=0
for i in range(1,(N//2)+1):
    if(N%i==0):
        sum+=i

if(sum==N):
    print((f"{N} is a perfect Number."))
else:
    print((f"{N} is not a perfect Number."))
