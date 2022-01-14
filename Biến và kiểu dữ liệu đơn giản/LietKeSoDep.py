def isReverse(s):
    s = str(s)
    if s == s[::-1]:
        return True
    return False

def isEven(s):
    s = str(s)
    for i in range(0, len(s)):
        if int(s[i]) % 2 != 0:
            return False
    return True

def N(s):
    s = int(len(str(s)))
    if s % 2 == 0:
        return True
    return False

def run():
    s = int(input())
    a = []
    for i in range(0, s):
        if isReverse(i) and isEven(i) and N(i):
            a.append(i)
    print(*a)
def main():
    t = int(input())
    for i in range(t):
        run()
main()
