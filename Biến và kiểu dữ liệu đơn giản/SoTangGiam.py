def Tangdan(s):
    for i in range(0, len(s)-1):
        if s[0] > s[1]:
            return False
        else:
            if s[i] >= s[i+1]:
                return i

def Giamdan(s):
    if Tangdan(s)==False or len(s) < 3:
        print("NO")
        return
    for i in range(Tangdan(s), len(s)-1):
        if s[i] < s[i+1]:
            print("NO")
            return
    print("YES")

def run():
    s = input()
    Giamdan(s)
    
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()