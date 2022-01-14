def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    # res = (max(a) - min(a) + 1) - n
    count = 0
    # s = list(range(min(a),max(a)+1))
    # res = len(s) - len(a)
    for i in range(min(a),max(a)+1):
        if i not in a:
            count += 1
    print(count)

def main():
    t = int(input())
    for i in range(t):
        run()
main()