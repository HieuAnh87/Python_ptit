def run():
    n = input()
    if n[0:2] == n[-2:]:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()
main()