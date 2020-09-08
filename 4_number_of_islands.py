class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Approach #1 DFS [Accepted]
        
        treat grid is undirectred graph and there is an edge fomed by adjacent nodes of value 1
        
        Linear scan the 2d grid map, 
        if a node contains a '1', then it is a root node that triggers a Depth First Search. 
        
        During  DFS, every visited node should be set as '0' to mark as visited node. Count the number of root nodes that trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.
        
        """
        def dfs(r, c):
            
            # check the boundaries or whilr grid[r][c] != 0
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == '0':
                return
            
            #check horizontally and vertically and mark each cell as visited (0)
            grid[r][c] = '0'
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        if not grid or not grid[0]:
            return 0
         # needed for checking boundaries
        R, C = len(grid), len(grid[0])
        count = 0 
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count += 1
                    # trigger DFS which will mark all ones as visited (zero)
                    dfs(r, c)
        
        return count
s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(grid) == 1)
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(s.numIslands(grid) == 3)
 
        