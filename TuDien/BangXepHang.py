def run():
    n =int(input())
    dssv = []
    for i in range(n):
        dict = {}
        dict['TenSv'] = input()
        temp = ''
        temp = input().split()
        dict['AC'] = int(temp[0])
        dict['Submit'] = int(temp[1])
        dssv.append(dict)
    res = sorted(dssv, key=lambda k: (
        -k['AC'],
        k['Submit'],
        k['TenSv'],
    ))
    for val in res:
        print(*val.values())
    # print(res)
run()
