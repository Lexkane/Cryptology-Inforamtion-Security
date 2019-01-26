def main():
 pass

X = 1685287499328328297814655639278583667919355849391453456921116729
Y = 7114192848577754587969744626558571536728983167954552999895348492
def karatsuba(x, y):
    x = str(x)
    y = str(y)
 
    if len(x)%2 != 0:
        x = "0" + x
    if len(y)%2 !=0:
        y = "0" + y
 
    if len(x) < len(y):
        while len(x) != len(y):
            x = "0" + x
 
    if len(y) < len(x):
        while len(y) != len(x):
            y = "0" + y
   
    a = int(x[0:len(x)/2])
    b = int(x[len(x)/2:len(x)+1])
   
    c = int(y[0:len(y)/2])
    d = int(y[len(y)/2:len(y)+1])
   
    if len(str(a))>1 or len(str(c))>1 or len(str(b))>1 or len(str(d))>1:  
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
 
    else:
        ac = a*c
        bd = b*d
 
    parenth1 = a + b
    parenth2 = c + d
 
    if len(str(parenth1))>1 or len(str(parenth2))>1:
        par_mult = karatsuba(parenth1, parenth2)
    else:
        par_mult = parenth1 * parenth2
 
 
    m = par_mult-ac-bd
 
    result = (10**len(x))*ac + (10**(len(y)/2))*m + bd
 
    return result

print (karatsuba(X,Y))