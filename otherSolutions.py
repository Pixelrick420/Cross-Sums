'''
BACKTRACKING SOLUTION
'''

# from random import randint, sample, shuffle
# from typing import Set, List, Tuple

# class Board:
#     def __init__(self, n: int) -> None:
#         self.n = n
#         self.matrix = [[randint(1, 9) for _ in range(n)] for _ in range(n)]
#         self.rowSums = [0] * n
#         self.colSums = [0] * n
#         self.answer = self.generateAnswer()
#         self.solution: Set[Tuple[int, int]] = set()

#     def generateAnswer(self) -> Set[Tuple[int, int]]:
#         answer = set()
#         for i in range(self.n):
#             for j in range(self.n):
#                 if randint(1, 10) <= 2:
#                     answer.add((i, j))
#                     self.rowSums[i] += self.matrix[i][j]
#                     self.colSums[j] += self.matrix[i][j]
        
#         rows = list(range(self.n))
#         cols = set(range(self.n))
        
#         rows = [i for i in range(self.n)]
#         cols = [i for i in range(self.n)]
#         shuffle(rows)
#         shuffle(cols)
#         for _ in range(self.n):
#             i = rows.pop()
#             j = cols.pop()
#             if (i, j) not in answer:
#                 answer.add((i, j))
#                 self.rowSums[i] += self.matrix[i][j]
#                 self.colSums[j] += self.matrix[i][j]
#         return answer

#     def display(self) -> None:
#         print('\n')
#         width = max(len(str(num)) for row in self.matrix for num in row) + 2     
#         for i, row in enumerate(self.matrix):
#             print('\t' + ''.join(f"{str(x):>{width}}" for x in row) + f"    {self.rowSums[i]}")
#         print('\n\t' + ''.join(f"{str(x):>{width}}" for x in self.colSums))
#         print('\n')

#     def solve(self) -> None:
#         positions = [(i, j) for i in range(self.n) for j in range(self.n)]
#         curSums = {'row': [0] * self.n, 'col': [0] * self.n}
#         self.backtrack(positions, 0, set(), curSums)

#     def backtrack(self, positions: List[Tuple[int, int]], index: int, curSolution: Set[Tuple[int, int]], curSums: dict) -> bool:
#         if index >= len(positions):
#             if (curSums['row'] == self.rowSums and curSums['col'] == self.colSums):
#                 self.solution = curSolution.copy()
#                 return True
#             return False

#         row, col = positions[index]
#         value = self.matrix[row][col]

#         if (curSums['row'][row] + value <= self.rowSums[row] and curSums['col'][col] + value <= self.colSums[col]):
#             curSums['row'][row] += value
#             curSums['col'][col] += value
#             curSolution.add((row, col))
            
#             if self.backtrack(positions, index + 1, curSolution, curSums):
#                 return True
                
#             curSums['row'][row] -= value
#             curSums['col'][col] -= value
#             curSolution.remove((row, col))

#         return self.backtrack(positions, index + 1, curSolution, curSums)

#     def maskSolution(self) -> None:
#         for i in range(self.n):
#             for j in range(self.n):
#                 if (i, j) not in self.solution:
#                     self.matrix[i][j] = 'X'
    
#     def check(self):
#         self.maskSolution()
#         curRowSums = [0] * self.n
#         curColSums = [0] * self.n 
#         for i in range(self.n):
#             for j in range(self.n):
#                 if self.matrix[i][j] != 'X':
#                     curRowSums[i] += self.matrix[i][j]
#                     curColSums[j] += self.matrix[i][j]  

#         return (curColSums == self.colSums) and (curRowSums == self.rowSums)           

# def main() -> bool:
#     board = Board(6)
#     #board.display()
#     board.solve()
#     #board.maskSolution()
#     #board.display()
#     return board.check()

# if __name__ == '__main__':
#     tcount, fcount = 0, 0
#     while True:
#         outcome = main() 
#         if outcome:
#             tcount += 1
#         else:
#             fcount += 1
#         print(outcome, tcount, fcount, fcount + tcount)


'''
USERINPUT FILE
'''

# import random
# import copy
# import time

# class Board:
#     def __init__(self, n):
#         self.n = n
#         self.answer = set()
#         self.rowSums = [0] * n
#         print("Enter Row Sums : ")
#         for i in range(n):
#             self.rowSums[i] = int(input(" , "))
            
