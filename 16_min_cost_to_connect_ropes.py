"""

https://leetcode.com/discuss/interview-question/344677

Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal to the sum of their lengths. This process is repeated until n ropes are connected into a single rope. Find the min possible cost required to connect all ropes.

Example 1:

Input: ropes = [8, 4, 6, 12]
Output: 58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58

"""

from heapq import heapify, heappop, heappush

class Solution:
    def min_cost_connect_ropes(self, ropes):
        heapify(ropes)
        
        min_cost = 0
        while len(ropes) > 1:
            cost1, cost2  = heappop(ropes), heappop(ropes)
            s = cost1 + cost2
            min_cost += s
            if ropes:
                heappush(ropes, s)
    
        
        return min_cost
            
        
    

ropes = [8, 4, 6, 12]   
sol = Solution()
print(sol.min_cost_connect_ropes(ropes))

    
