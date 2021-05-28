ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#craking caesar with BruteForce

def caesar_crack(cipher_text):
    
    #get all element size of the Alphabet
    for key in range(len(ALPHABET)):
        
        #reinitiallize this to be empty
        plain_text = ''
        
        #Caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index-key)%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
            
        print("with key %s, the result is %s"%(key,plain_text))

if __name__ == '__main__':
    
    encrypted = "VJKUBKUBCBOGUUCIG"
    caesar_crack(encrypted)