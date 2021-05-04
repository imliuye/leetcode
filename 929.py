class Solution:
    def numUniqueEmails(self, emails) -> int:
        def parseEmail(email):
            local,domain = email.split('@')
            valid= local.split('+')[0]
            valid = valid.replace('.','')
            return valid+'@'+domain
        result=set()
        for e in emails:
            parse = parseEmail(e)
            result.add(parse)
        return len(result)

s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
