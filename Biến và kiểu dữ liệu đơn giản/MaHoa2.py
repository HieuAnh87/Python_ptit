P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    s = input().split()
    k = int(s[0])
    if k == 0:
        break
    s = s[1]
    res = ''
    for i in s:
        pos = P.find(i)
        res = P[(pos + k) % 28] + res
    print(res)