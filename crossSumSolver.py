"""
MODULE: CROSS-SUMS SOLVER

This module provides functionality to solve cross-sum puzzles. 
The main feature is the `crossSumSolver` function, which identifies correct positions in a matrix to satisfy row and column sum constraints.

Author: Rohith Sajeev, Harikrishnan R
Date: 14 January 2025
Version: 1.0
"""

import copy

class Board:
    """
    Represents a board for solving cross-sum puzzles.

    Attributes:
        n (int): Size of the matrix (n x n).
        matrix (list): Initial matrix with numbers and placeholders ('X').
        rowSums (list): Target sums for each row.
        colSums (list): Target sums for each column.
        answer (set): Set of positions that form the solution.
        valid (bool): Validity of the board (True if dimensions and inputs are consistent).
        answerCopy (list): Deep copy of the original matrix for display purposes.
    """
    valid = True
    
    def __init__(self, n, matrix, rowSum, colSum):
        """
        Initializes the board with given dimensions, matrix, row sums, and column sums.

        Args:
            n (int): Size of the matrix.
            matrix (list): 2D list representing the puzzle matrix.
            rowSum (list): Target sums for each row.
            colSum (list): Target sums for each column.
        """
        self.n = n
        self.answer = set()
        self.rowSums = rowSum    
        self.colSums = colSum
        self.matrix = matrix
        self.answerCopy = copy.deepcopy(self.matrix)
        
        # Validate board dimensions
        if len(rowSum) != n or len(colSum) != n or len(matrix) != n:
            self.valid = False
        
    def display(self):
        """
        Displays the current state of the board with row and column sums for debugging purposes.
        """
        print('\n')
        width = max(len(str(num)) for row in self.matrix for num in row) + 2     
        for i, row in enumerate(self.matrix):
            print('\t' + ''.join(f"{str(x):>{width}}" for x in row) + f"    {self.rowSums[i]}")
        print('\n\t' + ''.join(f"{str(x):>{width}}" for x in self.colSums))
        print('\n')
        
    def sums(self, array, target):
        """
        Finds all subsets of an array whose sum equals the target.

        Args:
            array (list): Array to process.
            target (int): Target sum to achieve.

        Returns:
            set: A set of subsets, where each subset is represented as tuples of (value, index).
        """
        out = set()
        
        def f(curSum, index, sub):
            if curSum == target:
                out.add(sub)
                return
            if index >= len(array):
                return
            if curSum < target and array[index] != 'X':
                f(curSum + array[index], index + 1, sub + ((array[index], index),))
            f(curSum, index + 1, sub)

        f(0, 0, tuple())
        return out
    
    def solve(self):
        """
        Solves the cross-sum puzzle by determining correct positions iteratively.
        """
        if not self.valid:
            return
        
        total = set(i for i in range(self.n))
        
        # Solve for rows
        for i in range(self.n):
            possible = list(self.sums(self.matrix[i], self.rowSums[i]))
            
            if len(possible) == 1:
                if possible != [()]:
                    for solution in possible:
                        for col in solution:
                            self.answer.add((i, col[1]))
                            self.rowSums[i] -= col[0]
                            self.colSums[col[1]] -= col[0]
                            self.matrix[i][col[1]] = 'X'
            
            cols = set()
            for solution in possible:
                cols.update([j for (_, j) in solution])
            discard = list(total.difference(cols))
            for col in discard:
                self.matrix[i][col] = 'X'

        # Solve for columns
        transposed_matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]
        for j in range(self.n):
            possible = list(self.sums(transposed_matrix[j], self.colSums[j]))

            if len(possible) == 1:
                if possible != [()]:
                    for solution in possible:
                        for row in solution:
                            self.answer.add((row[1], j))
                            self.rowSums[row[1]] -= row[0]
                            self.colSums[j] -= row[0]
                            self.matrix[row[1]][j] = 'X'
            
            rows = set()
            for solution in possible:
                rows.update([i for (_, i) in solution])
            discard = list(total.difference(rows))
            for row in discard:
                self.matrix[row][j] = 'X'
                
    def check(self):
        """
        Validates if all row and column sums are satisfied.

        Returns:
            bool: True if solved, False otherwise.
        """
        return self.rowSums == [0] * self.n and self.colSums == [0] * self.n

    def finalDisplay(self):
        """
        Displays the solved board with only the solution positions.
        """
        a = list(self.answer)
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) in a:
                    print(self.answerCopy[i][j], end="  ")
                else:
                    print("X  ", end="")
            print()
            
def crossSumSolver(n, questionMatrix, rowSum, columnSum):
    """
    Solves a cross-sum puzzle for the given matrix and target sums.

    Args:
        n (int): Size of the matrix.
        questionMatrix (list): 2D list representing the puzzle matrix.
        rowSum (list): Target sums for each row.
        columnSum (list): Target sums for each column.

    Returns:
        list: Sorted list of correct positions in the matrix.
    """
    board = Board(n, questionMatrix, rowSum, columnSum)
    board.solve()
    board.finalDisplay()
    a = list(board.answer)
    a.sort()
    return a
