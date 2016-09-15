""" Question 14"""

# Import regurlar expression module, defaultdict function and reduce function.
import re
from collections import defaultdict
from functools import reduce

# Open the file and get its content.
def alternade_finder(file_name):
    with open(file_name, 'r') as f:
        words = re.findall(r'\w+', f.read())

    # Construct dictionary with defaultdict function as used in question 12.
    foundalters = defaultdict(list)

    # For each word in the list, we make a copy of the words list and prepare 
    # our variables, then we remove the word from the list so it doesn't 
    # choose itself as an alternade.
    for word in words:
        wordlist, smaller_even, smaller_odd = words[:], '', ''
        wordlist.remove(word)

        # Only words longer than 1 letter can possibly be divided into 2 
        # smaller words.
        if len(word) > 1:
            # For each letter in the word, get the position of this letter.          
            for letters in word: 
                letter_pos = word.index(letters)

                # If the letter is at an even position, add this letter to the 
                # variable.
                if letter_pos % 2 == 0:
                    smaller_even += letters
                    
                    # If the smaller word is in the words list and is not yet
                    # in the dictionary for the current word, add it to the dict
                    if smaller_even in wordlist and \
                    smaller_even not in foundalters[word]:
                        foundalters[word].append(smaller_even)

                # If the letter is at an odd position, add this letter to the 
                # variable. 
                if letter_pos % 2 != 0:
                    smaller_odd += letters 
                    
                    # If the smaller word is in the words list and is not yet
                    # in the dictionary for the current word, add it to the dict
                    if smaller_odd in wordlist and \
                    smaller_odd not in foundalters[word]:
                        foundalters[word].append(smaller_odd)

    # For each word in the dictionary, make a string out of the alternades.
    for word, alternades in foundalters.items():
        alt = reduce(lambda x, y: x + y, alternades)
        
        # If all the letters in the word have been used to create all
        # the alternades, print this word and its alternades
        if sorted(alt) == sorted(word):
            print ('"%s": makes %s' % (word, alternades))

# Output the result when given an input.
alternade_finder('sample.txt')