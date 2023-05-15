def ADDITION(num1,num2):
    return num1+num2   
def SUBTRACTION(num1,num2):
    return num1-num2
def MULTIPLICATION(num1,num2):
    return num1*num2
def DIVISION(num1,num2):
    return num1/num2
def MODULO(num1,num2):
    return num1%num2


num1=int(input("Enter the first number:"))
num2=int(input("Enetr the second number:"))

print("----operations----")
print("+ : ADDITION")          #addition(+) operation returns the sum of two numbers
print("- : SUBTRACTION")       #subtraction(-) operation returns the difference between two numbers
print("* : MULTIPLICATION")    #multiplication(*) returns the product of two numbers 
print("/ : DIVISION")          #division(/) returns the quotient 
print("% : MODULO")            #modulo(%) returns the remainder
symbol=input("Enter the operation you want(+,-,*,/,%):")




if(symbol=='+'):
    print(num1,"+",num2,"=",ADDITION(num1,num2))
elif(symbol=='-'):
    print(num1,"-",num2,"=",SUBTRACTION(num1,num2))
elif(symbol=='*'):
    print(num1,"*",num2,"=",MULTIPLICATION(num1,num2))
elif(symbol=='/'):
    print(num1,"/",num2,"=",DIVISION(num1,num2))
elif(symbol=='%'):
    print(num1,"%",num2,"=",MODULO(num1,num2))
else:
    print("INVALID SYMBOL .Please select valid operation")

