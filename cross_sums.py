import random

class Board:
    def __init__(self, n):
        self.n = n
        self.answer = set()
        self.rowSums = [0] * n
        self.colSums = [0] * n
        self.solution = set()
        self.matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.matrix[i][j] = random.randint(1, 9)
                if random.randint(1, 10) <= 2:
                    self.answer.add((i, j))
                    self.rowSums[i] += self.matrix[i][j]
                    self.colSums[j] += self.matrix[i][j]

        rows = [i for i in range(n)]
        cols = [i for i in range(n)]
        random.shuffle(rows)
        random.shuffle(cols)
        for _ in range(n):
            i = rows.pop()
            j = cols.pop()
            if (i, j) not in self.answer:
                self.answer.add((i, j))
                self.rowSums[i] += self.matrix[i][j]
                self.colSums[j] += self.matrix[i][j]

    def display(self):
        print('\n')
        def displayRow(array, row, isSum = False):
            print('\t', end='')
            for i in range(len(array)):
                print(array[i], end=(' ' * (6 - len(str(array[i])))))
            if not isSum:
                print('   ', self.rowSums[row])
            else:
                print()
        for i in range(self.n):
            displayRow(self.matrix[i], i)
        print()
        displayRow(self.colSums, 0, True)
        print('\n')
    
    def sums(self, array, target):
        if target == 0:
            return
            
        out = set()
        
        def f(curSum, index, sub):
            if curSum == target:
                out.add(sub)
                return
            if index >= len(array):
                return
            if curSum < target and array[index] != 'X':
                f(curSum + array[index], index + 1, sub + (index,))
            f(curSum, index + 1, sub)

        f(0, 0, tuple())
        return out
    
    def solve(self):
        total = set(i for i in range(self.n))
        
        order = list(range(self.n))
        random.shuffle(order)
        for row in order:
            if self.rowSums[row] > 0:
                possible = list(self.sums(self.matrix[row], self.rowSums[row]))
                cols = set()

                if len(possible) == 1:
                    confirm = [(row,col) for col in possible[0]]
                    self.solution.update(confirm)

                for solution in possible:
                    cols.update([col for col in solution])
                discard = list(total.difference(cols))
                for col in discard:
                    self.matrix[row][col] = 'X'
        
        transposedMatrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]
        random.shuffle(order)
        for col in order:
            if self.colSums[col] > 0:
                possible = list(self.sums(transposedMatrix[col], self.colSums[col]))
                rows = set()

                if len(possible) == 1:
                    confirm = [(row,col) for row in possible[0]]
                    self.solution.update(confirm)

                for solution in possible:
                    rows.update([row for row in solution])
                discard = list(total.difference(rows))
                for row in discard:
                    self.matrix[row][col] = 'X'

    def check(self):
        return self.answer == self.solution

def main():
    board = Board(6)
    
    board.display()
    board.solve()
    board.solve()
    board.solve()
    board.solve()
    board.solve()
    board.solve()
    board.display()
    print(board.solution)
    print(board.check())

if __name__ == '__main__':
    main()