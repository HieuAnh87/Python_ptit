def up(a):
    x = 0
    res = 0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            res = res + a[i][j]
    return res

def down(a):
    res = 0
    for i in range(0, len(a)):
        for j in range(len(a)-1-i, len(a)-1):
            # print(i, j+1)
            res = res + a[i][j+1]
            # print(a[i][j+1])
    return res

def run():
    n = int(input())
    a = [[int(i) for i in input().split()] for i in range(n)]
    k = int(input())
    res = abs(up(a) - down(a))
    if res <= k:
        print("YES")
    else:
        print("NO")
    print(res)
run()