class Solution:
    def spellchecker(self, wordlist, queries):
        answer = ["" for _ in range(len(queries))]
        original = {}
        capital = {}
        vowel = {}
        vocabs = {'a', 'e', 'i', 'o', 'u'}

        for i, w in enumerate(wordlist):
            if w not in original: original[w] = i
            lower = w.lower()
            if lower not in capital: capital[lower] = i
            tmp = set([lower])
            for index, char in enumerate(w):
                if char in vocabs:
                    for replace in vocabs:
                        news = set()
                        for word in tmp:
                            print(word)
                            new = word[:index] + replace + word[index + 1:]
                            news.add(new)
                            if new and new not in vowel: vowel[new] = i
                        tmp = tmp | news

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