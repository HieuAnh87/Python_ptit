def biggestPow(n,p):
    res = 0
    while(n>0):
        n /= p
        print(res)
        res += int(n)
    print(res)

def main():
    t  =int(input())
    for i in range(t):
        n,p = map(int, input().split())
        biggestPow(n,p)
main()

# Tìm x lớn nhất để n! chia hết cho p^x:

