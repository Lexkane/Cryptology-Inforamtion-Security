#Simple program to calculate Divider and Bezu coeficients
def extended_euclid(a,b):
    if b == 0:
        return a, 1, 0
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_euclid(b % a, a)
        return (g, y - (b // a) * x, x)
def main():
    a=int(input("Please enter 1st number"))
    b=int(input("Please enter 2nd number"))
    print("Divider of two numbers and Bezu coeficients are {}".format(extended_euclid(a,b)))

if __name__== "__main__" :
    main()
