""" Question 8"""

# Get user's name.
user_name = input('Hello! What is your name? ')

# Interact with user and give instructions, with user name info acquired from
# previous input.
print('Well, %s, I am thinking of a number between 1 and 20.' % user_name)

# Set the predetermined number.
my_num = 18

# Set the initial value of number of guesses the user takes.
guess_count = 1

# Use while loop to give user feedback for 3 possible outcomes.
while True:
    
    # Acquire user's guess and make it into an integer.
    guess = int(input('Take a guess. '))
    
    # One possible guess that is greater than the target number.
    # Hint the user that the number is high and add 1 to number of guesses.
    if guess > my_num:
        print('Your guess is too high.')
        guess_count += 1
    
    # One possible guess that is smaller than the target number.    
    # Hint the user that the number is low and add 1 to number of guesses.
    elif guess < my_num:
        print('Your guess is too low.')
        guess_count += 1
    
    # One possible guess that the user get the right number, end the program 
    # and tell the user how many times he/she has tried.    
    else:
        print('Good job, %s! You guessed my number in %d guesses!' % (user_name, guess_count))
        break
    