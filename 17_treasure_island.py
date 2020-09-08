"""

"""

from collections import deque 

class Solution:
    def shortest_path_to_treasure(self, matrix):
        if not matrix:
            return 0
        # if no X in matrix return 0
        # if no O in matyrix return 0
        
        def neighbours(r,c):
            for (nr,nc) in ((r+1,c), (r-1, c), (r,c+1), (r,c-1)):
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] != "D" and matrix[nr][nc] != "-1":
                    yield (nr,nc)
                    
        def find_treasure():
            tr,tc = -1,-1
            for r in range(R):
                for c in range(C):
                    if matrix[r][c] == "X":
                        tr,tc = r,c
                        break
            return (tr,tc)
                
        R, C = len(matrix), len(matrix[0])
        tr,tc = find_treasure()
        if tr == -1 and tc == -1:
            return 0
        
        q = deque([(0,0,0)])
        matrix[0][0] = "-1"
        while q:
            r, c, path = q.popleft()
            if r == tr and c == tc:
                return path
            for nr,nc in neighbours(r,c):
                matrix[nr][nc] = "-1"
                q.append((nr, nc, path+1))   
        return 0
            
            
            

sol = Solution()
matrix = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'],['X', 'D', 'D', 'O']]
print(sol.shortest_path_to_treasure(matrix))
print(matrix)



