class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist = [0] * num_people
        i = 0
        j = 0
        while candies > 0:
            curr = min(num_people * i + j + 1, candies)
            dist[j] += curr
            i, j = i + (j + 1) // num_people, (j + 1) % num_people
            candies -= curr
        return dist