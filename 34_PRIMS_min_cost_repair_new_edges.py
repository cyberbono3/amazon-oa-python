
# https://leetcode.com/discuss/interview-question/357310

from collections import defaultdict

from heapq import heapify, heappush, heappop

class Solution:
    def minCostConnectRepairNewEdges(self, n, edges, repair_edges):
        def buildGraph():
            repair_set = set()
            for u,v,c in repair_edges:
                repair_set.add((u,v))
                repair_set.add((v,u))
                graph[u].append((v,c))
                graph[v].append((u,c))
            
            for u,v in edges:
                if (u,v) in repair_set: continue
                graph[u].append((v,0))
                graph[v].append((u,0))
                
        graph = defaultdict(list)
        buildGraph()
        
        h = [(0, 1)]
        heapify(h)
        dist = {}
        while h:
            min_cost, v = heappop(h)
            if v in dist: continue
            dist[v] = min_cost
            for u,c in graph[v]:
                heappush(h, (c, u))
        return sum(dist.values())
sol = Solution()
print(sol.minCostConnectRepairNewEdges(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]) == 20 )
print(sol.minCostConnectRepairNewEdges(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]])== 410 )

