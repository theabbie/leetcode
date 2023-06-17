M = 10 ** 9 + 7

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * (n + 1)
        fi = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = i * f[i - 1]
            fi[i] = pow(i, M - 2, M) * fi[i - 1]
            f[i] %= M
            fi[i] %= M
        tree = {}
        for el in nums:
            curr = 1
            while curr in tree:
                if el < tree[curr]:
                    curr *= 2
                else:
                    curr *= 2
                    curr += 1
            tree[curr] = el
        ctr = {}
        size = {}
        for root in sorted(tree, reverse = True):
            l = ctr.get(2 * root, 1)
            r = ctr.get(2 * root + 1, 1)
            lsize = size.get(2 * root, 0)
            rsize = size.get(2 * root + 1, 0)
            size[root] = 1 + lsize + rsize
            ctr[root] = f[lsize + rsize] * fi[lsize] * fi[rsize] * l * r
            ctr[root] %= M
        return (M + ctr[1] - 1) % M