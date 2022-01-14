count = 0
a, k, n = map(int, input().split())

st = (int(a/k) + 1) * k

for i in range(st, n+1, k):
    print(i-a, end = ' ')
    count += 1
if count == 0:
    print(-1)
