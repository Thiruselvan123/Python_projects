                     #This is done by Thiruselvan E
#This program is coded without using function or recursion to print fibonacci series .


N=int(input("Enter the number : "))

first_term = 0
second_term = 1

print(first_term,end=" ")
print(second_term,end=" ")

for i in range(2,N):
    current_term = first_term + second_term

    first_term = second_term

    second_term = current_term

    print(current_term,end=" ")