def run():
    s = input()
    for i in s:
        if i != '4' and i != '7':
            print("NO")
            return
    print("YES")

def main():
    t = int(input())
    for i in range(t):
        run()
main()