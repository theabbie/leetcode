class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        ops = ((len(pizzas) // 4) + 1) // 2
        pizzas.sort()
        pizzas = deque(pizzas)
        res = 0
        odd = True
        for _ in range(ops):
            z = pizzas.pop()
            w = pizzas.popleft()
            x = pizzas.popleft()
            y = pizzas.popleft()
            res += z
        while pizzas:
            w = pizzas.popleft()
            x = pizzas.popleft()
            z = pizzas.pop()
            y = pizzas.pop()
            res += y
        return res