n, m = map(int, input().split())
a = [int(i) for i in input().split()]
count = {}
maxx = -1
for i in a:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
maxx = max(count.values())
res = -1
pos = -1
for i in range(0, len(a)):
    if count[a[i]] > res and count[a[i]] < maxx:
        res = count[a[i]]
        pos = a[i]
if pos == -1:
    print("NONE")
else: 
    print(pos)
