t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    if n % 2 == 0: m = 2
    else: m = 1
    for j in range(m, n+1, 2):
        sum += 1/j
    print("{:.6f}".format(sum))
