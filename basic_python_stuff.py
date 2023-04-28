# simple math functions using integers
x = 4
print (x, type(x))

add = x + 1
print (add)
sub = x - 1
print (sub)
mult = x * 2
print (mult)
div = x // 2
print (div)
exp = x ** 2
print (exp)

# same functions but using float
y = 4.321
print ("Float value is: ", y, type(y))
add = y + 1
print ("Addition: y+1=", add)
sub = y - 1
print ("Subtraction: y-1=", sub)
mult = y * 2
print ("Multiplication: y*2=", mult)
div = y // 2
print ("Division: y/2=", div)
exp = y ** 2
print ("Exponential: y^2=", exp)
#using prefix notation for incrementing a value
start = 10
print ("Starting value is ", start)
start +=1
print ("Addition: value +=1 returns ", start)
start -= 1
print ("Subtraction: current value -=1 returns ", start)
start *= 2
print ("Multiplication: current value *=2 returns ", start)
start //= 2
print ("Division: current value //=2 returns ", start)
start **= 2
print ("Exponential: current value^2=", start)




#Python3 program to add two integers
num1=3
num2=5

#Get the sum
sum= num1+num2

#Print value stored in sum
print("Sum = {0}." .format(sum))
###################

# Find the factorial for an integer
# n!=n*(n-1)*(n-2)*....*1
# Example:  4!=4*3*2*1=24
# Using a recursive approach:
def rec_factorial(n):
    return 1 if (n==1 or n==0) else n * rec_factorial(n-1);
# Driver
num = 12;
print ("Using a recursive method, the factorial of ", num, "is", rec_factorial(num))

##### Iterative method to find factorial
def it_factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        val=1
        while(n>1):
            val *=n
            n -=1
        return val
#Driver
value = 7;
print("Using an iterative method, the factorial of", value,"is", it_factorial(value))
########################

# Compute the square root of a simple number
s_num = 8
#  use the exponent operator to represent square of
s_root = s_num ** 0.5
print ('Square root of %0.5f is %0.5f.'%(s_num, s_root))

# Compute square root of complex number
# use the complex math module to access sqrt() function
import cmath
cs_num = 1+3j
# can use eval() function if we want to get input from user
#cs_num = eval(input('Enter a number: '))
#
cs_root = cmath.sqrt(cs_num)
print('Square root of {0} is {1:0.3f}+{2:0.3f}j'.format(cs_num, cs_root.real,cs_root.imag))

##############################

# Compute area of a triangle
a = 5
b = 6
c = 7
s = (a + b+ c)/2
# use an implementation of Heron's Formula to calculate area
t_area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the triangle is %0.3f.'%(t_area.real))

#######################

