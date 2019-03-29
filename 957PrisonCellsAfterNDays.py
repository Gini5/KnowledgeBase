class Solution:
    def prisonAfterNDays(self, cells, N):
        visited = []
        while N > 0:
            tmp = [0 for _ in range(8)]
            for i in range(8):
                if i == 0 or i == 7: continue
                tmp[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            if tmp in visited:
                return visited[N % len(visited) - 1]
            else:
                visited.append(tmp)
                cells = tmp
                N -= 1
        return cells