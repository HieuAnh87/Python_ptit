def Check(n):
    s = str(n)
    if len(s) > 1 and s == s[::-1]:
        return "YES"
    else:
        return "NO"

def main():
    t = int(input())
    for i in range(t):
        s = input()
        num = 0
        for i in s:
            num += int(i)
        print(Check(num))
main()