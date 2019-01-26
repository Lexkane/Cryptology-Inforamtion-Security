#Program to calculate Chineese Divider Theorem output
def main ():
    def bezucoef(a, b):
        """Here we calculate Bezu coefficients for a and b"""
        s, olds = 0, 1
        t, oldt = 1, 0
        r, oldr = b, a
        while r != 0:
            quot = oldr // r
            oldr, r = r, oldr - quot * r
            olds, s = s, olds - quot * s
            oldt, t = t, oldt - quot * t
        return olds, oldt
    def chinese_remainder(remainders):
        """We will calculate such that x satisfies congruences.
        remainders should be a list of tuples (ai, ni)"""
        a1, n1 = remainders[0]
        for a2, n2 in remainders[1:]:
            m1, m2 = bezucoef(n1, n2)
            x = a1 * m2 * n2 + a2 * m1 * n1
            n1 *= n2
            while x < 0:
                x += n1
            a1 = x
        return a1, n1
    """remainders is our list of input tuple pairs"""
    remainders=[(25,5),(2,8),(9,3),(7,35)]
    print (chinese_remainder(remainders))



if __name__=="__main__":
    main()