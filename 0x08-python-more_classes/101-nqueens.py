#!/usr/bin/python3
''' Implements and solves the N queens puzzle
    Finds all possible solutions to placing N
    Backtracks any other paths that cause the queens to attack
    Usage:
        nqueens N
    Attributes:
        __init__ : initialises instances
        backtrack: solves the problem
'''

import sys
''' Module for sys functions '''


class Nqueens:
    ''' Finds viable positions for a queen so that none attack each other '''
    def __init__(self):
        ''' Initializes an instance for class '''
        self.cSet = set()
        self.posDSet = set()
        self.negDSet = set()
        self.answer = []
        self.chessboard = []

    def backtrack(self, r):
        ''' Find a good position and return co-ordinates on the chessboard.
            r: row in question
        '''
        if r == self.N:
            self.answer.append(self.chessboard[:])
            solutions.append(self.chessboard[:])
            return

        for c in range(self.N):
            if c not in self.cSet and (r + c) not in self.posDSet:
                if (r - c) not in self.negDSet:
                    self.cSet.add(c)
                    self.posDSet.add(r + c)
                    self.negDSet.add(r - c)
                    self.chessboard.append([r, c])

                    self.backtrack(r + 1)

                    self.cSet.remove(c)
                    self.posDSet.remove(r + c)
                    self.negDSet.remove(r - c)
                    self.chessboard.pop()


nqueens = Nqueens()
solutions = []  # Initialize an empty list to store the solutions

if __name__ == "__main__":
    ''' main method to read command line arguments '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens.N = n
    nqueens.backtrack(0)
    answer = nqueens.answer
    for i in range(len(solutions)):
        print(solutions[i])  # Print the list of solutions
