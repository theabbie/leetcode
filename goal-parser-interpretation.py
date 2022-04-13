class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        op = ""
        while i < n:
            if command[i] == "G":
                op += "G"
                i += 1
            elif i < n - 1 and command[i:i+2] == "()":
                op += "o"
                i += 2
            elif i < n - 3 and command[i:i+4] == "(al)":
                op += "al"
                i += 4
        return op