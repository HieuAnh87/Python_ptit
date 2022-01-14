def run():
    n = int(input())
    s = input().split()
    # s = [int (i) for i in input().split()]
    for i in range(0, n): s[i] = int(s[i])
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    maxx = 0
    res = 0
    for i in dict:
        if dict[i] > maxx:
            maxx = dict[i]
            res = i
    if maxx > int(n/2):
        print(res)
    else:
        print("NO")


def main():
    t = int(input())
    for i in range(0, t):
        run()
main()