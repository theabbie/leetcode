import re
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        for file in paths:
            val = file.split()
            n = len(val)
            for i in range(1, n):
                file, content = re.search("(\S+)\((\S+)\)", val[i]).groups()
                files[content].append(f"{val[0]}/{file}")
        return [v for v in files.values() if len(v) > 1]