import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def run():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()