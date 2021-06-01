from random import randint
#import matplotlib.pylab as plt

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, key):
    plain_text = plain_text.upper()
    cipher_text = ""
    
    for index, char in enumerate(plain_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index+key_index)%len(ALPHABET)]
    
    return cipher_text

def decrypt(cipher_text, key):
    
    plain_text = ""
    
    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain_text += ALPHABET[(char_index-key_index)%len(ALPHABET)]
    
    return plain_text

def random_sequence(plain_text):
    random_sequence = []
    for rand in range(len(plain_text)):
        random_sequence.append(randint(0,len(ALPHABET)))
    return random_sequence
    
#from 2 Frequency analysis
def frequency_analysis(plain_text):
    
    plain_text = plain_text.upper()
    
    #assign dictionary to count letter frequency pair
    letter_frequency = {}
    
    #initiallize the dictionary content with zero
    for letter in LETTERS:
        letter_frequency[letter] = 0
        
    #count each letter using for loop
    for letter in cipher_text:
        if letter in LETTERS:
            letter_frequency[letter] += 1

    return letter_frequency

def plot_distribution(letter_frequency):
	centers = range(len(ALPHABET))
	plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
	plt.xlim([0,len(ALPHABET)-1])
	plt.show()
	

if __name__ == "__main__":
	
    plain_text = "ji sung park"

    print("Original message: %s" % plain_text)
    key = random_sequence(plain_text)
    cipher_text = encrypt(plain_text, key)
    print("Encrypted message: %s" % cipher_text)
    decrypted_text = decrypt(cipher_text, key)
    print("Decrypted message: %s" % decrypted_text)
	
#	plot_distribution(frequency_analysis(cipher_text))
	