def discrete_logarithm(a,b,m):
    c = 1
    while pow(b,c) % m != a:
        c = c+1
    return c

def modulo_exponentiation(b,c,m):
    return pow(b,c) % m