def run():
    n = int(input())
    upper = 0
    lower = 0
    for i in range(n):
        x = [int(i) for i in input().split()]
        for j in range(0, n - i - 1):
            upper += x[j]
        for j in range(n - i, n):
            lower += x[j]
    temp = abs(upper - lower)
    k = int(input())
    if (temp <= k):
        print("YES")
    else:
        print("NO")
    print(temp)
run()