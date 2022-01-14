def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def run():
    n = input()
    m = n[::-1]
    if gcd(int(n), int(m)) == 1:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()
main()