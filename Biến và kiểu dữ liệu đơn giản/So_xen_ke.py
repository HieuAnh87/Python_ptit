def check(s):
    if len(s) % 2 == 0 or s[0] == s[1]: return "NO"
    for i in range(0, len(s), 2):
        if s[i] != s[0]: return "NO"
        return "YES"
def main():
    t = int(input())
    for i in range(t):
        s = input()
        print(check(s))
main()
