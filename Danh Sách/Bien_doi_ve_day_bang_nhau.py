import math
def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    pos = a[0]
    minn = 1000000
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += abs(a[j] - a[i])
        print(tmp)
        if tmp < minn:
            minn = tmp
            pos = a[i]

    print(minn, pos)
run()