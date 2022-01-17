def run():    
    n = int(input())
    if(n > 10):
        print('INVALID INPUT')
    else:
        dict = {}
        for i in range(n):
            a = input().split()
            dict[a[0]] = a[1]
        tong = 0
        tich = 1
        for i in dict.keys():
            if dict[i].isdigit():
                tong += int(dict[i])
                tich *= int(dict[i])
        print(tong, tich)
run()

# 4
# a 9
# b 5
# c abc
# d 1
# 6371 ->