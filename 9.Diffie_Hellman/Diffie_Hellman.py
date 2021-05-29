import random

def generate_private_key(n,g):
    
    #random number for sender
    x = random.randint(1,n)
    
    #random number for receiver
    y = random.randint(1,n)
    
    #calculating g^x mod n for sender 
    k1 = pow(g,x,n)
    
    #calculating g^y mod n for receiver
    k2 = pow(g,y,n)
    
    print("Sender's Private key %s" % (pow(k2,x,n)))
    print("Receiver's Private key %s" % (pow(k1,y,n)))
    
if __name__ == "__main__":
    
    #set big prime number
    n = 37
    
    #g is the primitive root for n
    g = 13
    
    #using Diffie_Hellman cryptosystem for AES and DES
    generate_private_key(n,g)