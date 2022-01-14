def convert(num,b):
    m = 0
    res = ""
    a = num
    while(a>0):
        if(b>10):
            m = a % b
            if(m>=10):
                res = res + str(chr(55+m))
            else:
                res = res + str(m)
        else:
            res = res + str(a%b)
        a = int(a/b)
    return ''.join(reversed(res))

def run():
    num,b=map(int, input().split())
    print(convert(num,b))

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()