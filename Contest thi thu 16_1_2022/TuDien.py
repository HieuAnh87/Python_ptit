def Xuly(s):
    a = s.split()
    n = len(a)

    ds = []
    for i in set(a):
        TF = a.count(i)/n
        dic = {'word':i, 'TF':TF}
        ds.append(dic)
    
    for i in sorted(ds, key= lambda k: (-k['TF'], k['word'])):
        print(i.get('word'), '%.2f'%i.get('TF'))


t = int(input())
s = ""
while t>0:
    s+= input() + " "
    t-=1
Xuly(s)

# 9
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme