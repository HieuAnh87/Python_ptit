import math
n = int(input())
res = 0
row = [0]*n
col = [0]*n
for i in range(n):
    a = input()
    for j in range(len(a)):
        if a[j] == 'C':
            row[i] += 1
            col[j] += 1
for i in row:
    if i>=2: res += math.comb(i,2)
for i in col:
    if i>=2: res += math.comb(i,2)
print(res)