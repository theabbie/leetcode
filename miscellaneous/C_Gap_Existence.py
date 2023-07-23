n, x = map(int, input().split())

arr = list(map(int, input().split()))

def check(arr, x):
    seen = set()
    for el in arr:
        seen.add(el)
        if el - x in seen or el + x in seen:
            return "Yes"
    return "No"

print(check(arr, x))