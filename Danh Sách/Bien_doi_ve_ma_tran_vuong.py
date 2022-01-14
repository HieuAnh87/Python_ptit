n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))

nm = []
mn = []
N = n
M = m
if n > m:
    for i in range(0, n, 2):
        nm.append(i)
        n -= 1
        if n == m: break
if m > n:
    for i in range(1, m, 2):
        mn.append(i)
        m -= 1
        if n == m: break

for i in range(N):
    if i in nm: continue
    for j in range(M):
        if j in mn: continue
        print(a[i][j], end= " ")
    print()