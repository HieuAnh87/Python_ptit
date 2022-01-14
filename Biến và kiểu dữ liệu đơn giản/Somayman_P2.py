t = int(input())
while t:
    n = input()
    flag = 1
    for i in n:
        if i != '4' and i != '7':
            flag = 0
            break
    if flag == 1:
        print("YES")
    else:
        print("NO") #comment
    t -= 1