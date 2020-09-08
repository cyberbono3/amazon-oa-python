"""

leetcode problem
https://leetcode.com/problems/critical-connections-in-a-network/

find bridges


"""

import collections

def criticalConnections(n, connections):
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

connections = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
n = 5
print(criticalConnections(n, connections))