#         self.colSums = [0] * n
#         print("Enter Col Sums : ")
#         for i in range(n):
#             self.colSums[i] = int(input(" , "))
            
#         self.matrix = self.matrix = [[0 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 self.matrix[i][j] = int(input(">>"))
#             print()
        
#         self.answerCopy = copy.deepcopy(self.matrix)
        
#     def display(self) -> None:
#         print('\n')
#         width = max(len(str(num)) for row in self.matrix for num in row) + 2     
#         for i, row in enumerate(self.matrix):
#             print('\t' + ''.join(f"{str(x):>{width}}" for x in row) + f"    {self.rowSums[i]}")
#         print('\n\t' + ''.join(f"{str(x):>{width}}" for x in self.colSums))
#         print('\n')
    
#     def sums(self, array, target):
#         out = set()
        
#         def f(curSum, index, sub):
#             if curSum == target:
#                 out.add(sub)
#                 return
#             if index >= len(array):
#                 return
#             if curSum < target and array[index] != 'X':
#                 f(curSum + array[index], index + 1, sub + ((array[index], index),))
#             f(curSum, index + 1, sub)

#         f(0, 0, tuple())
#         return out
    
#     def solve(self):
#         total = set(i for i in range(self.n))
#         print("Total = ",total)
        
#         for i in range(self.n):
#             possible = list(self.sums(self.matrix[i], self.rowSums[i]))
#             print("\nPossible = ",possible)
#             print("Length of Possible :: ",len(possible))
            
#             # CHANGES
#             if (len(possible) == 1):
#                 if possible != [()]:
#                     for solution in possible:
#                         for kk in solution:
#                             self.answer.add((i,kk[1]))
#                             self.rowSums[i] -= kk[0]
#                             print("CONFIRMED :: ",kk[0])
#                             self.colSums[kk[1]] -= kk[0]
#                             self.matrix[i][kk[1]] = 'X'
            
#             cols = set()
#             print("cols = ",cols)
#             for solution in possible:
#                 cols.update([j for (_, j) in solution])
#             discard = list(total.difference(cols))
#             print("discard = ",discard)
#             for col in discard:
#                 self.matrix[i][col] = 'X'
        
#         print("ANSWER : ",self.answer)
        
#         self.display()
#         transposed_matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]
        
#         print(transposed_matrix)

#         for j in range(self.n):
#             possible = list(self.sums(transposed_matrix[j], self.colSums[j]))
#             print("\nPossible = ",possible)
            
#             print("Length of Possible :: ",len(possible))
            
#             # CHANGES
#             if (len(possible) == 1):
#                 if possible != [()]:
#                     for solution in possible:
#                         for row in solution:
#                             self.answer.add((row[1],j))
#                             self.rowSums[row[1]] -= row[0]
#                             print("CONFIRMED :: ",row[0])
#                             self.colSums[j] -= row[0]
#                             self.matrix[row[1]][j] = 'X'
            
#             rows = set()
#             print("rows = ",rows)
#             for solution in possible:
#                 rows.update([i for (_, i) in solution])
#             discard = list(total.difference(rows))
#             print("discard = ",discard)
#             for row in discard:
#                 self.matrix[row][j] = 'X'
                
#         self.display()
        
#         a = list(self.answer)
#         a.sort()
#         print("FINAL ANSWER : ",a)
    
#     def check(self):
#         return self.rowSums == [0] * self.n and self.colSums == [0] * self.n

#     def finalDisplay(self):
#         a = list(self.answer)
#         for i in range(self.n):
#             for j in range(self.n):
#                 if (i,j) in a:
#                     print(self.answerCopy[i][j],end = "  ")
#                 else:
#                     print("X  ",end="")
#             print()

# def main():
#     board = Board( int(input("Enter n : ")))
#     count = 0
#     board.display()
#     inTime = time.time()
#     while not board.check():
#         print("SOLUTION CYCLE ",count," ------->>>>> ")
#         board.solve()
#         count += 1
#     outTime = time.time()
#     board.finalDisplay()
#     print("TIME CONSUMED : ",outTime-inTime," seconds")

# if __name__ == '__main__':
#     main()

'''
idk final.py file
'''

# import random
# import copy

