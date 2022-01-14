n = int(input())
dict = {}
for i in range(n):
    x = input().upper()
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1

print(len(dict))