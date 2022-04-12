while True:
    denom = [3, 4]
    print("Enter value: ")
    n = int(input())
    while len(denom) > 0 and n > 0:
        curr = denom.pop()
        if n >= curr:
            n = n % curr
    if n == 0:
        print("YES")
    else:
        print("NO")

