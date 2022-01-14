import math
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def run():
    n = input()
    for i in range(0, len(n)-1):
        if isPrime(int(n[i])) == False and isPrime(i) == True:
            print("NO")
            return
        if isPrime(int(n[i])) == True and isPrime(i) == False:
            print("NO")
            return           
    print("YES")

def main():
    t = int(input())
    for i in range(t):
        run()
main()