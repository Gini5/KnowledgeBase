class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i,j = 0,0
        while j<len(typed):
            if i<len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j>0 and typed[j] == typed[j-1]:
                    j += 1
                else:
                    return False
        return i == len(name)