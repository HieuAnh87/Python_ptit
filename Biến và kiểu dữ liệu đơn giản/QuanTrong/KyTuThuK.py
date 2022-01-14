bang = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def run():
    n,m = map(int, input().split())
    s = 'A'
    for i in range(n):
        s = s + bang[i+1] + s
    print(s[m-1])
    
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()