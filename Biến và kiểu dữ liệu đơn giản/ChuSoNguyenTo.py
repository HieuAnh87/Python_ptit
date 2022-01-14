import math
def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def Check(n):
    count = 0
    for i in n:
        if isPrime(int(i)):
            count+=1
    if len(n) - count < count: return True
    return False

def run():
    s = input()
    if isPrime(len(s)) and Check(s):
        print("YES")
    else:
        print("NO")
        
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()
