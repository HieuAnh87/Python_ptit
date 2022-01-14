def run():
    s = input()
    n = input()
    count = 0
    while True:
        if n == s[s.find(n):s.find(n)+len(n)]:
            count += 1
            s = s[s.find(n)+len(n):]
        else:
            if count > 0:
                print(count)
            return

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()