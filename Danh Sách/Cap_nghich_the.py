def main():
    n = int(input())
    s = input().split()
    count = 0
    for i in range(0,n):
        s[i] = int(s[i])
    for i in range(0, n-1):
        j = i+1
        for j in range(i+1, n):
            if(s[i] > s[j]):
                count += 1
    print(count)
main()