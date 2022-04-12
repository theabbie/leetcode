w = "aabb"
n = len(w)

for d in range(n-2, -1, -1):
    words = [w[:d]]
    print(words)
    while len(words) > 0:
        word = words.pop(0)
        if len(word) == n:
            print(word)
        for c in w:
            if c not in word:
                words.append(word + c)