def run():
    s = input()
    sum, mul = 0, 1
    flag = 1
    for i in range(0, len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if s[i] != '0':
                mul *= int(s[i])
                flag = 0
    print(sum, end=" ")
    if flag == 1: print("0")
    else: print(mul)

def main():
    t = int(input())
    for i in range(t):
        run()
main()