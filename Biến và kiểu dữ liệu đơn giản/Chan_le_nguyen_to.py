import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def Check(n):
    for i in range(0, int(len(n))-1):
        if int(n[i]) % 2 != 0 and i % 2 == 0:
            return False
        if int(n[i]) % 2 == 0 and i % 2 != 0:
            return False
    return True

def run():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if isPrime(sum) and Check(n):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()
main()
