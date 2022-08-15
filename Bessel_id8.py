
#Bessel's identity
#(8) d/dx(x^(-n)*jn(n,x)) = -x^(-n)*jn(n+1,x)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=int(input("Enter the n: "))
x=float(input("Enter the x: "))

def Bessels(x):
    return jn(n,x)
def der_Bessels(x):
    return derivative(Bessels,x,order=61)

LHS=der_Bessels(x**(-n)*jn(n,x))
RHS=-(x**(-n))*jn(n+1,x)

print("LHS: ",LHS)
print("RHS: ",RHS)
