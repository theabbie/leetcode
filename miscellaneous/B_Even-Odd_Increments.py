t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    even = 0
    evenctr = 0
    odd = 0
    oddctr = 0
    for el in arr:
        if el & 1:
            odd += el
            oddctr += 1
        else:
            even += el
            evenctr += 1
    for _ in range(q):
        qt, x = map(int, input().split())
        if qt == 0:
            if (x + 2) % 2 == 0:
                even += x * evenctr
            else:
                odd += even + x * evenctr
                oddctr += evenctr
                even = 0
                evenctr = 0
        if qt == 1:
            if (x + 1) % 2 == 1:
                odd += x * oddctr
            else:
                even += odd + x * oddctr
                evenctr += oddctr
                odd = 0
                oddctr = 0
        print(odd + even)