class Matran():
    def __init__(self,n,m,a):
        self.n = n
        self.m = m
        self.a = a

    def cvi(self):
        A = self.a
        B = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
        res = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        for i in range(len(res)):
            print(*res[i])

def run():
    n,m = map(int, input().split())
    a = [[int(i) for i in input().split()] for j in range(n)]
    Matrix = Matran(n,m,a)
    Matrix.cvi()
def main():
    t = int(input())
    for i in range(t):
        run()
main()