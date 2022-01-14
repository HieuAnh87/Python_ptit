import re
def run():
    s = input()
    res = re.split('(\d+)', s)
    # res = str(tmp.match(s).groups())
    a = []
    for i in res:
        if i.isnumeric():
            a.append(int(i))
    print(min(a))
    
def main():
    t = int(input())
    for i in range(0, t):
        run()
main()