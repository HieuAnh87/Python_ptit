def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if gcd(a[i], a[j]) == 1:
                print(a[i], a[j])
run()
