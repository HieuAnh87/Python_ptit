def run():
    s = input()
    mul = 1
    for i in s:
        if int(i) != 0:
            mul *= int(i)
    print(mul)
def main():
    t = int(input())
    for i in range(t):
        run()
main()
