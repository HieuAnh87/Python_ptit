import math

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def run():
    n, m = [int(i) for i in input().split()]
    a = []
    maxx = 0
    for i in range(n):
        x = [int(i) for i in input().split()]
        a.append(x)
        for j in x:
            if isPrime(j) == True:
                maxx = max(j, maxx)
    if maxx == 0:
        print("NOT FOUND")
        return
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print(f"Vi tri [{i}][{j}]")
run()