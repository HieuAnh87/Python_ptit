def Mul(x):
    x = str(x)
    res = 1
    for i in x:
        res *= int(i)
    return res

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    dict = {}
    for i in a:
        dict[int(i)] = Mul(i)
    sorted_dict = sorted(dict.items(), key = lambda x: (x[1], x[0]))
    for i in sorted_dict:
        print(i[0], end= " ")
    print()
def main():
    t = int(input())
    for i in range(t):
        run()
main()