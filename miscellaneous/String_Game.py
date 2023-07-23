t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    k = min(s.count("0"), s.count("1"))
    if k % 2 == 0:
        print("Ramos")
    else:
        print("Zlatan")