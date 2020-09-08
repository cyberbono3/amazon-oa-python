

# razobratjsja


class Solution:
    
    def max_min_path(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        self.matrix = matrix
        # self.l = len(matrix)

        self.maxp = 0
        self.takeStep(0, 0, float('inf'))

        return self.maxp

    def takeStep(self, n, m, minval):
        if n == len(self.matrix)-1 and m == len(self.matrix)-1:
            self.maxp = max(self.maxp, minval)
        if n < len(self.matrix) -1:

            self.takeStep(n+1, m, min(minval, self.matrix[n+1][m]))
        if m < len(self.matrix[0]) -1:
            self.takeStep(n , m + 1, min(minval, self.matrix[n][m + 1]))
        
        