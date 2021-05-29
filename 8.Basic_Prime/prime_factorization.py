from math import sqrt
from math import floor

def factor(num):
    
    factors = []
    limit = floor(sqrt(num))
    
    for n in range(2, limit):
        if num % n == 0:
            factors.append(n)
            factors.append(int(num/n))
            
    return sorted(factors)

if __name__ == "__main__":
    print(factor(210))
    print(factor(11))