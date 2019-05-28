class Solution(object):
    def numUniqueEmails(self, emails):
        if len(emails) == 0:
            return 0
        res = set()
        for email in emails:
            local = email.split("@")[0]
            domain = email.split("@")[1]
            ignored = local.split("+")[0]
            dots = ignored.replace(".", "")
            res.add(dots + "@" + domain)

        return len(res)

test = Solution()
print test.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com", "testemail@lee.tcode.com"])