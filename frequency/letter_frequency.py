import frequency.utils as utils

def letter_frequency(string):
    frequencies = {}
    total = utils.total_letters(string)
    counts = utils.count_letters(string)
    
    for key in counts:
        value = counts[key]
        frequencies[key] = round((value/total)*100,3)
    
    return frequencies