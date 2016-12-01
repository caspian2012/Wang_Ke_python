""" Question 1""" 
'''This function is a palindrome recogniser that accepts a file
name from the user, reads each line, and prints the line to the
screen if it is a palindrome.'''

# Define a function named parlindrome that take a string as input,
# then the function re
# The parameter is a string.
def parlindrome(string):

# We list space and all the punctuations that will affect the program to judge 
# if the the input is palindrome.
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

# Set the string we gonna test initially to empty. We will remove the spaces
# and punctuations.
    remove_punct=""

# For each character in the string inputted from the user, if it is a space or 
# punctuation, then it is omitted. Only letters are added to the string
# we gonna test.
    for char in string:
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
        print(string)
    else:
        print("No, it is not a palindrome")
    
    
""" Question 2"""
'''This program is a semordnilap recogniser that accepts a file name 
from the user and finds and prints all pairs of words that are semordnilaps to 
the screen. '''

# Define a funtion semordnilap to find semordnilap that takes a file name from 
# the user and finds semordnilap pairs of a list of words in the file.
# The parameter is a file name from the user.
def semordnilap(file):

    # Access a file from the user, read its content and split the list of 
    # words into individual ones.
    filename = input("Enter filename: ")
    file = open (filename).read()
    words = file.split()
    
    # For any word in the list, if we can find another word that is its 
    # reverse, then we add the word pair to the result list.
    for word_a in words:
        for word_b in words:
            if word_b == word_a[::-1]:
                print (word_a, word_b)

    file.close()     

""" Question 3"""
'''This function accepts a file name from the user, builds a frequency listing 
of the characters contained in the file, and prints a sorted and nicely 
formatted character frequency table to the screen.'''

# Define a function char_freq_table that takes a file name from the user and
# builds a frequncy list of characters and print a frequency table.
# The parameter is a file name from the user.

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


""" Question 4"""
'''This is a program speak_ICAO()able to translate any text (i.e. any string)
into spoken ICAO words with given pause time of words and letters'''

# Import the operation system and time.
import os
import time

# Define a function speak_ICAO that takes 3 parameters and translate the 
# text into spoken ICAO words.
# The parameters of function speak_ICAO are:
# txt: the text to read
# letter_pause: the time pause between between each spoken ICAO word (letter)
# word_pause: the time pause between each word spoken
def speak_ICAO(txt, letter_pause, word_pause):
    
    # List the dictionary that matches the normal alphabet to the ICAO word.
    d = {
    'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
    'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
    'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
    'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
    'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
    'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
    'y':'yankee', 'z':'zulu'
    }
    
    for idx in range(0, len(txt)):
        # Change the letters from the text to lowercase since the dictionary
        # only consists of lowercase letters.         
        c = txt[idx]
        c = c.lower()
        # Set the time pause between each word.
        if c == ' ':
           time.sleep(word_pause)
        # Set the character to only alphabets. Use the system module to "speak"
        # the text. Note this only works for Mac system.
        elif 'a' <= c and c <= 'z':
           os.system('say '+ d[c])
           # Check the index idx+1 if it is within the text length and the 
           # next character is not a blank space. If both are met, then pause
           # for the time between letters.
           if idx+1 < len(txt) and txt[idx+1] != ' ':
               time.sleep(letter_pause)

# The text is 'This is a sentece'. It pauses for 1s bewteen ICAO word (letters)
# and 3s betweeb each word.        
speak_ICAO('This is a sentence.', 1, 3)


""" Question 5"""
'''This function return all its hapaxes in a text. Hapaxes are words which
occur only once in either the written record of a language, the
works of an author, or in a single text.'''

# Define a function hapax that takes a file name from the user and returns all
# its hapaxes (which are words that occur only once in the text).
# The parameter is a file name from the user.
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


""" Question 6"""
'''This program prompts user to enter a text file name, it will create a new 
text file in which all the lines from the original file are numbered from 
1 to n (where n is the number of lines in the file).'''
    
# Define a function add_number that takes a text file from the user and create 
# a new text file in which all the lines from the original file are numbered 
# from 1 to n (where n is the last line).
# The parameter is an input file name from the user and an output file name
# from the user.
def add_number(in_file_name, out_file_name):
    
    # Open file for reading and open file for writing.
    in_file = open(in_file_name,'r')
    out_file = open(out_file_name,'w')
    
    # Set initial line number to 1.
    line_num = 1
    
    # Write the file with adding a line number for each line recursively.
    for line in in_file:
        out_file.write('{}: {}'.format(line_num, line))
        line_num = line_num + 1


""" Question 7"""
'''This program calculates the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word the text, divided by the 
number of words). '''

# We list space and all the punctuations that will affect the length of the 
# word.
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

# Define a function avg_word_length that gives the average word length of a 
# text stored in an input file.
# The parameter is a file name from the user.
def avg_word_length(file_name):
    
    # Open file for reading.
    with open(file_name, 'r') as f:
        for line in f:
            
            # Remove punctuations.
            line = list(filter(lambda x: x not in punctuations, line))
            
            # The map function only take the length of each splitted word.
            words = list(map(len, line.split()))
    
    # sum(words) gives the sum of all the lengths of the word and len(words)
    # gives the number of word lenghts, which is also the number of words.         
    print (sum(words) / len(words))


""" Question 8"""
'''Guess the number game: this program asks user to guess a number between
0 to 20 inclusively. The user has infintely many trials. When the user guesses 
it correctly, it will tell the user that the guess is correct.'''

import random

