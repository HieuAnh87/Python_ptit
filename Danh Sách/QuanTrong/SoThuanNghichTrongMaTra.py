def isReverse(s):
    if s == s[::-1]:
        return True
    return False
def run():
    n,m = [int(i) for i in input().split()]
    # n = 6
    # m = 4
    maxx = -1
    a = [[int(i) for i in input().split()] for j in range(n)]
    # a = [[23, 21, 77, 10], [13, 13, 22, 14], [28, 67, 28, 23], [29, 77, 11, 67], [16, 51, 24, 21], [13, 25, 77, 77]]
    for i in range(len(a)):
        for j in range(m):
            n = a[i][j]
            if isReverse(str(n)) and len(str(n))>1:
                maxx = max(maxx, a[i][j])
    if maxx == -1:
        print("NOT FOUND")
        return
    print(maxx)
    for i in range(len(a)):
        for j in range(m):
            if a[i][j] == maxx:
                print(f"Vi tri [{i}][{j}]")
run()
