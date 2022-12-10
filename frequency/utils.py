import re

ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def total_letters(string):
    return len(re.findall("\w",string))

def count_letters(string, alphabet=ENGLISH_ALPHABET):
    letter_counts = {}
    
    for letter in alphabet:
        count = len(re.findall(letter,string.lower()))
        letter_counts[letter] = count
        
    return letter_counts
