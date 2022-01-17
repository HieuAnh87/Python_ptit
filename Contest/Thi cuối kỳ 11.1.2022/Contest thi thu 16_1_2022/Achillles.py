from math import sqrt, log
def check_powerful(n):
    while(n%2==0):
        p=0
        while(n%2==0):
            n/=2
            p+=1
        if p==1: return False
    p =int(sqrt(n))+1
    for factor in range(3,p,2):
        p=0
        while(n%factor == 0):
            n /= factor
            p += 1
        if p==1: return False
    return (n==1)
def check_power(a):
    if a == 1: return True
    p = int(sqrt(a)) + 1
    for i in range(2,a,1):
        val = log(a) / log(i)
        if ((val - int(val)) < 0.00000001):
            return True
        return False
    
def isAchilles(n):
    if check_powerful(n) and check_power(n) == False:
        print(0)
        return
    print(1)
n =int(input())
isAchilles(n)
