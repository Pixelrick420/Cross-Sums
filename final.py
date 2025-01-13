import random
import copy

class Board:
    def __init__(self, n):
        self.n = 8
        self.answer = set()
        self.rowSums = [13,23,24,5,9,5,16,2]
        self.colSums = [4,8,15,10,3,16,16,25]
        self.matrix = [
                    [4,2,5,6,3,2,6,5],
                    [1,2,9,5,6,3,5,2],
                    [4,2,6,3,5,7,5,4],
                    [2,1,9,3,4,5,1,8],
                    [2,3,8,8,5,7,2,6],
                    [6,5,5,3,5,5,4,5],
                    [5,1,1,5,1,2,9,7],
                    [7,2,4,2,2,4,1,6]
                ]
        
        self.answerCopy = copy.deepcopy(self.matrix)
        
    def display(self) -> None:
        print('\n')
        width = max(len(str(num)) for row in self.matrix for num in row) + 2     
        for i, row in enumerate(self.matrix):
            print('\t' + ''.join(f"{str(x):>{width}}" for x in row) + f"    {self.rowSums[i]}")
        print('\n\t' + ''.join(f"{str(x):>{width}}" for x in self.colSums))
        print('\n')
    
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
    
    def solve(self):
        total = set(i for i in range(self.n))
        print("Total = ",total)
        
        for i in range(self.n):
            possible = list(self.sums(self.matrix[i], self.rowSums[i]))
            print("\nPossible = ",possible)
            print("Length of Possible :: ",len(possible))
            
            # CHANGES
            if (len(possible) == 1):
                if possible != [()]:
                    for solution in possible:
                        for kk in solution:
                            self.answer.add((i,kk[1]))
                            self.rowSums[i] -= kk[0]
                            print("CONFIRMED :: ",kk[0])
                            self.colSums[kk[1]] -= kk[0]
                            self.matrix[i][kk[1]] = 'X'
            
            cols = set()
            print("cols = ",cols)
            for solution in possible:
                cols.update([j for (_, j) in solution])
            discard = list(total.difference(cols))
            print("discard = ",discard)
            for col in discard:
                self.matrix[i][col] = 'X'
        
        print("ANSWER : ",self.answer)
        
        self.display()
        transposed_matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]
        
        print(transposed_matrix)

        for j in range(self.n):
            possible = list(self.sums(transposed_matrix[j], self.colSums[j]))
            print("\nPossible = ",possible)
            
            print("Length of Possible :: ",len(possible))
            
            # CHANGES
            if (len(possible) == 1):
                if possible != [()]:
                    for solution in possible:
                        for row in solution:
                            self.answer.add((row[1],j))
                            self.rowSums[row[1]] -= row[0]
                            print("CONFIRMED :: ",row[0])
                            self.colSums[j] -= row[0]
                            self.matrix[row[1]][j] = 'X'
            
            rows = set()
            print("rows = ",rows)
            for solution in possible:
                rows.update([i for (_, i) in solution])
            discard = list(total.difference(rows))
            print("discard = ",discard)
            for row in discard:
                self.matrix[row][j] = 'X'
                
        self.display()
        
        a = list(self.answer)
        a.sort()
        print("FINAL ANSWER : ",a)
    
    def check(self):
        return self.rowSums == [0] * self.n and self.colSums == [0] * self.n

    def finalDisplay(self):
        a = list(self.answer)
        for i in range(self.n):
            for j in range(self.n):
                if (i,j) in a:
                    print(self.answerCopy[i][j],end = "  ")
                else:
                    print("X  ",end="")
            print()

def main():
    board = Board(6)
    count = 0
    board.display()
    while not board.check():
        print("SOLUTION CYCLE ",count," ------->>>>> ")
        board.solve()
        count += 1

    board.finalDisplay()

if __name__ == '__main__':
    main()