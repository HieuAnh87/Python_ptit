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
    prime = []
    for i in a:
        if isPrime(i):
            prime.append(i)
    prime.sort()
    pos = 0
    for i in range(n):
        if isPrime(a[i]):
            print(prime[pos], end = ' ')
            pos += 1
        else:
            print(a[i], end= ' ')
run()