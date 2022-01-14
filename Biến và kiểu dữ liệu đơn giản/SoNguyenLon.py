def gcd(a,b):
    if b==0: return a
    return gcd(b, a%b)

def run():
    a = int(input())
    b = int(input())
    print(int(gcd(b, a%b)))
    
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()