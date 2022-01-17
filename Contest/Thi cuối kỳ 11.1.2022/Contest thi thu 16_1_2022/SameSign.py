n = int(input())
a = [int(i) for i in input().split()]

ds = []
for i in range(0, n-1):
    if a[i]*a[i+1]>0:
        ds.append([a[i], a[i+1]])

if len(ds) >0:
    print(len(ds), end=" ")
    print(*ds[-1])
else: print(0)
