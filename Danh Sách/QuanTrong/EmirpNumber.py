import math
def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def run():
    n = int(input())
    # n = 40
    a = []
    prime = [1]*(n+1)
    for i in range(10,n):
        if isPrime(i):
            prime[i] = 0

    for i in range(10,n):
        j = int(str(i)[::-1])
        if isPrime(i) and j != i and isPrime(j) and j<n and prime[j]==0:
            print(i,j,end=" ")
            prime[j] = 1
            prime[i] = 1
    print()
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()