""" Question 7"""

# We list space and all the punctuations that will affect the length of the 
# word.
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

# Construct function to find the average word length.
def avg_word_length(file_name):
    
    # Open file for reading.
    with open(file_name, 'r') as f:
        for line in f:
            
            # Remove punctuations.
            line = filter(lambda x: x not in punctuations, line)
            
            # The map function only take the length of each splitted word.
            words = list(map(len, line.split()))
    
    # sum(words) gives the sum of all the lengths of the word and len(words)
    # gives the number of word lenghts, which is also the number of words.         
    print (sum(words) / len(words))

# Output the result when given an input.
avg_word_length('sample.txt')