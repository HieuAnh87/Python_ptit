n = int(input())
dict = {}
for i in range(n):
    s = input().split()
    for j in s:
        if j not in dict:
            dict[j] = 1
        else:
            dict[j] += 1

sorted_dict = sorted(dict.items(), key=lambda x: -x[1])
# print(sorted_dict)
res = sorted_dict[1][1]
for i in dict.keys():
    if dict[i] == res:
        print(i,end=" ")
# print(res)