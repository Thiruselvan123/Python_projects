N=int(input())
while(N>0):
    temp=N
    while(temp>0):
        print("*",end="")
        temp-=1
    N-=1
    print("\n")