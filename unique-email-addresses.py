class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        diff = set()
        for email in emails:
            host = email.split('@')[0]
            domain = email.split('@')[1]
            host = host.split('+')[0]
            host = "".join(host.split('.'))
            diff.add("{}@{}".format(host, domain))
        return len(diff)