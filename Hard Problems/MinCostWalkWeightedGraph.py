from typing import List

class UnionFind:   # Defining the Union Find
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): # Connects x and y
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        uf = UnionFind(n) # Creating instance of the union find class
        
        # 1. Build the components
        for u,v,w in edges:
            uf.union(u,v)
        
        # 2. Get costs of each component
        component_cost = {} # root -> cost
        for u,v,w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w
        
        # 3. Process Queries
        res = []
        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:      # Edges are not connected
                res.append(-1)
            else:
                res.append(component_cost[r1])
        return res