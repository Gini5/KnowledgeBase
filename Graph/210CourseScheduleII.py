import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        col = collections.defaultdict(set)
        attended = [0] * numCourses
        res = []
        for p1, p2 in prerequisites:
            col[p1].add(p2)

        def dfs(course, visited=[]):
            if attended[course] != 1:
                for item in col[course]:
                    if item in visited: return 0
                    success = dfs(item, visited + [course])
                    if not success: return 0
                attended[course] = 1
                res.append(course)
                return 1
            else:
                return 1

        for course in range(numCourses):
            success = dfs(course)
            if not success: return []

        return res if len(res) == numCourses else []