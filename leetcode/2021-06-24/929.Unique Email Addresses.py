class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            name, domain = email.split('@')
            if '+' in name:
                name = name.split('+')[0]
            name = name.replace('.','')
            email_set.add(name + '@' + domain)

        return len(email_set)


print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
