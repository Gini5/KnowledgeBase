class Solution:
    def bagOfTokensScore(self, tokens: 'List[int]', P: 'int') -> 'int':
        cur, res = 0, 0
        tokens.sort()
        while tokens and (P>=tokens[0] or cur):
            if P>=tokens[0]:
                P -= tokens[0]
                tokens.pop(0)
                cur += 1
            else:
                P += tokens[-1]
                tokens.pop(-1)
                cur -= 1
            res = max(res,cur)
        return res