from crossSumSolver import crossSumSolver

def main():
    n = int(input("Enter n \t:: "))
    
    rS = [0] * n
    cS = [0] * n
    print("Enter row sums :: \n")
    for i in range(n):
        rS[i] = int(input(" , "))
    print("Enter column sums :: \n")
    for i in range(n):
        cS[i] = int(input(" , "))
    
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
            for j in range(n):
                matrix[i][j] = int(input(">>"))
            print()

    answerSet = crossSumSolver(n,matrix,rS,cS)
    print(answerSet)
    
if __name__ == '__main__':
    main()