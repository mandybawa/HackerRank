# Task:
# You are given two classes, Person and Student, where Person is the base
# class and Student is the derived class. Completed code for Person and a
# declaration for Student are provided for you in the editor. Observe that
# Student inherits all the properties of Person.

# Complete the Student class by writing the following:

#  A Student class constructor, which has 4 parameters:

#  A string, firstName
#  A string, lastName
#  An integer, id
#  An integer array (or vector) of test scores, scores

# A char calculate() method that calculates a Student object's average and
# returns the grade character representative of their calculated average:

# O 90 <= a <= 100
# E 80 <= a < 90
# A 70 <= a < 80
# P 55 <= a < 70
# D 40 <= a < 55
# T a < 40

# Sample Input:
#  Heraldo Memelli 8135627
#  2
#  100 80

# Sample Output
#  Name: Memelli, Heraldo
#  ID: 8135627
#  Grade: O


# Solution:


class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        score_average = sum(self.scores) / len(self.scores)
        if score_average >= 90 and score_average <= 100:
            return 'O'
        elif score_average >= 80 and score_average < 90:
            return 'E'
        elif score_average >= 70 and score_average < 80:
            return 'A'
        elif score_average >= 55 and score_average < 70:
            return 'P'
        elif score_average >= 40 and score_average < 55:
            return 'D'
        elif score_average < 40:
            return 'T'
        else:
            return None

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
