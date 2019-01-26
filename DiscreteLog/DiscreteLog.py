import math

# efficient minmax algorithm to find x which suits for  B = A^x (mod p)

def discretelogsolve (a,b,p,N = None):
    if not N: N = 1 + int(math.sqrt(p))
    #small cycle
    baby_steps = {}
    baby_step = 1
    for r in range(N+1):
        baby_steps[baby_step] = r
        baby_step = baby_step * a % p

    #giant cycle
    giant_stride = pow(a,(p-2)*N,p)
    giant_step = b
    for q in range(N+1):
        if giant_step in baby_steps:
            return q*N + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % p
    return "No Match"
def main():
    print("Finding x for  B = A^x (mod p)/n")
    a=int(input(("Enter A")))
    b = int(input(("Enter B")))
    p = int(input(("Enter p")))
    print ('{} to the power of {} with modulo  of {} is equal to {}'.format(a,discretelogsolve(a,b,p),p,b))

if __name__== "__main__": main()