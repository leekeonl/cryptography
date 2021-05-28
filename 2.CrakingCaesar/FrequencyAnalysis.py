#import matplotlib.pylab as plt

LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(cipher_text):
    
    cipher_text = cipher_text.upper()
    
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

#plotting ciphertext. 
#def plot_distribution(letter_frequency):
#	centers = range(len(LETTERS))
#	plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
#	plt.xlim([0,len(LETTERS)-1])
#	plt.show()
	
def caesar_crack(cipher_text):
	
	letter_frequency = frequency_analysis(cipher_text)
	print(letter_frequency)
#	plot_distribution(letter_frequency)
	
	
if __name__ == "__main__":
	
	cipher_text = 'QBDREQIDMWDFEPECWDLSPGCIVCDMDEQDJVSQDFYHETIWXCDLYRKEVBCDMDEQDUYEPMJMIHDEWDEDTLBWMGMWXDERHDPEXIVDSRCDEXDXLIDQSQIRXDMDEQD SVOMRKDEWDEDWMQYPEXMSRDIRKMRIIVDEXDEDQYPXMREXMSREPDGSQTERBCDMDLEZIDFIIRDMRXIVIWXIHDMRDEPKSVMXLQWDERHDHEXEDWXVYGXYVIWDERHDMXWDMQTPIQIRXEXMSRWDIWTIGMEPPBDMRDNEZEDWMRGIDYRMZIVWMXBCDPEXIVDSRDMDKSXDEGUYEMRXIHD MXLDQEGLMRIDPIEVRMRKDXIGLRMUYIWCDEVXMJMGMEPDMRXIPPMKIRGICDRYQIVMGEPDQIXLSHWDERHDVIGMTIWDWYGLDEWDWSPZMRKDHMJJIVIRXMEPDIUYEXMSRWCDPMRIEVDEPKIFVECDMRXIVTSPEXMSRDERHDIAXVETSPEXMSRCDXLIWIDXLMRKWDQEBDTVSZIDXSDFIDZIVBDZIVBDMQTSVXERXDMRDWIZIVEPDJMIPHWCDWSJX EVIDIRKMRIIVMRKCDVIWIEVGLDERHDHIZIPSTQIRXDSVDMRZIWXQIRXDFEROMRKCDMDLEZIDEDWTIGMEPDEHHMGXMSRDXSDUYERXMXEXMZIDQSHIPWDWYGLDEWDXLIDFPEGOCWGLSPIWDQSHIPCDSVDXLIDQIVXSRCQSHIPC'
	caesar_crack(cipher_text)
	