from random import randint, sample, shuffle
from typing import Set, List, Tuple
import time

class Board:
    def __init__(self, n: int) -> None:
        self.n = 7
        self.matrix = [
            [2,7,9,2,7,4,7],
            [7,7,9,1,5,6,2],
            [3,3,6,1,7,9,3],
            [7,1,7,6,4,3,5],
            [4,5,2,1,7,7,7],
            [9,7,6,4,9,6,6],
            [8,8,5,7,3,7,1]
        ]
        self.rowSums = [16,16,11,29,16,6,8]
        self.colSums = [14,4,33,14,21,3,13]
        #self.answer = self.generateAnswer()
        self.solution: Set[Tuple[int, int]] = set()

    def generateAnswer(self) -> Set[Tuple[int, int]]:
        answer = set()
        for i in range(self.n):
            for j in range(self.n):
                if randint(1, 10) <= 2:
                    answer.add((i, j))
                    self.rowSums[i] += self.matrix[i][j]
                    self.colSums[j] += self.matrix[i][j]
        
        rows = list(range(self.n))
        cols = set(range(self.n))
        
        rows = [i for i in range(self.n)]
        cols = [i for i in range(self.n)]
        shuffle(rows)
        shuffle(cols)
        for _ in range(self.n):
            i = rows.pop()
            j = cols.pop()
            if (i, j) not in answer:
                answer.add((i, j))
                self.rowSums[i] += self.matrix[i][j]
                self.colSums[j] += self.matrix[i][j]
        return answer

    def display(self) -> None:
        print('\n')
        width = max(len(str(num)) for row in self.matrix for num in row) + 2     
        for i, row in enumerate(self.matrix):
            print('\t' + ''.join(f"{str(x):>{width}}" for x in row) + f"    {self.rowSums[i]}")
        print('\n\t' + ''.join(f"{str(x):>{width}}" for x in self.colSums))
        print('\n')

    def solve(self) -> None:
        positions = [(i, j) for i in range(self.n) for j in range(self.n)]
        curSums = {'row': [0] * self.n, 'col': [0] * self.n}
        #self.reorder()
        self.backtrack(positions, 0, set(), curSums)

    # def backtrack(self, positions: List[Tuple[int, int]], index: int, curSolution: Set[Tuple[int, int]], curSums: dict) -> bool:
    #     if index >= len(positions):
    #         if (curSums['row'] == self.rowSums and curSums['col'] == self.colSums):
    #             self.solution = curSolution.copy()
    #             return True
    #         return False

    #     row, col = positions[index]
    #     value = self.matrix[row][col]

    #     if (curSums['row'][row] + value <= self.rowSums[row] and curSums['col'][col] + value <= self.colSums[col]):
    #         curSums['row'][row] += value
    #         curSums['col'][col] += value
    #         curSolution.add((row, col))
            
    #         if self.backtrack(positions, index + 1, curSolution, curSums):
    #             return True
                
    #         curSums['row'][row] -= value
    #         curSums['col'][col] -= value
    #         curSolution.remove((row, col))

    #     return self.backtrack(positions, index + 1, curSolution, curSums)
    
    def backtrack(self, positions: List[Tuple[int, int]], index: int, curSolution: Set[Tuple[int, int]], curSums: dict) -> bool:
        if index >= len(positions):
            # Check if the current solution satisfies all row and column sums
            if curSums['row'] == self.rowSums and curSums['col'] == self.colSums:
                self.solution = curSolution.copy()
                return True
            return False

        row, col = positions[index]
        value = self.matrix[row][col]

        # Skip positions marked as "X"
        if value == "X":
            return self.backtrack(positions, index + 1, curSolution, curSums)

        # Try including the current position in the solution
        if (curSums['row'][row] + value <= self.rowSums[row] and 
            curSums['col'][col] + value <= self.colSums[col]):
            
            # Add value to current sums and include position in the solution
            curSums['row'][row] += value
            curSums['col'][col] += value
            curSolution.add((row, col))
            
            # Recursively explore with the updated state
            if self.backtrack(positions, index + 1, curSolution, curSums):
                return True
            
            # Backtrack: Remove the value and position
            curSums['row'][row] -= value
            curSums['col'][col] -= value
            curSolution.remove((row, col))

        # Skip the current position and continue exploring
        return self.backtrack(positions, index + 1, curSolution, curSums)


    def maskSolution(self) -> None:
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) not in self.solution:
                    self.matrix[i][j] = 'X'
    
    def sums(self, array, target):
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
    
    def easysolve(self):
        total = set(i for i in range(self.n))
        
        for i in range(self.n):
            possible = list(self.sums(self.matrix[i], self.rowSums[i]))
            cols = set()
            for solution in possible:
                cols.update([j for (_, j) in solution])
            discard = list(total.difference(cols))
            for col in discard:
                self.matrix[i][col] = 'X'

        transposed_matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]

        for j in range(self.n):
            possible = list(self.sums(transposed_matrix[j], self.colSums[j]))
            rows = set()
            for solution in possible:
                rows.update([i for (_, i) in solution])
            discard = list(total.difference(rows))
            for row in discard:
                self.matrix[row][j] = 'X'
        
        #self.display()

    def reorder(self):
        # Sort rows based on rowSums
        row_order = sorted(range(self.n), key=lambda x: self.rowSums[x])
        self.matrix = [self.matrix[i] for i in row_order]
        self.rowSums = [self.rowSums[i] for i in row_order]

        # Sort columns based on colSums
        col_order = sorted(range(self.n), key=lambda x: self.colSums[x])
        self.matrix = [[row[i] for i in col_order] for row in self.matrix]
        self.colSums = [self.colSums[i] for i in col_order]

    
    def check(self):
        self.maskSolution()
        curRowSums = [0] * self.n
        curColSums = [0] * self.n 
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != 'X':
                    curRowSums[i] += self.matrix[i][j]
                    curColSums[j] += self.matrix[i][j]  

        return (curColSums == self.colSums) and (curRowSums == self.rowSums)           

def main() -> bool:
    board = Board(7)
    #board.display()
    for i in range(4):
        board.easysolve()
    board.solve()
    board.maskSolution()
    board.display()
    #print(board.solution)
    return board.check()

if __name__ == '__main__':
    print(main())
    # tcount, fcount = 0, 0
    # while True:
    #     inTime = time.time()
    #     outcome = main()
    #     outTime = time.time() 
    #     if outcome:
    #         tcount += 1
    #     else:
    #         fcount += 1
    #     print(outcome, tcount, fcount, fcount + tcount,outTime-inTime)
