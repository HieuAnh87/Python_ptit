n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(int(i) for i in input().split()))
maxx = a[0][0]
minn = a[0][0]
for i in range(n):
    for j in range(m):
        minn = min(minn, a[i][j])
        maxx = max(maxx, a[i][j])

check = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == maxx-minn:
            if check == 0: print(a[i][j])
            print(f"Vi tri [{i}][{j}]")
            check = 1
if check == 0:
    print("NOT FOUND")