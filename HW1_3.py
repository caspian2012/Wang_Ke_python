""" Question 3"""
def char_freq_table(file_name):
    # Set the original frequency string to empty.
    frequency = {}
    
    # open file and read its content.
    with open(file_name, 'r') as f:
        
        # We remove the whitespaces and newlines to avoid them beijing counted.
        # Filter functions takes out elements that satisfy lambda function from
        # f.read().
        str = filter(lambda x: x not in [' ','\n'], f.read())

        # We check each character in string: if it is a new character, add it 
        # to the frequency string and set its value to 1; if it already exists
        # in the frequency string, then we add 1 to its value.
        for c in str:
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1

        # We sort the frequency list with the elements' value (it is positive  
        # interger since it represents the number of times it appeared). 
        # Then we print the character frequency table.
        print ('Characters frequency listing:')
        for char in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
            print (char[0], frequency[char[0]])

# Output the result when given an input.
file_name = input('Enter file name: ')
char_freq_table(file_name)
