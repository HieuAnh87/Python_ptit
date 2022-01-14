n = input()
a = []
if len(n) % 2 != 0: m = len(n) - 1
else: m = len(n)
for i in range(0,m,2):
    a.append(n[i]+n[i+1])
res = []
for i in a:
    if i not in res:
        res.append(i)
res.sort()
for i in res:
    print(i, end = " ")