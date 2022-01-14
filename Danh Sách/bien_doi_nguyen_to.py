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
    minn = 0
    for i in a:
        tmp = 0
        if isPrime(i) == False:
            r = i
            while isPrime(r) == False:
                r += 1
            l = i
            if l < 2:
                l = 2
            else:
                while isPrime(l) == False:
                    l -= 1
            # print(l, r)
            tmp = min(abs(r - i), abs(l - i))
            minn = max(tmp, minn)
    print(minn)
run()