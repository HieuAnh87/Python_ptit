import math

def run():
    n = int(input())
    res = "1"
    for i in range(2, int(math.sqrt(n))+1):
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        if count > 0:
            res = res + " * " + str(i) + "^" + str(count)
    if n > 1:
        res = res + " * " + str(int(n)) + "^1"
    print(res)

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()