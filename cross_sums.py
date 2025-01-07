import random

class Board:
    def __init__ (self, n):
        self.n = n
        self.answer = set()
        self.rowSums = [0] * n
        self.colSums = [0] * n
        self.matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.matrix[i][j] = random.randint(1, 9)
                if(random.randint(1, 10)) <= 2:
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
            if(i, j) not in self.answer:
                self.answer.add((i, j))
                self.rowSums[i] += self.matrix[i][j]
                self.colSums[j] += self.matrix[i][j]


    def display(self):
        def displayRow(array):
            print('\t', end='')
            for val in array:
                print(val, end=(' ' * (6 - len(str(val)))))
            print()
        for row in self.matrix:
            displayRow(row)
        
        print(self.rowSums)
        print(self.colSums)
    
    def sums(self, array, target):
        out = set()
        def f(curSum, index, sub):
            if(curSum == target):
                out.add(sub)
                return
            elif index >= len(array):
                return
            elif curSum < target:
                f(curSum + array[index], index + 1, sub + ((array[index], index),) )
                f(curSum, index + 1, sub)
        f(0, 0, tuple())
        return out
    
    def solve(self):
        total = set(i for i in range(self.n))
        for i in range(self.n):
            possible = list(self.sums(self.matrix[i], self.rowSums[i]))
            cols = set()
            for solution in possible:
                cols.update([j for (i, j) in solution])
            discard = list(total.difference(cols))
            for col in discard:
                self.matrix[i][col] = 'X'
            

def main():
    board = Board(6)
    board.display()
    board.solve()
    board.display()

if __name__ == '__main__':
    main()

