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
    dict = {}
    for i in a:
        if isPrime(i):
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    for key,val in dict.items():
        print(str(key) + ' ' + str(val))
run()