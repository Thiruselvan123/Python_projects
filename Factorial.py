                   #This code is done by Thiruselvan E
 #The python program  to find factorial of a given  number using recursion.Ex:N=5,then factorial=5*4*3*2*1.


def Factorial(N):
    if(N!=0):
        return N*Factorial(N-1)
    else:
        return True
    

N=int(input("Enter a number : "))

result = Factorial(N)

print(f"The factorial of {N} is {result}.")