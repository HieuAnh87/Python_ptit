def run():
    n = int(input())
    tren = 0
    duoi = 0
    for i in range(n):
        a = [int(i) for i in input().split()]
        for j in range(i + 1, n):
            tren += a[j]
        for j in range(0, i):
            duoi += a[j]
    sum = abs(tren - duoi)
    k = int(input())
    if sum <= k:
        print("YES")
    else:
        print("NO")
    print(sum)
run()