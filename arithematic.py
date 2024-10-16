#class arithematic1():
#z1==20
#z2==30
def add_func1(z1,z2):
    addition = z1+z2
    return addition

def sub_func1(z1,z2):
    subtraction = z1-z2
    return subtraction
  
def mul_func1(z1,z2):
    multiplication = z1*z2
    return multiplication
  
def div_func1(z1,z2):
    division = z1%z2
    return division

num1=int(input("enter first number : "))
num2=int(input("enter second number:"))  

sum = add_func1(num1,num2)
print ("addition:",sum)
sub = sub_func1(num1,num2)
print ("subtraction:",sub)
mul =mul_func1(num1,num2)
print ("multiplication:",mul)
div = div_func1(num1,num2)
print ("division:",div)
