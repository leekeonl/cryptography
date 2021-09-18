#let There is given alphabet and key

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3

#caesar encrypt code algorithm
def caesar_encrypt(plain_text):
    
    #The encrypted message
    cipher_text = ''
    
    #make small letter case to upper case
    plain_text = plain_text.upper()
    
    #consider all the letters in the plain text
    for c in plain_text:
        #find the numerical representation (index associated with character)
        index = ALPHABET.find(c)
        #caesar encryption is simple shift
        #need to divide and get modulo by length of caesar encryption
        index = (index+KEY)%len(ALPHABET)
        #keeping encrypt word
        cipher_text = cipher_text + ALPHABET[index]
        
    return cipher_text

#caesar decrypt code algorithm
def caesar_decrypt(cipher_text):
    
    #The decrypted message
    plain_text = ''
    
    #consider all the letters in the plain text
    for c in cipher_text:
        #find the numerical representation (index associated with character)
        index = ALPHABET.find(c)
        #caesar decryption is simple shift
        #need to divide and get modulo by length of caesar decryption
        index = (index-KEY)%len(ALPHABET)
        #keeping decrypt word
        plain_text = plain_text + ALPHABET[index]
        
    return plain_text

if __name__ == '__main__':
    encrypted = caesar_encrypt("this is an example")
    print("encrypted word is ", encrypted)
    decrypted = caesar_decrypt(encrypted)
    print("decrypted word is ", decrypted)