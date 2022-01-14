n = int(input())
a = [float(i) for i in input().split()]
a.sort()
count = 0
sum = 0
for i in range(1, n):
    if a[i] != a[0] and a[i] != a[n-1]:
        count += 1
        sum += a[i]
print("{:.2f}".format(float(sum/count)))