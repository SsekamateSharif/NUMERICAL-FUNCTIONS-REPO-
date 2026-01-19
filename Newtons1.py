#when using Newtons method
#first define the equation
def f(x):
    return x**2 - 7*x + 12
#define the derivative
def divf(x):
    return 2*x - 7
#define the newtons method
def newtons(Xo, n, tol): # initial approximation, number of iterations and the tolerance
    i = 0
    while i < n:
        if divf(Xo) == 0:
            print(f"The derivative of {Xo} is zero")
            return None
        Xn = Xo - (f(Xo)/divf(Xo))
        if abs(Xn-Xo) > tol:
            print("There is a divergence")
            return None
        else:
            Xo = Xn
            i += 1
    return Xn

#implementation
root_1 = newtons(2.5,6,1)
root_2 = newtons(4,6,1)
print("The roots are: ")
print(f"X1 = {root_1}, X2 = {root_2}")





