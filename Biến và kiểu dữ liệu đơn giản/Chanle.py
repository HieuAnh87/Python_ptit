t = int(input())
while t:
    line = input()
    sum = 0
    for i in line:
        sum += int(i)
    # Neu tong chu so % 10 == 0 thi moi xet tiep
    if(sum % 10 == 0):
        flag = 1
        for i in range( 0, len(line) - 1):
            if( abs(int( line[i+1]) - int( line[i] )) != 2):
                print("NO")
                flag = 0
                break

        if flag :
            print("YES")
    else:
        print("NO")
    t -= 1
