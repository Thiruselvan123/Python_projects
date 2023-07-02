                     #This code is done bt Thiruselvan E

#Here the program is coded to print whether it is armstrong number or not without using recursion.

# Logic of the program : first find the count of the digit then if the sum of digits power of count is equal to N or not

N=int(input("Enter the number : "))

S=str(N)     #Here int is type casting to str because we need to find the count by using len() function.

L=len(S)

sum=0

temp=N

while(temp!=0):
    rem=temp%10
    sum+=rem**L
    temp//=10

if(sum==N):
    print(f"{N} is an armstrong number")
else:
    print(f"{N} is not an armstrong number")


