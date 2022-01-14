import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def run():
    s = input()
    prime = 0
    for i in s:
        if isPrime(int(i)):
            prime += 1
    nonprime = len(s) - prime
    if isPrime(len(s)) and prime > nonprime: 
        print("YES")
    else: 
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()
main()