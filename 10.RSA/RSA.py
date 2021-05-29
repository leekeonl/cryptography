import random
from math import floor
from math import sqrt
 
RANDOM_START = 1e3
RANDOM_END = 1e5
 
def is_prime(num):
 
	#numbers smaller than 2 can not be primes
	if num<=2: return False
	
	#even numbers can not be primes
	if num%2==0: return False
 
	#we have already checked numbers < 3
	#finding primes up to N we just have to check numbers up to sqrt(N)
	#increment by 2 because we have already considered even numbers
	for i in range(3,floor(sqrt(num)),2):
		if num%i==0:
			return False
			
	return True
	
#extended Euclid's algorithm to find modular inverse in O(log m) so in linear time
#this is how we can find the d value which is the modular inverse of e in the RSA cryotisystem
def modular_inverse(a,m):
 
	m0 = m 
	y = 0
	x = 1
  
	if (m == 1) : 
		return 0
  
	while (a > 1) : 
  
        #quotient 
		q = a // m 
		t = m 
  
        #m is the remainder
        #same as the Euclid's gcd() algorithm 
		m = a % m 
		a = t 
		t = y 
  
        #update x and y accordingly
		y = x - q * y 
		x = t 
  
        #make sure x>0 so x is positive 
	if (x < 0) : 
		x = x + m0 
  
	return x 
 
#Euclid's greates common divisor algorithm: this is how we can verify whether (e,phi)
#are comprime ... with the gcd(e,phi)=1 condition 
def gcd(a,b):
 
	while b!=0:
		a, b = b, a%b
 
	return a
	
#method to generate large prime numbers
def generate_large_prime(start=RANDOM_START,end=RANDOM_END):
 
	#generate a random number [RANDOM_START,RANDOM_END]
	num = random.randint(RANDOM_START,RANDOM_END)
	
	#and check whether it is prime or not
	while not is_prime(num):
		num = random.randint(RANDOM_START,RANDOM_END)
	
	#we know the number is prime
	return num
	
def generate_rsa_keys():
 
	#generate the first huge random prime number 
	p = generate_large_prime()
		
	#generate the second huge random prime number
	q = generate_large_prime()
			
	#this is the trapdoor function: multiplying is fast but getting p and q from n
	#is an exponentially slow operation
	n = p*q
 
	#Euler's totient phi function
	phi = (p-1)*(q-1)
	
	e = random.randrange(1,phi)
	
	#we must make sure gcd(e,phi)=1 so e and phi are comprime otherwise we cannot find d
	while gcd(e,phi)!=1:
		e = random.randrange(1,phi)
	
	#d is the modular inverse of e
	d = modular_inverse(e,phi)
	
	#private key and the public key
	return ((d,n),(e,n))		
	
#encrypt messages: we use public keys for encryption
def encrypt(public_key, plain_text):
 
	#e and n are needed for encryption (these are public!!!)
	e, n = public_key
	
	#we use ASCII representations for the characters and the transformation of every
	#character is stored in an array
	cipher_text = []
	
	#consider all the letters one by one and use modular exponentiation
	for char in plain_text:
		a=ord(char)
		cipher_text.append(pow(a,e,n))
	
	return cipher_text	
	
#decrypt messages: we use private keys for decryption
def decrypt(private_key, cipher_text):
 
	#d and n are needed for decryption (these are private!!!)
	d, n = private_key
		
	plain_text = ''
		
	#consider all the numbers one by one and use modular exponentiation
	for num in cipher_text:
		a = pow(num,d,n)
		plain_text = plain_text + str(chr(a))
	
	return plain_text
	
if __name__ == "__main__":
 
	private_key, public_key = generate_rsa_keys()
 
	plain_text = 'This is a secret message!'
	
	print("Original message: %s" % plain_text)
	cipher_text = encrypt(public_key, plain_text)
	print("Cipher text: %s"%cipher_text)
	original_text = decrypt(private_key, cipher_text)
	print("Decrypted text: %s"%original_text)