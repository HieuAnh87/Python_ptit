def Nhiphan_Doicoso (s,k):    
    if k == 2: return s    
    x = 2    
    while 1:        
        if pow(2, x) == k:            
            break        
        x+=1
    if len(s)%x!=0:        
        s = (x-len(s)%x)*'0' + s   
    a = [int(i) for i in list(s)]    
    res = ""    
    for i in range(0, len(a)+1-x,x):        
        tmp = 0        
        for j in range(0, x):            
            tmp += a[i+j]*pow(2, x-1-j)        
        if tmp<10: res += str(tmp)        
        else: 
            res+= chr(ord('A') + tmp-10)    
    return res


def run():
    n = int(input())
    s = input()
    # res = int(s,2)
    print(Nhiphan_Doicoso(s,n))

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()