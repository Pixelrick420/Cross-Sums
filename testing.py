from random import randint, shuffle
import copy

class Board:
    def __init__(self, n):
        self.n = n
        self.answer = set()
        self.rowSums = [0] * n
        self.colSums = [0] * n
        self.matrix = [[randint(1, 9) for _ in range(n)] for _ in range(n)]
        self.answerCopy = copy.deepcopy(self.matrix)
        self.genAns = self.generateAnswer()
        
        self.answerCopy = copy.deepcopy(self.matrix)
        
        print(self.answerCopy)
        print(self.rowSums)
        print(self.colSums)
        
    def generateAnswer(self):
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
        #print("Total = ",total)
        
        for i in range(self.n):
            possible = list(self.sums(self.matrix[i], self.rowSums[i]))
            #print("\nPossible = ",possible)
            #print("Length of Possible :: ",len(possible))
            
            # CHANGES
            if (len(possible) == 1):
                if possible != [()]:
                    for solution in possible:
                        for kk in solution:
                            self.answer.add((i,kk[1]))
                            self.rowSums[i] -= kk[0]
                            #print("CONFIRMED :: ",kk[0])
                            self.colSums[kk[1]] -= kk[0]
                            self.matrix[i][kk[1]] = 'X'
            
            cols = set()
            #print("cols = ",cols)
            for solution in possible:
                cols.update([j for (_, j) in solution])
            discard = list(total.difference(cols))
            #print("discard = ",discard)
            for col in discard:
                self.matrix[i][col] = 'X'
        
        #print("ANSWER : ",self.answer)
        
        #self.display()
        transposed_matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]
        
        #print(transposed_matrix)

        for j in range(self.n):
            possible = list(self.sums(transposed_matrix[j], self.colSums[j]))
            #print("\nPossible = ",possible)
            
            #print("Length of Possible :: ",len(possible))
            
            # CHANGES
            if (len(possible) == 1):
                if possible != [()]:
                    for solution in possible:
                        for row in solution:
                            self.answer.add((row[1],j))
                            self.rowSums[row[1]] -= row[0]
                            #print("CONFIRMED :: ",row[0])
                            self.colSums[j] -= row[0]
                            self.matrix[row[1]][j] = 'X'
            
            rows = set()
            #print("rows = ",rows)
            for solution in possible:
                rows.update([i for (_, i) in solution])
            discard = list(total.difference(rows))
            #print("discard = ",discard)
            for row in discard:
                self.matrix[row][j] = 'X'
                
        #self.display()
    
    def check(self):
        #print(self.rowSums, self.colSums)
        return self.rowSums == [0] * self.n and self.colSums == [0] * self.n

    def finalDisplay(self):
        
        a = list(self.answer)
        a.sort()
        print("FINAL ANSWER : ",a)
        
        b = list(self.genAns)
        b.sort()
        print("GEN ANSWER : ",b)
        
        
        a = list(self.answer)
        width = max(len(str(num)) for row in self.answerCopy for num in row) + 2

        for i in range(self.n):
            print('\t')
            for j in range(self.n):
                if (i, j) in a:
                    print(f"{str(self.answerCopy[i][j]):>{width}}", end="")
                else:
                    print(f"{'X':>{width}}", end="")
    
def main():
    count = 0
    tcount = 0
    while True:
        
        it = 0
        board = Board(8)
        board.generateAnswer()
        board.display()
        
        while True:
            board.solve()
            if board.check():
                tcount += 1
                break
            if it > 15:
                print("OVER",end = "")
                break
            it += 1
            
        board.finalDisplay()
        count += 1
        
        print("Count : ",count," Work : ",tcount)
        if count == 1:
            break
        

if __name__ == '__main__':
    main()