#QUADRATIC EQUATION
import cmath
a=int(input("EnTER A VALUE:"))
b=int(input("EnTER B VALUE:"))
c=int(input("EnTER C VALUE:"))
Q=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(Q))/(2*a)
sol2=(-b+cmath.sqrt(Q))/(2*a)
print("THE SOLUTION ARE:",sol1,sol2)
