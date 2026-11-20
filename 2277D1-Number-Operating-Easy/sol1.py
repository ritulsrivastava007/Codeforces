import sys
from functools import lru_cache
mod = 998244353

@lru_cache(maxsize=None)
def solve(n):
    if n== 0:
        return 0
    if n== 1:
        return 1
    if n== 2:
        return 3
    if n== 3:
        return 2

    k = n.bit_length()-1
    power = 1<< k
    np = power<<1

    op1 = solve(n-power + 2) + k +1
    op2 = np -n +k

    return min(op1,op2)

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        l, r = map(int,input().split())
        ans = 0
        for n in range(l, r+1):
            ans = (ans+solve(n)) % mod

        print(ans)

if __name__ == "__main__":
    main()