  
from heapq import heappop, heapify  
   
class Solution:
   def closest_k_points(self, points, K):   
      h = [[x**2 + y**2, x, y] for x,y in points]
      heapify(h)
      return [heappop(h)[1:] for _ in range(K)]
   
sol = Solution()
points = [[1,3],[-2,2]]
K = 1
print(sol.closest_k_points(points, K) == [[-2, 2]] )
            