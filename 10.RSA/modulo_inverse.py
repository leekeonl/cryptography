from math import sqrt
from math import floor

def modulo_inverse(a,m):
    
    for i in range(m):
        if (a*i) % m == 1:
            return i
    
    return 0

if __name__ == "__main__":
    # should print 9 since 7*9 = 63 mod31 == 1
    print(modulo_inverse(7,31))