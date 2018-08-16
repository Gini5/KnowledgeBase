class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        vowel = 'aeiouAEIOU'
        for i,w in enumerate(words):
            if w and w[0] in vowel:
                new = w+'ma'
            elif w and w[0] not in vowel:
                new = w[1:]+w[0]+'ma'
            new += 'a'*(i+1)
            words[i] = new
        return ' '.join(words)