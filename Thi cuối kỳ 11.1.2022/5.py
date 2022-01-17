from itertools import accumulate
import math
n = int(input())
a = [int(i) for i in input().split()]
res = list(accumulate(a))
tong = sum(res)
tich = math.prod(res)
print(tong,tich)
