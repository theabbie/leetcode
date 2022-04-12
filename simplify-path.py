class Solution:
    def simplifyPath(self, path: str) -> str:
        path += "/"
        chunk = ""
        chunks = []
        for c in path:
            if c == "/":
                if len(chunk) > 0:
                    chunks.append(chunk)
                chunk = ""
            else:
                chunk += c
        curr = []
        for folder in chunks:
            if folder == "..":
                if len(curr) > 0:
                    curr.pop()
            elif folder != ".":
                curr.append(folder)
        return "/" + "/".join(curr)