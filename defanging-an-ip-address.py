class Solution:
    def defangIPaddr(self, address: str) -> str:
        n = len(address)
        op = ""
        for i in range(n):
            if address[i] == ".":
                op += "[.]"
            else:
                op += address[i]
        return op