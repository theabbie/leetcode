class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        for a, b in paths:
            cities.add(a)
            cities.add(b)
        for a, b in paths:
            if a in cities:
                cities.remove(a)
        return list(cities)[0]