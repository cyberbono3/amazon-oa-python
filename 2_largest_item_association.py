
import collections


def func(l):
    # largest outptu of topological ordering in a graph
    
    if not l :
        return l
    if len(l) == 1:
        return l
    
    def build_graph():
        for u,v in l:
            graph[u].add(v)
            graph[v].add(u)
            
    def dfs(v, output):
        stack = [v]
        while stack:
            curr = stack.pop()
            visited.add(curr)
            output.append(curr)
            for nei in graph[curr]:
                if nei not in visited:
                    stack.append(nei)
                   
        
    res = []
    graph = collections.defaultdict(set)
    build_graph()
    visited = set()
    for v in graph:
        if v not in visited:
            output = []
            dfs(v, output)
            output.sort()
            if not res or len(output) > len(res):
                res = output
            elif len(output)  == len(res):
                res = min(output,res)
    return res
        
print(func([]) == [])
print(func([['item1','item2']]) == ['item1','item2'])
print(func([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]) == ['item1','item2','item3'])
print(func([['Item1','Item2'],['Item3','Item4'],['Item4','Item5']]) == ['Item3', 'Item4', 'Item5'])
print(func([['Item1','Item2'],['Item2','Item5'],['Item3']]) == ['Item1', 'Item2', 'Item5'])
print(func([['Item1','Item2'],['Item2','Item3'],['Item4','Item5'],['Item5','Item6']]) == ['Item1', 'Item2', 'Item3'])
print(func([["Item1","Item2"], ["Item1","Item3"], ["Item2","Item7"], ["Item3","Item7"], ["Item5","Item6"], ["Item3","Item7"]]) == ['Item1', 'Item2', 'Item3', 'Item7'])
print(func([['Item1','Item2'],['Item1','Item3'],['Item2','Item7'],['Item3','Item7'],['Item5','Item6'],['Item3','Item7']]) == ['Item1', 'Item2', 'Item3', 'Item7'])
print(func([['Item3','Item2','Item4'], ['Item1', 'Item2'],['Item3', 'Item5', 'Item7'],['Item6','Item8']]) == ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item7'])