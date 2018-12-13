class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack and not popped