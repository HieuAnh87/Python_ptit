t = int(input())
for t in range(t):
    n = int(input())
    a = list(int(i) for i in input().split())
    b = list(int(i) for i in input().split())
    a.sort()
    b.sort()
    check = 'YES'
    for i in range(0, n):
        if a[i] > b[i]:
            check = 'NO'
            break
    print(check)