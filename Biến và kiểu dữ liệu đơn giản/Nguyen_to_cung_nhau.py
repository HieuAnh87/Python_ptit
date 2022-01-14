import math
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

def main():
    n, num = input().split()
    num = int(num)
    count = 0
    for i in range(10**(num-1), 10**num):
        if math.gcd(int(n), int(i)) == 1:
            count += 1
            print(i, end=" ")
        if count == 10:
            print("")
            count = 0
main()
# dung ham math.gcd(x, y) co san