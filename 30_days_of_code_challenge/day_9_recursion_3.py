# Task:
# Write a factorial function that takes a positive integer, N as a
# parameter and prints the result of N!( Nfactorial).

# Input Format:
# A single integer, N (the argument to pass to factorial).

# Output Format:
# Print a single integer denoting N!

# Sample Input:
# 3

# Sample Output:
# 6


# Solution:

import os


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
