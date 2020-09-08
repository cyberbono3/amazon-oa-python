class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        
        
        size = n**2
        
        [
        [ 0, 0, 0 ],
        [ 0, 0, 0 ],
        [ 0, 0, 0 ]
        ]
        
        top = 0 
        bottom = n -2
        

        matrix = [[0]*n for _ in range(n)]
        
        """
        matrix = [[0]*n for _ in range(n)]
        
        top = 0  # row
        bottom = n -1  # row
        left = 0 # col
        right = n -1 # col
    
        
        num = 1

        while left <= right and top <= bottom:
            
            for col in range(left, right+1):
                matrix[top][col] = num
                num += 1
            top += 1
           
            
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
           
            
            for col in range(right, left -1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            for row in range(bottom, top-1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
        return matrix
sol = Solution()

print(sol.generateMatrix(3) == [[1, 2, 3 ],[8, 9, 4 ],[7, 6, 5 ]])
