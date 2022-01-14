import math
def gcd(a,b):
    if b==0: return a
    return gcd(b, a % b)

def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def isDigit(a):
    sumofn = sum(map(int, str(a)))
    return sumofn

def run():
    a,b = map(int, input().split())
    if isPrime(isDigit(gcd(a,b))):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()
main()
