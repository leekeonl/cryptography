from math import sqrt
from math import floor

def is_prime(num):
    
    #number smaller than 2 cant be prime
    if num <= 2:
        return False
    
    #even number is not a prime
    if num % 2 == 0: 
        return False
    
    
    for i in range(3, floor(sqrt(num)), 2):
        if num % i == 0:
            return False
        
    return True

if __name__ == "__main__":
    print(is_prime(11))