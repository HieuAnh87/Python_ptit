n, m = map(int, input().split())
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
a = set(input().split())
b = set(input().split())
print(*sorted(a & b))
print(*sorted(a - b))
print(*sorted(b - a))