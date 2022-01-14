def run():
    s = input()
    a = []
    res = []
    for i in range(len(s),0,-3):
        if i >= 3:
            a.append(s[i-3:i:])
        else:
            a.append(s[0:i])
    for i in a:
        res.append(int(i, 2))
    res.reverse()
    print(*res, sep='')
run()