def run():
    n = int(input())
    s = [int (i) for i in input().split()]
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    res = max(dict, key=dict.get)
    maxx = dict[res]
    if maxx > n//2:
        print(res)
    else:
        print("NO")


def main():
    t = int(input())
    for i in range(0, t):
        run()
main()