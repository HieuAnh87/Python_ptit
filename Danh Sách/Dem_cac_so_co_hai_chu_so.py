n = input()
a = []
if len(n) % 2 != 0: m = len(n) - 1
else: m = len(n)
for i in range(0,m,2):
    a.append(n[i]+n[i+1])
# print(a)
dict = {}
for i in a:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
# print(dict)
for i in dict:
    print(i, dict[i])