from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or not grid[r][c]:
                return 0

            visit.add((r, c))
            res = 1
            dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dir:
                res += dfs(r + dr, c + dc)

            return res

        visit = set()
        land = 0
        borderland = 0
        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] and (r, c) not in visit and
                        (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                    borderland += dfs(r, c)

        return land - borderland

