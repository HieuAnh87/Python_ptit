f = {}
def fibo():
    f[1],f[2] = 1,1
    for i in range(3, 95):
        f[i] = f[i-1] + f[i-2]
fibo()

t = int(input())
while t:
    t -= 1
    a,b = map(int, input().split())
    res = ""
    for i in range(a, b+1):
        res += str(f[i]) + " "
    print(res)