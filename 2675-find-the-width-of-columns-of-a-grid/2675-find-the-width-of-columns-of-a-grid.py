class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [0 for _ in range(n)]
        for r in grid:
            for j in range(n):
                ans[j] = max(ans[j], len(str(r[j])))
        return ans