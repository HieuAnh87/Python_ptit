def run():
    n,m = [int(i) for i in input().split()]
    # n = 6
    # m = 4
    maxx = -1
    minn = 10001
    a = [[int(i) for i in input().split()] for j in range(n)]
    # a = [[23, 21, 77, 10], [13, 13, 22, 14], [28, 67, 28, 23], [29, 77, 11, 67], [16, 51, 24, 21], [13, 25, 77, 77]]
    for i in range(n):
        for j in range(m):
            maxx = max(maxx,a[i][j])
            minn = min(minn,a[i][j])
    space = maxx - minn
    flag = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == space:
                flag = 1
                break
    if flag == 0:
        print("NOT FOUND")
        return

    print(space)
    for i in range(n):
        for j in range(m):
            if a[i][j] == space:
                print(f"Vi tri [{i}][{j}]")
run()

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77