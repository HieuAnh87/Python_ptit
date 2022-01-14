def run():
    n = input()
    a =[]
    for i in range(0, len(n)-1,2):
        a.append(n[i] * int(n[i+1]))
    print(''.join(a))


def main():
    t = int(input())
    for i in range(0, t):
        run()
main()