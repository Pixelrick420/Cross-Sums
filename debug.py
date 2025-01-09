from random import randint, sample, shuffle
from typing import Set, List, Tuple

class Board:
    def __init__(self, n: int) -> None:
        self.n = n
        self.matrix = [[randint(1, 9) for _ in range(n)] for _ in range(n)]
        self.rowSums = [0] * n
        self.colSums = [0] * n
        self.answer = self.generateAnswer()
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
        self.backtrack(positions, 0, set(), curSums)

    def backtrack(self, positions: List[Tuple[int, int]], index: int, curSolution: Set[Tuple[int, int]], curSums: dict) -> bool:
        if index >= len(positions):
            if (curSums['row'] == self.rowSums and curSums['col'] == self.colSums):
                self.solution = curSolution.copy()
                return True
            return False

        row, col = positions[index]
        value = self.matrix[row][col]

        if (curSums['row'][row] + value <= self.rowSums[row] and curSums['col'][col] + value <= self.colSums[col]):
            curSums['row'][row] += value
            curSums['col'][col] += value
            curSolution.add((row, col))
            
            if self.backtrack(positions, index + 1, curSolution, curSums):
                return True
                
            curSums['row'][row] -= value
            curSums['col'][col] -= value
            curSolution.remove((row, col))

        return self.backtrack(positions, index + 1, curSolution, curSums)

    def maskSolution(self) -> None:
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) not in self.solution:
                    self.matrix[i][j] = 'X'
    
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
    board = Board(6)
    #board.display()
    board.solve()
    #board.maskSolution()
    #board.display()
    return board.check()

if __name__ == '__main__':
    tcount, fcount = 0, 0
    while True:
        outcome = main() 
        if outcome:
            tcount += 1
        else:
            fcount += 1
        print(outcome, tcount, fcount, fcount + tcount)