n = 5

curr = [1]

for i in range(n):
    print(" " * (n - i - 1), end="")
    print(" ".join("{}".format(x) for x in curr))
    curr = [0] + curr + [0]
    curr = [curr[j] + curr[j + 1] for j in range(i + 2)]