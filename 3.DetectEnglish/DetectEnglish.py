ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#
ENGLISH_WORDS = []

#load english word
def get_data():
    dictionary = open("english_words.txt","r")

    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)
        
    dictionary.close()
    

def count_words(text):
    
    text = text.upper()
    words = text.split(' ')
    matches = 0
    
    for word in words:
        if word in ENGLISH_WORDS:
            matches = matches + 1
            
    return matches

def is_text_english(text):
    
    matches = count_words(text)
    
    #algorithm: if the text contains more than 80% of English, lets assume this is english words
    if (float(matches) / len(text.split('\n'))) * 100 >= 80:
        return True
    
    return False

#use from 2, BruteForce Algorithm
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
        
        if is_text_english(plain_text):
            print("we have managed to crack Caesar cipher, the key is %s, The message was %s" % (key, plain_text))
#        print("with key %s, the result is %s"%(key,plain_text))

if __name__ == "__main__":
	
	get_data()
	
	encrypted = 'VJKUBKUBCBOGUUCIG'
	caesar_crack(encrypted)
