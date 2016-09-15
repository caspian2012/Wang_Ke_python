""" Question 4"""

# Import the operation system and time.
import os
import time

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


# The parameters of function speak_ICAO are:
# txt: the text to read
# letter_pause: the time pause between between each spoken ICAO word (letter)
# word_pause: the time pause between each word spoken
def speak_ICAO(txt, letter_pause, word_pause):
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