def run():
    n =int(input())
    # n = 7
    a = [int(i) for i in input().split()]
    # a = [100, 80, 60, 70, 60, 75, 85]
    # print(a)
    p = []
    res = []
    for i in range(0, n):
        if len(p)==0:
            p.append([a[i], 1])
            res.append(1)
        else:
            if a[i] < p[-1][0]: #top
                p.append([a[i], 1])
                res.append(1)
            else:
                tmp = 1
                while a[i] >= p[-1][0]:
                    tmp += p[-1][1]
                    p.pop()
                    if len(p)==0: break
                p.append([a[i], tmp])
                res.append(tmp)
    print(*res)

def main():
    t = int(input())
    # t= 1
    for i in range(0, t):
        run()
main()