# class Board:
#     def __init__(self, n):
#         self.answer = set()
#         self.n = 7
#         self.matrix = [
#             [2,7,9,2,7,4,7],
#             [7,7,9,1,5,6,2],
#             [3,3,6,1,7,9,3],
#             [7,1,7,6,4,3,5],
#             [4,5,2,1,7,7,7],
#             [9,7,6,4,9,6,6],
#             [8,8,5,7,3,7,1]
#         ]
#         self.rowSums = [16,16,11,29,16,6,8]
#         self.colSums = [14,4,33,14,21,3,13]
        
#         self.answerCopy = copy.deepcopy(self.matrix)
        
#     def display(self) -> None:
#         print('\n')
#         width = max(len(str(num)) for row in self.matrix for num in row) + 2     
#         for i, row in enumerate(self.matrix):
#             print('\t' + ''.join(f"{str(x):>{width}}" for x in row) + f"    {self.rowSums[i]}")
#         print('\n\t' + ''.join(f"{str(x):>{width}}" for x in self.colSums))
#         print('\n')
    
#     def sums(self, array, target):
#         out = set()
        
#         def f(curSum, index, sub):
#             if curSum == target:
#                 out.add(sub)
#                 return
#             if index >= len(array):
#                 return
#             if curSum < target and array[index] != 'X':
#                 f(curSum + array[index], index + 1, sub + ((array[index], index),))
#             f(curSum, index + 1, sub)

#         f(0, 0, tuple())
#         return out
    
#     def solve(self):
#         total = set(i for i in range(self.n))
#         print("Total = ",total)
        
#         for i in range(self.n):
#             possible = list(self.sums(self.matrix[i], self.rowSums[i]))
#             print("\nPossible = ",possible)
#             print("Length of Possible :: ",len(possible))
            
#             # CHANGES
#             if (len(possible) == 1):
#                 if possible != [()]:
#                     for solution in possible:
#                         for kk in solution:
#                             self.answer.add((i,kk[1]))
#                             self.rowSums[i] -= kk[0]
#                             print("CONFIRMED :: ",kk[0])
#                             self.colSums[kk[1]] -= kk[0]
#                             self.matrix[i][kk[1]] = 'X'
            
#             cols = set()
#             print("cols = ",cols)
#             for solution in possible:
#                 cols.update([j for (_, j) in solution])
#             discard = list(total.difference(cols))
#             print("discard = ",discard)
#             for col in discard:
#                 self.matrix[i][col] = 'X'
        
#         print("ANSWER : ",self.answer)
        
#         self.display()
#         transposed_matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.n)]
        
#         print(transposed_matrix)

#         for j in range(self.n):
#             possible = list(self.sums(transposed_matrix[j], self.colSums[j]))
#             print("\nPossible = ",possible)
            
#             print("Length of Possible :: ",len(possible))
            
#             # CHANGES
#             if (len(possible) == 1):
#                 if possible != [()]:
#                     for solution in possible:
#                         for row in solution:
#                             self.answer.add((row[1],j))
#                             self.rowSums[row[1]] -= row[0]
#                             print("CONFIRMED :: ",row[0])
#                             self.colSums[j] -= row[0]
#                             self.matrix[row[1]][j] = 'X'
            
#             rows = set()
#             print("rows = ",rows)
#             for solution in possible:
#                 rows.update([i for (_, i) in solution])
#             discard = list(total.difference(rows))
#             print("discard = ",discard)
#             for row in discard:
#                 self.matrix[row][j] = 'X'
                
#         self.display()
        
#         a = list(self.answer)
#         a.sort()
#         print("FINAL ANSWER : ",a)
    
#     def check(self):
#         return self.rowSums == [0] * self.n and self.colSums == [0] * self.n

#     def finalDisplay(self):
#         a = list(self.answer)
#         for i in range(self.n):
#             for j in range(self.n):
#                 if (i,j) in a:
#                     print(self.answerCopy[i][j],end = "  ")
#                 else:
#                     print("X  ",end="")
#             print()

# def main():
#     board = Board(6)
#     count = 0
#     board.display()
#     while not board.check():
#         print("SOLUTION CYCLE ",count," ------->>>>> ")
#         board.solve()
#         count += 1

#     board.finalDisplay()

# if __name__ == '__main__':
#     main()

