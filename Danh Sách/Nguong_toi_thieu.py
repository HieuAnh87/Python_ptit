n = input()
k = int(input())
a = []
if len(n) % 2 != 0: m = len(n) - 1
else: m = len(n)
for i in range(0,m,2):
    a.append(n[i]+n[i+1])
# print(a)
a.sort()
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
# print(dict)
flag = True
for i in dict:
    if dict[i] >= k:
        print(i, dict[i])
        flag = False
if flag: print("NOT FOUND")