t = int(input())
while t:
    flag = 1
    s = input()
    for i in range(0,len(s)-1):
        if int(s[i]) > int(s[i+1]):
            print("NO")
            flag = 0
            break
    if flag:
        print("YES")
    t -= 1