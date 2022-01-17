import math
def tinhtong(n):
    tong = 0
    while n % 2 == 0:
        tong += 2
        n /= 2
    for i in range(3, math.sqrt(n) + 1, 2):
        while n % i == 0:
            tong += i
            n /= i
        if n > 2:
            tong += n
    return int(tong)
def main():
    kq = 1
    t = int(input())
    ds1, ds2 = [], []
    ds1 = [int(x) for x in input().split()]
    for x in ds1:
        ds2.append(tinhtong(x))
    for x in ds2:
        kq *= x
    print(kq)
main()

# 5
# 7
# 9
# 10
# 13
# 100


# 5
# 7
# 10
# 13
# 100
# [7, 6, 7, 13, 14]
# 53508