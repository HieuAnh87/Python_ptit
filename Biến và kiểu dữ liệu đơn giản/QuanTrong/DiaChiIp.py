def run():
    n = input().split('.')
    # print(len(n))
    if len(n) != 4:
        print("NO")
        return
    for i in range(len(n)):
        if n[i].isdigit()==False:
            print("NO")
            return
        if int(n[i])>255 or int(n[i]) <0:
            print("NO")
            return
    print("YES")
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()