t = int(input())
for i in range(t):
    a = sorted(input())
    b = sorted(input())
    if a == b:
        print(f"Test {i+1}: YES")
    else:
        print(f"Test {i+1}: NO")
