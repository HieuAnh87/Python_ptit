import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

def countDigit(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

def main():
    t = int(input())
    while t:
        a , b = input().split()
        a = int(a)
        b = int(b)
        if isPrime(countDigit(gcd(a, b))):
            print("YES")
        else:
            print("NO")
        t -= 1
main()