t = int(input())
for i in range(t):
    N, X, M = input().split()
    N, X, M = float(N), float(X), float(M)
    days = 0
    while (N < M):
        days = days + 1
        N = N + N*(X/100) # chia %
    print(days)