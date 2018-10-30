class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        sent = set()
        for e in emails:
            name, domain = e.split('@')
            parsed = name.split('+')[0].replace('.','')
            sent.add(parsed+'@'+domain)
        return len(sent)