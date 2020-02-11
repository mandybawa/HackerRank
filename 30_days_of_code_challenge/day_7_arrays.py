# Task:
# Given an array, A, of N integers, print
# A's elements in reverse order as a single line of space-separated numbers.

# Input Format:
# The first line contains an integer, N (the size of our array).
# The second line contains N space-separated integers describing array A's elements.

# Output Format:
# Print the elements of array A in reverse order as a single line of space-separated numbers.

# Sample Input:
# 4
# 1 4 3 2

# Sample Output:
# 2 3 4 1


# Solution:

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reverse_arr = arr[::-1]
    output = ' '.join(str(e) for e in reverse_arr)
    print(output)
