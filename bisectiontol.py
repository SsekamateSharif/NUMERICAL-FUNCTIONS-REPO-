#when given tolerance
#first define the equation
from itertools import count


def f(x):
    return x**2 -7*x + 12
#define the bisection method
def bisection(a,b,tol): # given approximations and the tolerance
    if f(a)*f(b) > 0: # check for roots between (a,b)
        print(f"There is no root between {a} and {b}")
        return None
    else:
        while abs(b-a) > tol:
            m = (a+b)/2
            if f(m)*f(a) < 0: # check for root btn (a,m)
                b = m

            else:
                a = m
        return m

#implementation
root_1 = bisection(1,4,0.001)
root_2 = bisection(3,4.5,0.001)
print("The roots for the equation are: ")
print(f"X1 = {root_1}  , X2 = {root_2} ")

