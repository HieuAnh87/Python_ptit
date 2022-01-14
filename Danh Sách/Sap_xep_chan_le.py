def run():
    n = int(input())
    chan = []
    le = []
    res = []
    sl = 0
    while sl < n:
        temp = [int(i) for i in input().split()]
        for so in temp:
            sl += 1
            if so % 2 == 0:
                chan.append(so)
            else:
                le.append(so)
        res.extend(temp)
    le.sort(reverse=True)
    chan.sort()
    i = 0
    j = 0
    for x in res:
        if x % 2 == 0:
            print(chan[i], end = " ")
            i += 1
        else:
            print(le[j], end = " ")
            j += 1
run()