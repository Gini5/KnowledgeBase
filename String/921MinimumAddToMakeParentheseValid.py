class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(': stack.pop()
                else: stack.append(c)
        return len(stack)