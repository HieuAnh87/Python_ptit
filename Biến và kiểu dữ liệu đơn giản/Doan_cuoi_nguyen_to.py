import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def run():
    n = input()[-4:]
    if isPrime(int(n)):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()
main()