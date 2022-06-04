class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        isv4 = True
        isv6 = True
        if "." in queryIP:
            isv6 = False
            queryIP = queryIP.split(".")
            if len(queryIP) != 4:
                isv4 = False
        else:
            isv4 = False
        if ":" in queryIP:
            isv4 = False
            queryIP = queryIP.split(":")
            if len(queryIP) != 8:
                isv6 = False
        else:
            isv6 = False
        if isv4:
            for x in queryIP:
                if not x.isnumeric() or (len(x) > 1 and x[0] == "0") or not 0 <= int(x) < 256:
                    isv4 = False
                    break
        if isv6:
            for x in queryIP:
                try:
                    int(x, 16)
                    if len(x) > 4:
                        raise
                except:
                    isv6 = False
                    break
        if isv4:
            return "IPv4"
        if isv6:
            return "IPv6"
        return "Neither"