def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    count = {}
    for i in range(n):
        if a[i] not in count:
            count[a[i]] = 1
        else:
            count[a[i]] += 1
    for i in range(n):
        if count[a[i]] % 2 != 0:
            print(a[i])
            return

def main():
    t = int(input())
    for i in range(t):
        run()
main()