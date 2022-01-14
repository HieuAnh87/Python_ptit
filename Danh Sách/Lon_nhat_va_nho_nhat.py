def run():
    while 1:    
        t = int(input())
        if t == 0: return
        a = []
        for i in range(t):
            a.append(int(input()))
        dict = {}
        check = True
        for i in range(t):
            if a[i] not in dict:
                dict[a[i]] = 1
            else:
                dict[a[i]] += 1
            # print(dict[a[i]])
            if dict[a[i]] == t:
                print("BANG NHAU")
                check = False
        if check: print(min(a), max(a))
    
run()