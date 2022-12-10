import frequency.utils as utils
def ioc(string,alphabet=utils.ENGLISH_ALPHABET):
    total_letters = utils.total_letters(string)
    total_length = len(string)
    letter_counts = utils.count_letters(string)
    # print(total_letters,letter_counts)
    
    total = 0 
    for letter in alphabet:
        ni = letter_counts[letter]
        if ni > 0:
            # print(ni)
            # print((ni,ni-1))
            total += ni*(ni-1)

    # print(total)
        
    return float(total)/(total_letters*(total_letters-1))
    