a, b, c = map(int, input().split())

m = int(input())

usb = []
ps2 = []

for _ in range(m):
    x, y = input().split()
    if y == "USB":
        usb.append(int(x))
    else:
        ps2.append(int(x))

usb.sort(reverse = True)
ps2.sort(reverse = True)

a = min(a, len(usb))
b = min(b, len(ps2))
c = min(c, len(usb) + len(ps2) - a - b)

res = 0

for i in range(a):
    res += usb.pop()

for i in range(b):
    res += ps2.pop()

for i in range(c):
    if len(ps2) == 0 or (len(usb) > 0 and usb[-1] < ps2[-1]):
        res += usb.pop()
    elif len(ps2) > 0:
        res += ps2.pop()

print(a + b + c, res)