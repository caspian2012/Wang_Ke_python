""" Question 5"""

# Construct function hapax.
def hapax(file_name):
    
    # Set the list we gonna get to empty.
    words = [] 
    
    # Acquire the text and modify the letters to lowercase and split the words.
    with open(file_name, 'r') as f:
        for line in f:
            words += line.lower().split()

    # Remove the words repeated more than once from the words list with the  
    # filter function for lambda function remains True. Lambda function remails
    # True when the occurance of word is 1.
    hapaxes = list(filter(lambda x: words.count(x) == 1, words))
	
    # Return what we need.
    return hapaxes

# Output the result when given the text.
print (hapax('sample.txt'))