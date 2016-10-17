#Stuart- Nice HW all around. Excellent work.
""" Question 1"""
#Stuart- Nice, a simple and clean implementation.

# Define the function that finds the index of the first term that contains x
# digits.
def fib_digit(x):
    
    # Set "a" to be the value of nth Fibonacci sequence (here initially n=0); 
    # "b" to be the n+1th, or the sum of n-1th and nth (initially 1st);
    # "i" to be the index of Fibonacci (initially 0)
    a, b, i = 0, 1, 0
    
    # Loop while the value of Fibonacci sequence is less than 1*10^n, namely
    # has less than n digits. Assign "a" to be the n+1th value (which is "b"), 
    # "b" to be the n+2th value (acquired by adding nth and n+1th), "i the 
    # index increase by 1. When the loop stops, we get the nth number of 
    # Fibonacci sequence such that it is the first that has x digits, return 
    # its index i.
    while a < 10**x:
        a, b = b, a + b
        i += 1
    return i
    
# Find the index of such number in Fibonacci sequence that has 100 digits.
fib_digit(100)


""" Question 2"""

# We first create the triangle.
triangle= [ [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]  ]

# Define the function to calculate the max sum.
def max_triangle(triangle):
    
    # Suppose we know the maximum sum to get to the numer in 2nd to last line,
    # triangle[13][x], then to find the maximum sum for the last line, we 
    # simply choose the larger of the two options, namely 
    # max(triangle[14][x], triangle[14][x+1]).
    # Then we can use recursion to find each one in the triangle from bottom to
    # top and eventually, the maximum sum for triangle[0][0]
    # Note for range of i and j, the recusion is from bottom to top so the 
    # step is -1.
    
    n = len(triangle)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

max_triangle(triangle)


""" Question 3 """

# Define the function that calculates the length of Collatz chain for a given
# integer.
def collatz(num):
    
    # Set the initial length to 1.
    length = 1
    
    # The loop will continue until the number becomes 1. If the number is even,
    # then the next number equals to num/2. If the number is odd, then the next
    # number equals to 3*num+1. We increase the length by 1 each time we do a 
    # calculation for the next number. It returns the length of the chain.
    while num != 1:
        if num%2 == 0:
            num = int(num/2)
        else:
            num = 3*num+1
        length += 1
    return length
 
# Define the function that calculates the longest Collatz chain.   
def main(limit):
    
    # Set the initial value of length and initial starting number.
    value = collatz(1)
    start = 1
    
    # Use for loop to go through every positive integer under the limit
    for i in range(2,limit):
        
        # Replace the value of length and the starting number whenever a 
        # longer chain is found.
        if value < collatz(i):
            value = collatz(i)
            start = i
            
    # Print the result.
    print('Starting number is {}, under the limit of {}, produces the longest chain and the length is {}'.format(start,limit,value))

# Find the longest Collatz chain of numbers under 1,000.
main(1000)


""" Question 4""" 

#Stuart- Interesting solution and correct, but if you wanted to run this program 
#on integers greater than 3000 your code would fail. If you decided not to call 
#any external lbiraries you could try implementing long division from scratch, but
#this solves the problem as asked.


# We import decimal library since we want to be able to access more numbers 
# after the decimal point. We use getcontext() function to access 3000 digits
# after the decimal point.
from decimal import *
getcontext().prec = 3000

# Define the function that checks the recurring cycle with parameter "integer" 
# represent the denominator.
def recur_cycle(integer):   
    
    # we get the value of 1/integer with 3000 digits after decimal point and 
    # convert it into a string.
    x = Decimal(1)/Decimal(integer)
    temp = str(x)
    
    # We find the position of the decimal point and remove it, since we only
    # care for numbers after the decimal point.
    place = temp.find('.')
    temp = temp[place+1:]
    
    # Set the initial i to 1 and set running to true to help us doing the loop.
    i = 1
    running = True
    
    # The while loop stops once the "running" becomes to false. We check the 
    # digits in the recurring cycle in recursion method.
    while running:
        
        # If there are digits that recurred twice, then we find our needed
        # cycle and return its length i and end the loop.
        if temp[:i] == temp[i:2*i] and temp[i:2*i]== temp[2*i:3*i]:
            return i
            running = False
            
        # The loop could run forever if there is no recurring cycle for the 
        # number (e.g. e, pi). Thus we set it to stop at i = 800 and return
        # the length as 0.
        elif i == 800:
            return 0
            running = False
        
        # If i is not the length of recurring cycle and i is smaller than 800, 
        # add 1 to i and go to the next loop.
        else:
            i +=1

def main():
    
    # Set an empty list for the length 
    length = []
    
    # Calculate every length for integer from 2 to 499 and add it to the list           
    for i in range(2,500):
        length.append(recur_cycle(i))
        
    # Print the max length of the list. Note we add 2 since the list starts 
    # with 2 instead of 0.
    print ('The integer which has the longest recurring cycle is {}. Its length is {}.'.format(length.index(max(length))+2,max(length)))

