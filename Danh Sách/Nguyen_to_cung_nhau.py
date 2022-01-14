def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if gcd(int(a[i]), int(a[j])) == 1:
                print(a[i], a[j])
main()