def run():   
    n, k = map(int,input().split())
    if n > 70 or k > 5:
        print('INVALID INPUT')
    else:
        res = {}
        for i in range(n):
            s = input().split()
            res[s[0]] = int(s[1])
        res = sorted(res.items(), key = lambda x:(-x[1], x[0]))
        for i in range(k):
            print(res[i][0], end = ' ')
run()


# 10 3
# Hung 6
# Long 7
# Giang 8
# Linh 5
# Tuan 8
# Hoa 9
# Mai 5
# Ngoc 4
# Khanh 9
# Ngan 10