def fibo(i):
    if i==0:
        return i
    elif i==1:
        return i
    else:
        return fibo(i-1)+fibo(i-2)
    
N=int(input())
for i in range(0,N):
    print(fibo(i),end=" ")