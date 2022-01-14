# https://www.geeksforgeeks.org/count-ways-express-number-sum-consecutive-numbers/
def run():
    n = int(input())
    res = 0
    L = 1
    while (L * (L + 1) < 2 * n):
        a = (1.0 * n - (L * (L + 1)) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            res += 1
        L += 1
    print(res)   

def main():
    t = int(input())
    for i in range(t):
        run()
main()
 

# Approach: The idea is to represent N as a sequence of length L+1 as: 
# N = a + (a+1) + (a+2) + .. + (a+L) 
# => N = (L+1)*a + (L*(L+1))/2 
# => a = (N- L*(L+1)/2)/(L+1) 
# We substitute the values of L starting from 1 till L*(L+1)/2 < N 
# If we get ‘a’ as a natural number then the solution should be counted.