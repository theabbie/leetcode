class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ctr = {}
        for val in cpdomains:
            rep, domain = val.split(" ")
            rep = int(rep)
            doms = domain.split(".")
            n = len(doms)
            for i in range(n):
                curr = ".".join(doms[i:])
                ctr[curr] = ctr.get(curr, 0) + rep
        return ["{} {}".format(v, k) for k, v in ctr.items()]