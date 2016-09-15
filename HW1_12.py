""" Question 12"""

# Import defaultdict function.
from collections import defaultdict

def ana_finder(file_name):

    # Open the file, read it and add the raw stripped words into a list.
    words = []
    with open(file_name, 'r') as f:
        for line in f:
            words.append(line.rstrip())

    # We find words are anagram must have the same letters and have the same
    # length after they are sorted. To achieve a dictionary where the keys are
    # each of the sorted words of anagram, the values are the anagrams of such
    # letter combinations, we use the function defaultdict. We assign 
    # "anadict" to a dictionary with the above keys and values hold. The 
    # dictionary is a list of (anagram, anawords) where "anagram" is the key,
    # and "anawords" is the value.
    anagramdict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagramdict[key].append(word)

    # We set the biggest length value of anawords to 0 then 
    # replace it whenever a bigger length value of anawords is found to get 
    # the words length of the anagrams with the most words in them.
    longest_ana = 0
    for anagram, anawords in anagramdict.items():
        if len(anawords) > longest_ana:
            longest_ana = len(anawords)

    # After finding the max value of anaword length, we print the anagrams 
    # with the most words in them
    for anagram, anawords in anagramdict.items():
        if len(anawords) > longest_ana-1:
            print (anagram, anawords)

# Output the result when given an input.
ana_finder('sample.txt')
