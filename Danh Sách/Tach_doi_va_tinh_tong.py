n = input()
k = len(n)
while k > 1:
    m = int(k / 2)
    h1 = ""
    h2 = ""
    for i in range(0, m):
        h1 += n[i]
    for i in range(m, len(n)):
        h2 += n[i]
    res = str(int(h1) +int(h2))
    n = res
    k = len(n)
    print(res)