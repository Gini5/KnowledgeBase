class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        vowel = 'aeiouAEIOU'
        for i,w in enumerate(words):
            if w and w[0] not in vowel:
                new = w[1:]+w[0]
            new += 'ma'+'a'*(i+1)
            words[i] = new
        return ' '.join(words)