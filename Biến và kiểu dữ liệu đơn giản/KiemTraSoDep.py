def run():
    s = input()
    a = s[0] + s[1]
    for i in range(0, len(s)-1, 2):
        if s[i] + s[i+1] != a:
            print("NO")
            return
    print("YES")

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()