# Task:
# Given an integer n, perform the following conditional actions:

#  If n is odd, print Weird
#  If n is even and in the inclusive range of 2 to 5, print Not Weird
#  If n is even and in the inclusive range of 6 to 20, print Weird
#  If n is even and greater than 20, print Not Weird

# Input Format:
# A single line containing a positive integer n

# Output Format:
# Print Weird if the number is weird; otherwise, print Not Weird.

# Sample Input Format 0:
# 3

# Sample Output Format 0:
# Weird

# Sample Input Format 1:
# 24

# Sample Output Format 1:
# Not Weird


# Solution:

if __name__ == '__main__':
    N = int(input())
    if N % 2 == 0:
        if N in range(2, 6):
            print("Not Weird")
        if N in range(6, 21):
            print("Weird")
        if N > 20:
            print("Not Weird")
    else:
        print("Weird")
