#first define the derivative equation
def divf(x):
    return 2*x
#define eurlers method
def eulers(Xo, Yo, h, target):
    if Xo > target:
        print("The X approximation is bigger than the target")
        return None
    elif Yo > target:
        print("The Y approximation is greater than the target")
        return None
    else:
        while Xo <= target:
            Xn = Xo + h
            Xo = Xn
            Yn = Yo + h*(divf(Xo))
            Yo = Yn

        return Yn

ans = eulers(1,1,0.1,2)
print(f"f({2})= {ans}")



