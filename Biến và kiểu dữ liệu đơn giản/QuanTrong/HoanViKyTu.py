import itertools
s = input().upper()
# s ="XYZ"
a = []
for i in range(len(s)):
    a.append(s[i])
a.sort()
res = list(itertools.permutations(a))
for i in range(len(res)):
    print(''.join(res[i]))
