def num(n):
    if n >= '0' and n <= '9':
        return True
    return False

def run():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        temp = ""
        for i in s:
            if num(i):
                temp += i
            else:
                if temp != "":
                    a.append(int(temp))
                temp = ""
        if temp != "":
            a.append(int(temp))
    a.sort()
    for i in a:
        print(i)
run()