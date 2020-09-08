"""
https://www.youtube.com/watch?v=aZXi1unBdJA
fidn articulations points in undirected graphs

"""
import collections
def find_articulation_points(n, connections):
    
        def find_art_point(v):
            if not art[v] and outdegree[v] > 1:
                art[v] = True
            
        def dfs(rank, curr, prev):
            low[curr] = rank
            for neighbor in graph[curr]:
                if neighbor == prev: continue
                if not low[neighbor]:
                    dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    find_art_point(curr)
                    find_art_point(neighbor)
                    
        graph = collections.defaultdict(list)
        low = [0] * n
        art  = [False]*n
        outdegree = {i:0 for i in range(n)}
        for u, v in connections:
            graph[u].append(v)
            outdegree[u] += 1
            graph[v].append(u)
            outdegree[v] += 1

        dfs(1, 0, -1)
        print(low)
        return [v for v,is_art in enumerate(art) if is_art]
        

connections = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
n = 7
print(find_articulation_points(n, connections))
  