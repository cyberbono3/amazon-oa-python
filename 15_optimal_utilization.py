"""

Given 2 lists a and b. 
Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements.
 If no pair is possible, return an empty list.

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

"""

import heapq

class Solution:
    def max_utilization(self, a, b):
        h = []
        count = 0
        for id1,val1 in a:
            for id2,val2 in b:
                s = val1 + val2
                if s < target:
                    heapq.heappush(h, (target - s, [id1,id2]) )
                elif s == target:
                    count += 1
                    heapq.heappush(h, (target - s, [id1,id2]) )
                    
        if not h:
            return []
        return [heapq.heappop(h)[1] for _ in range(count)] if count else [heapq.heappop(h)[1]]
      
sol = Solution()  
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
print(sol.max_utilization(a, b))



            
        