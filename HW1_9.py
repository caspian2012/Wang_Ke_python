""" Question 9"""

# Import modules random and itertools for random selection and permutation.
import random
import itertools

# List color words and get a random one from the list with functions
# random.sample, where we select one element from the list color_words.
color_words =["red","orange","yellow","green","purple","black","brown","white",
              "blue","pink","grey"]
word=random.sample(color_words,1)[0]

# User itertools.permutations function to get the permutations of letters in 
# the random word we acquired previously and make it into a list, which is perm.
# Then we randomly select one of the permutations and join the letters into a
# anagram of the original random word.
perm = list(itertools.permutations(word))
perm_r = random.sample(perm,1)[0]
hint = ''.join(perm_r)

# Interact with the user and give him/her the hint.
print("import anagram")
print("Colour word anagram: " + hint)
ana_guess = input("Guess the color word!\n")

# Loop when the user fails to guess the right word.
while ana_guess != word:
    ana_guess = input("Guess the color word!\n")
    
# When the user get the right word, tell him/her that it is correct and break
# out of the loop.
print("Correct!")