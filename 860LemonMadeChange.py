class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        if n == 0: return True
        cnt = {5:0,10:0,20:0}
        for item in bills:
            if item == 5: cnt[item] += 1
            elif item == 10:
                if cnt[5] < 1: return False
                cnt[10] += 1
                cnt[5] -= 1
            else:
                if cnt[5]<1 or cnt[10]<1 and cnt[5]<3: return False
                cnt[20] += 1
                if cnt[10]<1: cnt[5] -= 3
                else:
                    cnt[5] -= 1
                    cnt[10] -=1
        return True