def run():
    n = int(input())
    t = 0
    while t <= 1000:
        if n%7==0:
            print(n)
            return
        n = n + int(str(n)[::-1])
        t+=1
    print(-1)
    return

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()