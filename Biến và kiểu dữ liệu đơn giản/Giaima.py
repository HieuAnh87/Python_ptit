t = int(input())
while t:
    s = input()
    for i in s:
        if(i.isnumeric()):
            for j in int(i):
                print(i-1, end='')
    print("")
    t -=1