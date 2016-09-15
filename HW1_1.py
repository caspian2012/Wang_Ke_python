""" Question 1""" 

# We list space and all the punctuations that will affect the program to judge 
# if the the input is palindrome.
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

# Set the string we gonna test initially to empty. We will remove the spaces
# and punctuations.
remove_punct=""

# For each character in the string inputted from the user, if it is a space or 
# punctuation, then it is omitted. Only letters are added to the string
# we gonna test.
sth = input("Enter text: ")
for char in sth:
   if char not in punctuations:
       remove_punct = remove_punct + char
       
# Construct a function that turns a string order backward (last letter first).
def reverse(remove_punct):
    return remove_punct[::-1]
    
# Construct a function that check if the string is palindrome by comparing the
# test string and its reverse. The function compares only the lowercase of 
# the letters.
def is_palindrome(remove_punct):
    return remove_punct.lower() == reverse(remove_punct.lower())

# If the string is the same with its reverse then the input is a palindrome
# and the program gives yes and the original input. If it is not the same
# then the program returns no.
if is_palindrome(remove_punct):
    print("Yes, it is a palindrome")
    print(sth)
else:
    print("No, it is not a palindrome")
    