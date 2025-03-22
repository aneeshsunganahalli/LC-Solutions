from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(v, res): # DFS taking the vertex and an array that will store all nodes of component
            if v in visit:
                return
            visit.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei, res)
            return res

        adj = defaultdict(list)   # Builds the adjacent list for undirected graph
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        res = 0
        visit = set()
        for v in range(n):
            if v in visit:
                continue
            component = dfs(v, []) # Building the component

            flag = True
            for v2 in component:
                if len(component) - 1 != len(adj[v2]): # Condition for valid Component
                    flag = False
                    break
            if flag:
                res += 1
        return res