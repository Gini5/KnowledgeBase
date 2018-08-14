class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        visited = [[r0,c0]]
        n,i = 0,0   #n means move how many steps before turn right, i means how many steps have made
        x,y = 0,1
        while len(visited)<R*C:
            r0, c0, i = r0 + x, c0 + y, i + 1
            if 0 <= r0 < R and 0 <= c0 < C:
                visited.append([r0, c0])
            if i == n//2+1:
                #turn right
                x, y, n, i = y, -x, n+1, 0
        return visited