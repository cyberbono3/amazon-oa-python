
import collections

class Solution:
    def __init__(self):
        self.duration = 0
    def solve_zombie_matrix(self, matrix):
        def find_zombies_humans():
            zombies, humans = [], []
            for r in range(R):
                for c in range(C):
                    if matrix[r][c] :
                        zombies.append((r,c))
                    else:
                        humans.append((r,c))
            return (zombies, humans)
            
        def neighbours(x, y):
            for nx,ny in ((x+1, y), (x-1, y), (x, y+1), (x,y-1)):
                if 0 <= nx < R and  0 <= ny < C and not matrix[nx][ny]:
                    yield (nx, ny)
            
            
        def bfs():
            q = collections.deque(zombies)
            while q:
                size = len(q)
                self.duration += 1
                for _ in range(size):
                    x,y = q.popleft()
                    for nx, ny in neighbours(x,y):
                        matrix[nx][ny] = 1
                        q.append((nx, ny))

    
                        
                             
        # address more edge cases
        if not matrix:
            return 0   
        R, C = len(matrix), len(matrix[0])
        zombies, humans = find_zombies_humans()  # list of tuple coordinatates
        if not zombies or not humans:
            return 0
        bfs()
        return 0 if any(not matrix[r][c] for (r,c) in humans) else self.duration - 1
            
        
matrix = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
sol = Solution()
print(sol.solve_zombie_matrix(matrix))
       
        

