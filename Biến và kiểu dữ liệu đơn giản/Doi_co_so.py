t = int(input())
sample = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(t):
    n, b = [int(x) for x in input().split()]
    s = ""
    if b >= 2 and b <= 36:
        while n != 0:
            s = sample[n%b] + s
            n = int(n/b)
        print(s)