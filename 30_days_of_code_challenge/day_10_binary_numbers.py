# Task:
# Given a base-10 integer,n, convert it to binary (base-2). Then find and
# print the base-10 integer denoting the maximum number of consecutive 1's
# in n's binary representation.

# Input Format:
# A single integer, n.

# Output Format:
# Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary
# representation of n.

# Sample Input 1:
# 5

# Sample Output 1:
# 1

# Sample Input 2:
# 13

# Sample Output 2:
# 2


# Solution:


if __name__ == '__main__':
    n = int(input().strip())
    consecutive_count = 0
    while n > 0:
        n = n & (n << 1)
        consecutive_count += 1

    print(consecutive_count)
