import math
def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

def gcd(a,b):
    if b==0: 
        return a
    return gcd(b, a%b)

def run():
    n = int(input())
    count = 0
    for i in range(1, n):
        if gcd(i,n) == 1:
            count += 1
    if isPrime(count):
        print('YES')
    else:
        print("NO")
def main():
    t = int(input())
    for i in range(t):
        run()
main()