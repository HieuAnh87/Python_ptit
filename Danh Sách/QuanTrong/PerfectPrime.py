import math
def isPrime(n):
    n = int(n)
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def isReversed(n):
    s = n[::-1]
    if isPrime(s): return True
    return False
def isSumofDigit(n):
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    if isPrime(summ): return True
    return False
def isDigit(n):
    for i in range(len(n)):
        if isPrime(n[i]) == False:
            return False
    return True

def run():
    n = input()
    if isPrime(n)==True and isReversed(n)==True and isSumofDigit(n)==True and isDigit(n)==True:
        print("Yes")
        return
    print("No")

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()