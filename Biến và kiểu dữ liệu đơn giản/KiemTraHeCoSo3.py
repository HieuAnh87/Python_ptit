P = '012'
def run():
    n = input()
    for i in n:
        if i != P[P.find(i)]:
            print("NO")
            return
    print("YES")

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()