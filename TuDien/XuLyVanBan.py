def Xuly (s):
    res = []
    ktdb = ['.', '?', '!']
    s.lower()
    tmp = ""
    for i in range(0,len(s)):
        if s[i] in ktdb:
            res.append(tmp)
            tmp = ""
        else:
            tmp += s[i]
            
    for i in range(0, len(res)):
        res[i] = " ".join(res[i].split())
        res[i] = res[i].capitalize()
        print(res[i])
   
s = ""
while 1:
    try:
        s += input()
    except:
        break
Xuly(s)