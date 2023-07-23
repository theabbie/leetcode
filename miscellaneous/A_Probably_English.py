n = int(input())

words = set(input().split())

print("Yes" if len(set.intersection(words, {"and", "not", "that", "the", "you"})) > 0 else "No")