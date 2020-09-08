class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        """
        
        def binary_search(row, left, right):
            while left <= right:
                mid = left + (right - left) // 2
                x = matrix[row][mid]
                print(left, right, mid , x)
                if x == target:
                    return True
                elif target > x:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
            
        

        if not matrix or not target:
            return False
        R, C = len(matrix), len(matrix[0])
        row, col = 0, C - 1
        while row < R :
            if target <= matrix[row][col] and binary_search(row, 0, col):
                    return True
            row += 1
        return False