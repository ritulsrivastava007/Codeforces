import sys
mod = 998244353

def solve(n):
    added = 0
    best = floar('inf')
    while n>= 4:
        k = n.bit_length()-1
        power = 1<< k
        op2 = (power << 1)- n + k

        best = min(best, op2 +added)

        added += k+1
        n = n -power +2
    if n== 0:
        base = 0
    elif n== 1:
        base = 1
    elif n== 2:
        base = 3
    else:
        base = 2
        
    return min(base +added, best)

def main():
    input = sys.stdin.readline
    t = int(input())
    results = []

    for _ in range(t):
        l, r = map(int,input().split())
        ans = 0
        for n in range(l, r+1):
            ans = (ans+solve(n)) % mod
        results.append(str(ans))
        print('\n'.join(results))

if __name__ == "__main__":
    main()