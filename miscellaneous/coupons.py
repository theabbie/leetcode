n = int(input())

prices = list(map(int, input().split()))

q = int(input())

coupons = list(map(int, input().split()))

prices.sort()

total = sum(prices)

for c in coupons:
    print(total - prices[-c])