""" Question 10"""

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