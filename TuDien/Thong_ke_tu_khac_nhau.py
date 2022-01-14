def run():
    n = int(input())
    a = []
    # nhap van ban
    for i in range(n):
        x = input().lower()
        x = x.replace(".","")
        x = x.replace(",","")
        x = x.replace("!","")
        x = x.replace(":","")
        x = x.replace(";","")
        x = x.replace("-"," ")
        x = x.replace("/"," ")
        x = x.split()
        a.append(x)
    # a.sort()
    dict = {}
    for i in a:
        # i = i.split()
        for j in i:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
    sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse=True)
    for i in sorted_dict:
        print(i[0],i[1])
run()