main()


""" Question 5"""

#Stuart- Again a nice clean and simple implementation.

# We create a list with each value being 0 for 201 values, with the ith  
# value will be the total number of metheds to divide i-1 pennies.
ways = [0]*201

# We set the initial value at index 0 to 1, since whenever a successful method
# to divide the 200 pennies is found, we add 1 to the value indicating the 
# total number of such methods.
ways[0] = 1

# All possible coin values.
for x in [1,2,5,10,20,50,100,200]:
    
    # We use recursion to find the total methods to divide i pennies by adding
    # all possible methods to divide i-x pennies, where x is one of the possible
    # coin values.
    for i in range(x, 201):  
        ways[i] += ways[i-x]
        
# We find the total number of methods to divide 200 pennies.
print (ways[200])


""" Question 6"""

import math

# The function checks if a number is a prime number starting with divisor 2.
def is_prime(num):
    return is_prime_recur(2, num)

# The recursion function checks if a number is prime with parameters "divisor"
# to check if the number is dividable and "num" is the number to check.
def is_prime_recur(divisor, num):
    
    # We set the initial values.
    if num == 1:
        return False
    if num == 2:
        return True
    
    # We only need to check divisor that is smaller than the square root of 
    # the number, since by mathematics, if there is a number larger than its
    # square root that can divide the number to check, there must exist a 
    # number smaller than the square root.
    if divisor > int(math.sqrt(num)):
        return True 
    
    # If we can find such divisor, then the number is not prime.
    if num % divisor == 0:
        return False
    # We check for the next divisor.
    else:
        return is_prime_recur(divisor + 1, num)
        
# We test with a few numbers.    
print(is_prime(1))
print(is_prime(2))  
print(is_prime(7))
print(is_prime(25))
print(is_prime(43))


""" Question 7""" 

# We define the function that sorts a list of strings. We want to sort with 
# order that number 0-9 first and then letter a-z (regardless of lowercase or
# uppercase). When the first character is the same, we compare the second, 
# the third and so on until it is different. If first few characters are the 
# same for two strings, then the shorter one comes first (e.g. "to" and "today"
# will give "to" first)
def sort_list(strings):

    # Here we want to compare two adjacent strings. If the former one is bigger
    # than the later one, exchange them. We will get the biggest one to the end
    # of the list, while the rest of the list not sorted. We continue the 
    # process until the list is sorted.
    
    # We set i that counts backword.
    for times in range(1,len(strings)):
        for i in range(len(strings)-times):
            
            # Since we can only compare when both string has character in 
            # position i, we get n which is the length or shorter string.
            # We set "flag" for later when the two string has the same first 
            # few characters.
            n = min(len(strings[i]),len(strings[i+1]))
            flag = 0
            
            # Loop.
            for j in range(n):
                
                # If the character is not the same, we put the bigger one in 
                # the later position and break the loop.
                if strings[i][j] != strings[i+1][j]:
                    if strings[i][j]>strings[i+1][j]:
                        temp = strings[i]
                        strings[i] = strings[i+1]
                        strings[i+1] = temp
                    break
                
                # If the characters for position i are the same, add 1 to "flag".
                elif strings[i][j] == strings[i+1][j]:
                    flag +=1
                    
            # If flag is equal to n, then it means the first n characters of the
            # two string are the same. Then we put the shorter one in the 
            #former position.
            if flag == n and len(strings[i])>len(strings[i+1]):
                strings[i] = strings[i+1]
    print(strings)
    
# check
strings = ['alph','beta','betas','omega','happy','waht','2to1']            
sort_list(strings)  


""" Question 8"""

# Define the function that does the calculation, with x being the intial value
# and n being the number of time the function is run.
def calculation(x,n):
    
    # e1, e2, e3 are the results of 3 expressions respectively. i is the 
    # counter of times the function has run.
    e1 = x
    e2 = x
    e3 = x
    i  = 0
    
    # We keep running the function until it has run the required n times.
    while i < n:
        
        # The three expression are given
        e1 = 3.95*e1*(1-e1)
        e2 = 3.95*e2-3.95*e2**2
        e3 = 3.95*(e3-e3**2)
        
        # Output the result of e1, e2, e3 each time the function is run.
        print(e1,e2,e3)
        
        # Add 1 to the counter.
        i += 1
        
# Calculate the required x = 0.9, n = 100.
calculation(.9,100)

# From the results we find that the first several values of the 3 expressions 
# are very close (approx. first 50). Then the values soon become very different
# from each other. Although the 3 expressions gives the same value mathematically,
# they are different after multiple runs with our program because each time a
# calculation is done, the program will take the approximate value of the 
# result, rather than the actual value. When it is plug into the function for 
# next calculation, the values of 3 expressions are already not the same. The 
# more calculations done, the more they diverge from each other, with each
# approximate value taken.