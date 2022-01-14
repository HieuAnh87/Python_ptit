import math
def run():
    n = int(input())
    # a = [i for i in input().split()]
    a = []
    # nhập mảng
    for i in range(n):
            a.append(input())
    res = 0
    # tính hàng
    for i in range(n):
        count = 0
        for j in range(n):
            if a[i][j] == 'C':
                count += 1
        res += math.comb(count,2)
    # tính cột
    for i in range(n):
        count = 0
        for j in range(n):
            if a[j][i] == 'C':
                count += 1
        res += math.comb(count,2)
    print(res)
run()