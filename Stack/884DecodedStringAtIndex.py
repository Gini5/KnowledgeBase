class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        stack = []
        l = 0
        for c in S:
            l = l + 1 if c.isalpha() else l * int(c)
            stack.append(c)
            while l >= K:
                while stack[-1].isdigit(): l //= int(stack.pop())
                K %= l
                if not K: return stack[-1]
                l -= 1
                stack.pop()