def Sum(n):
    sum = 0
    n = str(n)
    for i in n:
        sum = sum + int(i)
    return sum

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    dict = {}
    for i in a:
        dict[i] = Sum(i)
    sorted_dict = sorted(dict.items(), key = lambda x: (x[1], x[0])) # #x : x[1] theo value, x : x[0] theo key 
    for i in sorted_dict:
        print(i[0], end = ' ')
    print()

def main():
    t = int(input())
    for i in range(t):
        run()
main()