class Solution:
    def spellchecker(self, wordlist, queries):
        answer = ["" for _ in range(len(queries))]
        original = {w:w for w in wordlist}
        capital = {w.lower():w for w in wordlist[::-1]}
        vowel = {}
        vocabs = {'a', 'e', 'i', 'o', 'u'}

        for i, q in enumerate(queries):
            res = -1
            if q in original:
                res = original[q]
            elif q.lower() in capital:
                res = capital[q.lower()]
            elif q.lower() in vowel:
                res = vowel[q.lower()]
            if res != -1: answer[i] = wordlist[res]

        return answer

t = Solution()
print(t.spellchecker(["KiTe","kite","hare","Hare"],["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))