""" Question 2"""

# Construct a funtion to find semordnilap that finds semordnilap pairs of a 
# list of words.
def semordnilap(file):

    # Access a file, read its content and split the list of words into
    # individual ones.
    file = open ('sample.txt').read()
    words = file.split()
    
    # Set the default empty result list
    results = []
    
    # For any word in the list, if we can find another word that is its 
    # reverse, then we add the word pair to the result list.
    for word_a in words:
        for word_b in words:
            if word_b == word_a[::-1]:
                results.append((word_a),(word_b))
    return results
    
    # Print the result list.
    print(semordnilap('sample.txt'))
           