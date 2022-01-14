def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    a.append(-1)
    for i in range(n):
        if a[i] != a[i+1]:
            count += 1
    print(count - 1)
run()    
