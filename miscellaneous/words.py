s = "the sun rises in the east"
words = s.split()

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
output = []

for i, word in enumerate(words):
    if i % 2 == 0:
        output.append(word[::-1])
    else:
        curr = sorted(word, key = lambda l: 1 if l in vowels else 0)
        output.append("".join(curr))

print(" ".join(output))
