def run():
    n = input()   
    if n[0] == n[len(n)-1]:
        print("YES")
        return
    print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()