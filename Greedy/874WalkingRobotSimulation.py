class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        i,j = 0,0
        move = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        res = 0
        obstacles = set(map(tuple,obstacles))
        for c in commands:
            if c == -1:
                d = (d+1)%4
            elif c == -2:
                d = (d+3)%4
            else:
                x,y = move[d][0], move[d][1]
                while c > 0 and (i+x,j+y) not in obstacles:
                    i += x
                    j += y
                    c -= 1
            res = max(res,i**2 + j**2)
        return res