sample ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rotate(s):
    k = 0
    res = ""
    for i in s:
        k += sample.find(i)
    for i in s:
        res += sample[(sample.find(i)+k) % 26]
    return res

def run():
    n = input()
    a = ""
    # Devine:
    for i in range(0, int(len(n)/2)):
        a += n[i]
    b = ""
    for i in range(int(len(n)/2), len(n)):
        b += n[i]
    # Rotate:
    a = rotate(a)
    b = rotate(b)
    res = ""
    # DMR:
    for i in range(len(a)):
        res += sample[(sample.find(a[i]) + sample.find(b[i])) % 26]
    print(res)
    
def main():
    t = int(input())
    for i in range(t):
        run()
main()