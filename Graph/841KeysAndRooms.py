class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        opened = [0] * n
        opened[0] = 1
        stack = [0]

        while stack:
            key = []
            for i in stack:
                for k in rooms[i]:
                    if opened[k] == 0:
                        key.append(k)
                        opened[k] = 1
            stack = key
        return not 0 in opened