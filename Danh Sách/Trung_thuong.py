def run():
    n = int(input())
    list = []
    for i in range(n):
        list.append(int(input()))
    list.sort()
    list.append(-1)
    print(list)
    max = 0
    res = 0
    temp = 1
    for i in range(n):
        if list[i] == list[i+1]:
            temp += 1
        else:
            if max < temp:
                max = temp
                res = list[i]
            temp = 1
    print(res)

def main():
    t = int(input())
    for i in range(t):
        run()
main()