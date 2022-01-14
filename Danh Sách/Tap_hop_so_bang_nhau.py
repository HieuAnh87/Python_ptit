n, m = map(int, input().split())
# a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
a = set(input().split())
b = set(input().split())
if a == b:
    print("YES")
else:
    print("NO")
