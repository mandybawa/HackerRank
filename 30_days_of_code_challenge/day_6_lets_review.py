# Task:
# Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd-indexed characters as 2
# space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Input Format:
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String, S.

# Output Format:
# For each String S print even-indexed characters, followed by a space, followed by S's odd-indexed characters.

# Sample Input:
# 2
# Hacker
# Rank

# Sample Output:
# Hce akr
# Rn ak


# Solution:

if __name__ == '__main__':
    num_test_cases = int(input())
    for x in range(num_test_cases):
        input_string = input()
        even_index_string = input_string[::2]
        odd_index_string = input_string[1::2]
        print(f"{even_index_string} {odd_index_string}")
