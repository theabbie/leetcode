import scipy.optimize as opt

class Solution:
    def getMinDistSum(self, positions):
        def f(x, y):
            return sum(math.sqrt((x - px) ** 2 + (y - py) ** 2) for px, py in positions)
        def blackbox_function(xy):
            x, y = xy
            return f(x, y)
        result = opt.minimize(blackbox_function, [50, 50], bounds=[(0, 100), (0, 100)], tol=1e-9)
        return result.fun