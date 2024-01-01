from collections import defaultdict
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.deleted = defaultdict(int)
        self.cuisines = defaultdict(list)
        self.f2c = {}
        self.ratings = {}
        for i in range(n):
            heapq.heappush(self.cuisines[cuisines[i]], (-ratings[i], foods[i]))
            self.f2c[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.f2c[food]
        old = self.ratings[food]
        self.deleted[(cuisine, -old, food)] += 1
        self.ratings[food] = newRating
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisines[cuisine][0]
        while (cuisine, rating, food) in self.deleted:
            heapq.heappop(self.cuisines[cuisine])
            self.deleted[(cuisine, rating, food)] -= 1
            if self.deleted[(cuisine, rating, food)] == 0:
                del self.deleted[(cuisine, rating, food)]
            rating, food = self.cuisines[cuisine][0]
        return food