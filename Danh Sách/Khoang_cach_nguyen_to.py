import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
Prime = [2]
so = 2
while (len(Prime) < 1000):
    so += 1
    if (isPrime(so)):
        Prime.append(so)

n, m = map(int, input().split())
for i in range(0, n):
    print(m, end = " ")
    m = m + Prime[i]
print(m)
