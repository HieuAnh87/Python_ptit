def run():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().lower())
    dict = {}
    for i in a:
        if i not in dict:
            dict[i] = 1
    for i in dict.keys():
        print(i)
run()