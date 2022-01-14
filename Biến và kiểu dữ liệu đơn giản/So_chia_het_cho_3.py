def run():
    s = str(input())
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
def main():
    t = int(input())
    for i in range(t):
        run()
main()