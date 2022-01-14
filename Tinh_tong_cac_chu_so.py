T = int(input())
for t in range(T):
    s = input()
    res = ''
    count = 0
    for i in s:
        if i.isnumeric():
            count = count + int(i)
        else:
            res = res + i
    res = ''.join(sorted(res))
    print(res+str(count))