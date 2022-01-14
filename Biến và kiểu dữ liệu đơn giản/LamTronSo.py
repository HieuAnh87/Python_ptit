def run():
    s = list(input())
    s.reverse()
    for i in range(0, len(s)-1):
        if int(s[i]) >= 5:
            s[i+1] = int(s[i+1]) +  1
    print(s[-1], end="")
    print('0'*(len(s)-1))

def main():
    t = int(input())
    for i in range(t):
        run()
main()
