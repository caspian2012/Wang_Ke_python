""" Question 13 - Part A: about 'balanced strings'"""

# Import module random with function randrange and module regular expressions.
from random import randrange
import re

# Set the initial result string to empty, recursively add brackets to the 
# empty string from i == 0 and stops when i == n*2. 
def brackets(n):
    i, result, brackets = 0, '', '[]'

    # The result string is recursively modified with brackets randomly added
    # to the result string.
    while i < n*2:
        result += brackets[randrange(len(brackets))]
        i+=1

    # Save our randomly composed string of brackets.
    bracket_string = result

    # When there are still brackets in the results string, we find "[" and "]"
    # pairs and replace is with empty string. Note re.findall gives all the 
    # matched pattern (in this case, a pair "[" and "]"). When its length is 
    # greater than 0, it means there are still brackets in the result string.
    # re.sub function is explained in question 11. Thus the loop breaks 
    # when all "[" and "]" pairs are replaced with empty string. 
    while len(re.findall(r'\[\]', result)) > 0:
        result = re.sub(r'\[\]', '', result)

    # If after removing all pairs of brackets the string is still not empty, 
    # it means that there are "]" and "[" pairs left, thus it is not balanced
    # string.
    if len(result) > 0:
        print (bracket_string, 'NOT OK')
    else:
        print (bracket_string, 'OK')

# Test for any positive integer n.
brackets(4)


""" Question 13 - Part B: Pokemon"""

# Import regular expression module. Note python alerts me that there is something
# wrong with the code because I imported regular expression in Part A. But I
# would rather not seperate these two part to cause confusion.
import re

def pokemon_names(file_name):
    # Get all the names of pokemons from the file.
    with open(file_name, 'r') as f:
        names = re.findall(r'\w+', f.read())

    # Set the initial empty list for the longest and current pokemon name series.
    longest_series, current_series = [], []

    # Returns the index of the word that starts with the last letter
    # of the previous word. Note startswith function checks the first letter.
    def name_starts_with(lastletter, names):
        for index, name in enumerate(names):
            if name.startswith(lastletter):
                return index
        return False

    # For each name that is in the pokemon names list, add the first name to
    # the series. 
    for name in names:
        current_name = name
        current_series.append(current_name) 
        
        # Make a copy of the names list and remove the first name from the list.
        namelist = names[:]
        namelist.pop(namelist.index(current_name))
        
        # Use the function constructed above to get the index of the next name.
        index = name_starts_with(current_name[-1], namelist) 

        # The loop continues as long as there exists a pokemon name that starts
        # with the last letter of the previous name. Note the loop get the 
        # name that satisfies, add it to the list, remove it and then look for
        # the next one.
        while index is not False:
            current_name = namelist[index] 
            current_series.append(current_name) 
            namelist.pop(index) 
            index = name_starts_with(current_name[-1], namelist)

        # We find such lists recursively and replace the longest_series list 
        # with the current_series whenever the current_series list length is
        # larger than the longest_series list length.
        if len(current_series) > len(longest_series):
            longest_series = current_series

        # Everytim the loop stops we reset the current_series list to empty to
        # start a new loop for a new starting pokemon name.
        current_series = []

    # After finished with everyone possible start pokemon name, we find the 
    # longest list and we output it.
    print (longest_series)

# Output the result when given an input.
pokemon_names('sample.txt')
