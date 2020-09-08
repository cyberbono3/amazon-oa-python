from collections import deque 

class Solution:
    shortest_path = 0
    def shortest_path_to_treasure(self, matrix):
        # if no X in matrix return 0
        # if no O in matyrix return 0
        
        def neighbours(r,c):
            for (nr,nc) in ((r+1,c), (r-1, c), (r,c+1), (r,c-1)):
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] != "D" and matrix[nr][nc] != "S":
                    yield (nr,nc)
                    
        def find_start_vertices():
            start_vertices = []
            for r in range(R):
                for c in range(C):
                    if matrix[r][c] == "S":
                        start_vertices.append((r,c))      
            return start_vertices
        
         
        def bfs():
            q = deque(start_vertices)
            while q:
                size = len(q)
                Solution.shortest_path += 1
                for _ in range(size):
                    r, c = q.popleft()
                    for nr,nc in neighbours(r,c):
                        if matrix[nr][nc] == "X":
                            return Solution.shortest_path
                        matrix[nr][nc] = "S"
                        q.append((nr, nc))   
        if not matrix :
            return 0
        R, C = len(matrix), len(matrix[0])
        start_vertices  = find_start_vertices()
        if not start_vertices:
            return 0
        return bfs()
        
        
           
sol = Solution()
matrix = [['S', 'O', 'O', 'S', 'S'],['D', 'O', 'D', 'O', 'D'],['O', 'O', 'O', 'O', 'X'],['X', 'D', 'D', 'O', 'O'],['X', 'D', 'D', 'D', 'O']]
print(sol.shortest_path_to_treasure(matrix))

