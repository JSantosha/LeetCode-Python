class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxarea = 0
        top = 0
        right = 0
        left = 0
        bottom = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                top = 0
                right = 0
                left = 0
                bottom = 0
                if grid[i][j] != 0:
                    grid[i][j] = 0
                    if i - 1 >= 0:
                        top = self.dfsvisit(grid, i - 1, j)
                    if i + 1 < len(grid):
                        bottom = self.dfsvisit(grid, i + 1, j)
                    if j + 1 < len(grid[0]):
                        right = self.dfsvisit(grid, i, j + 1)
                    if j - 1 >= 0:
                        left = self.dfsvisit(grid, i, j - 1)

                    maxarea = max(maxarea, top + bottom + left + right + 1)
        return maxarea

    def dfsvisit(self, grid, x, y):
        value = 0
        top = 0
        right = 0
        left = 0
        bottom = 0
        if grid[x][y] != 0:
            grid[x][y] = 0
            if x - 1 >= 0:
                top = self.dfsvisit(grid, x - 1, y)
            if x + 1 < len(grid):
                bottom = self.dfsvisit(grid, x + 1, y)
            if y + 1 < len(grid[0]):
                right = self.dfsvisit(grid, x, y + 1)
            if y - 1 >= 0:
                left = self.dfsvisit(grid, x, y - 1)

            value += top + right + bottom + left + 1
        return value



