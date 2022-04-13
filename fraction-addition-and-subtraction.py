class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, arr):
        n = len(arr)
        curr = arr[0]
        for i in range(1, n):
            l = arr[i]
            curr = (curr * l) // self.gcd(curr, l)
        return curr
    
    def fractionAddition(self, expression: str) -> str:
        expression += "x"
        sign = 1
        chunk = ""
        nums = []
        for c in expression:
            if c == "+" or c == "-" or c == "x":
                if len(chunk) > 0:
                    a, b = chunk.split("/")
                    a, b = int(a), int(b)
                    nums.append([sign * a, b])
                chunk = ""
                if c == "+":
                    sign = 1
                elif c == "-":
                    sign = -1
            else:
                chunk += c
        mul = self.lcm([num[1] for num in nums])
        ans = sum([num[0] * mul // num[1] for num in nums])
        hcf = self.gcd(ans, mul)
        return "{}/{}".format(ans // hcf, mul // hcf)