
#CALCULUS
def differentiation(x):

    #using numerical differentiation
    def f(x):
        output = cos(x)
        return output

    h = 0.00001
    output = ((f(x+h) - f(x-h)) / (2*h))

    return output

print(differentiation(pi))
