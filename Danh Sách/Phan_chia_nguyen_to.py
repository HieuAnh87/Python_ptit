import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    # print(b)
    for i in range(1,len(b)): # tong tu b[0] -> b[i]
        b[i] += b[i-1]
    for i in range(0, len(b)):
        if isPrime(b[i]) and isPrime(b[len(b)-1] - b[i]):
            print(i)
            return
    print("NOT FOUND")
run()