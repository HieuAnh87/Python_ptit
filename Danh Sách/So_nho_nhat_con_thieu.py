def run():  
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(1,a[n-1]):
        if i not in a:
            print(i)
            return
    print(a[n-1] + 1)
run()