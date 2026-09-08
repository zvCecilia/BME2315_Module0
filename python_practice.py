# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX
"""
def sum_fibonacci(N):
    sum = 0
    total = 0
    num = 0           """Used Ai help here to determine what I should set my variables equal to so that my loop would run correctly. For num and next""""
    next = 1
    for i in range (N): 
        sum += num
        num += sum
        total = num
        num = next
        next = sum + next
    return total

print(sum_fibonacci(5))

    
# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # The number of Fibonacci numbers to sum

a = 0 # A is set to the current fibonacci number
b = 1 # b is set to the next fibonacci number
count = 0
total = 0 # Total is the sum of the fibonacci numbers up to the Nth fibonacci number

while count < N:    # Loop of all fibonacci numbers up to the Nth fibonacci number
    total = total + a  # Add the current fibonacci number to the total

    next_value = a + b # Calculate the next fibonacci number
    a = b #a is now the current fibonacci number.
    b = next_value # b is now the next fibonacci number

    count = count + 1 #Adding the total count of fibonacci numbers to the count variable.

print(total)

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy as np
fibonacci_sequence10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # First 10 Numbers
std_dev = np.std(fibonacci_sequence) # Calculate the standard deviation using numpy





# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.
def sum_fibonacci(N):
    sum = 0
    total = 0
    num = 0
    next = 1
    for i in range(N): 
        sum += num
        num += sum
        total = num
        num = next
        next = sum + next
    return total

N = [5, 10, 15, 20, 25, 30]
new = []
for i in N:
    new.append(sum_fibonacci(i))
print(new)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    a = 0
    b = 1
    index = 0 # The index starting point has not been added + python did not know where to begin counting, Name error
    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1
    return index

print(find_fib_above_limit(7))


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # This line checks if the Fibonacci number is odd
            total = b
        a, b = b, a + b
    return total


limit = 7 would return 2, this is because the function originally calulcated the sum of even Fibonacci numbers instead of odd Fibonacci numbers.

# %%
