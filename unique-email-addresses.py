class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        diff = set()
        for email in emails:
            host, domain = email.split('@')
            host = host.split('+')[0]
            host = "".join(host.split('.'))
            diff.add("{}@{}".format(host, domain))
        return len(diff)