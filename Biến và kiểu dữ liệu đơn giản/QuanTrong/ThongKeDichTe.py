def isFound(a,n,m):
    s = ""
    count = 0
    for i in range(n):
        for j in range(m):
            if int(a[i][j]) == -1:
                s = s + str(i) +" "+ str(j)+" "
                count += 1
    s = s + str(count)
    return s.split()

def run():
    # m,n = map(int, input().split())
    # a = [[int(i) for i in input().split()] for j in range(n)]
    n = 4
    m = 4
    a = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, -1], [0, 1, 1, 1]]
    f0 = isFound(a,n,m)
    test = int(f0[-1])
    res = 1
    for case in range(test):
        row = int(f0[case*2])
        col = int(f0[row+1])
        for i in range(0, 3):
            for j in range(0, 3):
                if 0<=row+j-1<m-1 and 0<=col+i-1<n-1 and 0<=row+j-1<m-1 and 0<=col+i<n-1 and 0<=row+j-1<m-1 and 0<=col+i+1<n-1:
                    res = res + a[col+i-1][row+j-1] + a[col+i][row+j-1] + a[col+i+1][row+j-1]
    # print(res)

run()
