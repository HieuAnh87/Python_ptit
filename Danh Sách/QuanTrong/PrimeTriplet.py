import math
def sieve(n, prime) :
    p = 2
    while (p * p <= n ) :
        # If prime[p] is not changed
        # , then it is a prime
        if (prime[p] == True) :
            # Update all multiples of p
            i = p * 2
            while ( i <= n ) :
                prime[i] = False
                i = i + p
        p = p + 1

def run():
    n = int(input())
    # n = 25
    count = 0
    prime = [True] * (n + 1)
    sieve(n, prime)
    for i in range(2, n - 6 + 1) :
        # triplets of form (p, p+2, p+6)
        if (prime[i] and prime[i + 2] and prime[i + 6]):
            count += 1
        # triplets of form (p, p+4, p+6)
        elif (prime[i] and prime[i + 4] and prime[i + 6]) :
            count += 1
    print(count)

def main():
    t = int(input())
    for i in range(0, t):
        run()
main()