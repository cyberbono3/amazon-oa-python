"""

find bridges in a graph



"""

import collections

class Solution:
    def criticalConnections(self, n, connections) :
        def dfs(rank, curr, prev):
            low[curr], result = rank, []
            for neighbor in graph[curr]:
                if neighbor == prev: continue
                if not low[neighbor]:
                    result += dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    result.append([curr, neighbor])
            print(low)
            return result

        low, graph = [0] * (n+1), collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        return dfs(1, 1, 1)
        
        
        
        
sol = Solution()

print(sol.criticalConnections(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))
print(sol.criticalConnections(6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]))
print(sol.criticalConnections(9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]))



    