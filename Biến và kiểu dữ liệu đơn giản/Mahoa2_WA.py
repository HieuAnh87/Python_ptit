P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.' # Dãy P

while True:
    s = input().split() #input multiple trong 1 string 
    k = int(s[0])
    if k == 0: # Nếu số = 0 break
        break
    s = s[1]
    print(s)
    res = ''
    for i in s:
        pos = P.find(i)
        res = P[(pos + k) % 28] + res
    print(res)