# Define a function num_guess that generates a random number between 1 to 20
# and interact to user's guesses to the number.
# The parameter is a randomly generated number.
def num_guess(num):
    
    # Generate a random integer between 1 to 20 inclusively.
    num = random.randint(1, 20)  

    # Get user's name.
    user_name = input('Hello! What is your name? ')

    # Interact with user and give instructions, with user name info acquired from
    # previous input.
    print('Well, %s, I am thinking of a number between 1 and 20.' % user_name)

    # Set the initial value of number of guesses the user takes.
    guess_count = 1

    # Use while loop to give user feedback for 3 possible outcomes.
    while True:
    
        # Acquire user's guess and make it into an integer.
        guess = int(input('Take a guess. '))
    
        # One possible guess that is greater than the target number.
        # Hint the user that the number is high and add 1 to number of guesses.
        if guess > num:
            print('Your guess is too high.')
            guess_count += 1
    
        # One possible guess that is smaller than the target number.    
        # Hint the user that the number is low and add 1 to number of guesses.
        elif guess < num:
            print('Your guess is too low.')
            guess_count += 1
    
        # One possible guess that the user get the right number, end the program 
        # and tell the user how many times he/she has tried.    
        else:
            print('Good job, %s! You guessed my number in %d guesses!' % (user_name, guess_count))
            break
    
    
""" Question 9"""
'''This program is anagram game. It will generate an anagram from a random 
word in the given list and prompt user to guess the word.'''

# Import modules random and itertools for random selection and permutation.
import random
import itertools

# Define a function anagram_game that generates a random word from a word list,
# and make permutation of the letters in the word to ask the user to guess the
# original word and interacts with the user.
# The parameter is the randomly generated word from a word list.
def anagram_game(word):
    
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


""" Question 10"""
'''This program prompts the user to guess a five-letter word. 
Clues are given: [] means the letter is the right letter and in right position 
() means the letter is the right letter but not in the right position. '''

# Define a function lingo that has a preset five-letter word and ask the user
# to guess the word with clues.
# The parameter is the preset word.
def lingo(word):
    
    # Set the target word.
    word = list("tiger")
    
    # Interact with the user.
    print("import lingo")
    
    # Set the list of user's guess to empty.
    guess = []
    
    # Loop till the user get the correct word.
    while True:
        
        # Acquire the guess from user and turn it into a list.
        guess = list(input("Please enter your guess: "))
        
        # One possibility that the user guessed the right word. Break the loop.
        if guess == word:
            print("You guessed the right word!")
            break
        
        # One possibility that the user guess the word wrong. Set a clue list
        # equals to the user's guess list.    
        else:
            cluelst = guess
            
            # If a letter of user's guess is the same with the letter in 
            # target word and both are in the same position, then add "[]" to that
            # letter in the clue list. Note range(0, len(word)) makes sure the 
            # values of guess[i] and word[i] are letters in the respective word.
            for i in range(0, len(word)):
                if guess[i] == word[i]:
                    cluelst[i] = "[" + guess[i] + "]" 
                    
            # Similarly, if a letter of user's guess is the same with the letter 
            # in target word but in different position, then add "()" to that 
            # letter in the clue list.
            for i in range(0, len(word)):
                for j in range(0, len(word)):
                    if guess[i] == word[j]:
                        cluelst[i] = "(" + guess[i] + ")"
            
            # We join the letters, "[]"s, and "()"s which are elements of clue list
            # into a string, clue.
            clue = "".join(cluelst)
            
            # Give user the clue.
            print("Clue: " + clue)
            

""" Question 11"""
'''This program is a sentence splitter can split a text into sentences. 
It will print every sentence in every line'''

# Import regular expression operations module. The regular expression
# specifies a set of strings that matches it.
import re

# Define a fuction sentence_splitter that takes a file name from the user and
# split the text into sentences.
# The parameter is a file name from the user.
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


""" Question 12"""
'''This program finds the sets of words of anagram that share the same 
characters that contain the most words in them. '''

# Import defaultdict function.
from collections import defaultdict

# Define a function ana_finder that takes a file name from the user and finds
# the sets of words that share the same characters that has the most words.
# The parameter is a file name from the user.
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


""" Question 13 - Part A: about 'balanced strings'"""
'''This program generates a string with N opening brackets ("[") 
and N closing brackets ("]"), in some arbitrary order. 
And it prints whether there exists complete pairs of brackets'''

# Import module random with function randrange and module regular expressions.
from random import randrange
import re

# Define a function brackets that generates a string of pairs of "[" and "]',
# in some arbitrary order, and determines if the generated string is balances,
# namely consists entirely of pairs of opening/closing brackets.
# The parameter is an integer that decides the number of pairs of brackets are
# generated.
def brackets(n):
    
# Set the initial result string to empty, recursively add brackets to the 
# empty string from i == 0 and stops when i == n*2. 
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
'''This program generates the sequence with the highest possible
number of Pokemon names where the subsequent name starts with
the final letter of the preceding name from a given list with no
 Pokemon names repeated.'''

# Import regular expression module.
import re

# Define a function pokemon_names that takes a list of pokemon names from a 
# file and finds the list with the highest possible number of pokemon names 
# where the subsequent name starts with the final letter of the preceding name。
# The parameter is the file name from the user.
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


""" Question 14"""
'''This program prints all the alternade of every word in a word list. The 
alternades are of specially cases that one smaller words is formed by the odd
number of sequence in the original letter and the other smaller words if formed
by the even number of letters. These two smaller letters are also in the word
list. '''

# Import regurlar expression module, defaultdict function and reduce function.
import re
from collections import defaultdict
from functools import reduce

# Define a function alternade_finder that finds the special case alternades as
# described above from a file name and print all such alternades.
# The parameter is a file name from the user.
def alternade_finder(file_name):
    
    # Open the file and get its content.
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
