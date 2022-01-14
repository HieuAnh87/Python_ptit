def run():
    s = list(input())
    s.reverse()
    for i in range(0, len(s)-1):
        if int(s[i]) >= 5:
            s[i+1] = int(s[i+1]) + 1
    print(s[-1],end="")
    for i in range(0, len(s)-1):
        print("0",sep="",end="")
    print("")
        
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()