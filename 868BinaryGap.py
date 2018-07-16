class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)
        res = 0
        i = 2
        while i < len(binary):
            if binary[i] == '1':
                j = i+1
                while j < len(binary) and binary[j] != '1':
                    j += 1
                if j<len(binary): res = max(res,j-i)
                i = j
            else:
                i += 1
        return res