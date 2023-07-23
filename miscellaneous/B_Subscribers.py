n = list(input())

for i in range(3, len(n)):
    n[i] = "0"

print("".join(n))