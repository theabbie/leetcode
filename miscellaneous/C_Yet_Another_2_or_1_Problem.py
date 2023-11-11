import sys

input = sys.stdin.readline

t = int(input())

cres = []

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

print("\n".join(cres))