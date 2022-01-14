def up(a):
    x = 0
    res = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            res = res + a[i][j]
    return res

def down(a):
    res = 0
    for i in range(len(a)-1):
        for j in range(i+1):
            res = res + a[i+1][j]
    return res


def run():
    n = int(input())
    a = [[int(i) for i in input().split()] for j in range(n)]
    k = int(input())
    res = abs(up(a) - down(a))
    if res <= k:
        print("YES")
    else:
        print("NO")
    print(res)
run()