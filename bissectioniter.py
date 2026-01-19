#bisection method when given iterations
#first define the function of the equation
def f(x):
    return x**2 - 7*x + 12
#define the bisection method
def bisection(a,b,n): # where a and b are the first approximations and n is the number of iterations
    if f(a)*f(b) > 0:  # check for a root btn (a,b)
        print(f"There is no root btn {a} and {b}")
        return None
    else:
        i = 0
        while i < n:
            m = (a+b)/2
            if f(m)*f(a) < 0:
                b =m
            else:
                a = m
            i += 1
        return m

#implemantation
root_1 = bisection(1,4,6)
root_2 = bisection(3,4.5,6)
print(f"X1 = {root_1}, X2 = {root_2}")





