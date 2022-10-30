a, b = map(int, input().split())

def getstr(a, b):
    if b == 0:
        return "0.000"
    if b == a:
        return "1.000"
    k = str(round(1000 * b / a))
    return f"0.{k}" + "0" * max(3 - len(k), 0)

print(getstr(a, b))