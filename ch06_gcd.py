def gcd_i(a, b):
    while b:
        a, b = b, a%b
        return a

def gcd_r(a, b):
    if b == 0:
        return a
    else:
        return gcd_r(b, a%b)
