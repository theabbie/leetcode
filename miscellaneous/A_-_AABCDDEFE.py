n = int(input())

vals = []

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        curr = int(f"{i}{i}{a}{b}{j}{j}{k}{c}{k}")
                        vals.append(curr)

vals.sort()

print(vals[n - 1])