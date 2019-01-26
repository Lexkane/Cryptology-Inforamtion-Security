import math
def main():
 pass

counter=0
X = 1685287499328328297814655639278583667919355849391453456921116729
Y = 7114192848577754587969744626558571536728983167954552999895348492

def karat(x,y):
    global counter
    if len(str(x)) < 3 or len(str(y)) < 3:
        return x*y

    n = max(len(str(x)),len(str(y))) // 2

    a = x // 10**(n)
    b = x % 10**(n)
    c = y // 10**(n)
    d = y % 10**(n)
    z0 = karat(b,d)
    z1 = karat((a+b), (c+d))
    z2 = karat(a,c)

    return ((10**(2*n))*z2)+((10**n)*(z1-z2-z0))+z0
    

print (karat(X,Y))
  