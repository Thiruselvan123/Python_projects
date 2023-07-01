                 #This code is done by Thiruselvan E

# This program prints the sum of two values without using '+' operator 

# The approach of the program is using for loop from range 1 to second value until second value is reached N1 is incremented by 1


N1 = int(input("Enter the first number : ")) 

N2 = int(input("Enter the second number : ")) 

for i in range(1,N2+1):
    N1 += 1

print(N1)