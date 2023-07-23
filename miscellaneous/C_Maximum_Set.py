M = 998244353

t = int(input())

facts = [1] * 21

for i in range(1, 21):
    facts[i] = i * facts[i - 1]
    facts[i] %= M

def solve(l, r):
    size = 1
    ll = l
    while ll * 2 <= r:
        ll *= 2
        size += 1
    k = size - 1
    ctr = 0
    for i in range(k + 1):
        curr = pow(2, i) * pow(3, k - i)
        if l * curr <= r:
            mul = r // curr - l + 1
            ctr += mul * facts[k] * pow(facts[i], M - 2, M) * pow(facts[k - i], M - 2, M)
            ctr %= M
    print(size, ctr)

for _ in range(t):
    l, r = map(int, input().split())
    solve(l, r)