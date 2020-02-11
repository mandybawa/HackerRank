# Task:
# Complete the Difference class by writing the following:

#  A class constructor that takes an array of integers as a parameter and saves it to the  elements instance variable.
#  A computeDifference method that finds the maximum absolute difference between any 2
#  numbers in N and stores it in the maximumDifference instance variable.


# Input Format:
# You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in
# 2 lines of input; the first line contains N, and the second line
# describes the elements array.

# Sample Input:
# 3
# 1 2 5

# Sample Output:
# 4


# Solution:


class Difference:

    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
