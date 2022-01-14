import math
def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def run():
    n,m = [int(i) for i in input().split()]
    # n = 6
    # m = 4
    a = [[int(i) for i in input().split()] for j in range(n)]
    res = 0
    # a = [[23, 21, 26, 10], [13, 13, 22, 14], [28, 29, 28, 23], [29, 19, 11, 19], [16, 26, 24, 21], [13, 25, 21, 29]]
    for i in range(n):
        for j in range(m):
            if isPrime(a[i][j]):
                res = max(res, a[i][j])
    if res == 0:
        print("NOT FOUND")
        return
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f"Vi tri [{i}][{j}]")
run()