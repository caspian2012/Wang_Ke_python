""" Question 11"""

# Import regular expression operations module. The regular expression
# specifies a set of strings that matches it.
import re

# Construct a fuction. Open file for reading and acquire its content.
def sentence_splitter(file_name):
    with open(file_name, 'r') as f:
        file_in = f.read()

    # We first remove the newlines that were already there. Note that re.sub
    # is a substitute function that replace the pattern (in this case: r'\n',
    # a raw newline) in string (in this case: file_content) with replacement
    # (in this case '', empty string)
    sentences = re.sub(r'\n', '', file_in)

    # Following the rules from question,  we add a newline after each period 
    # only if that period is not preceded by 'Mr', 'Mrs' or 'Dr' and is 
    # followed by a space and an uppercase letter. Note that "?<!Mr" matches if
    # the current position in the string is not proceeded by a match of Mr. 
    # "\s([A-Z])" matches a whitespace followed by uppercase letters. The 
    # replacement is to add a raw newline, from the string "sentences" that
    # matches the pattern.
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)

    # Similarly, we do it for '!'. Note we do not need to worry about "Mr",
    # "Mrs", and "Dr" and all we need is a whitespace following "!".
    sentences = re.sub(r'!\s', '!\n', sentences)

    # Finally, we do it for every '?'.
    sentences = re.sub(r'\?\s', '?\n', sentences)

    print (sentences)

# Output the result when given an input.
sentence_splitter('sample.txt')
