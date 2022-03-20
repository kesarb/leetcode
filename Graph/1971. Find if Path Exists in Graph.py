"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        g = {}
        for e1,e2 in edges:
            if e1 not in g:
                g[e1] = []
            g[e1].append(e2)
            if e2 not in g:
                g[e2] = []
            g[e2].append(e1)
            
        self.visit = {}
        #print(g)
        def dfs(curr, dest):
            
            if curr in self.visit:
                return 0
            
            if curr == dest:
                return 1
            self.visit[curr] = 1
            #print(curr)
            for i in g[curr]:
                if i not in self.visit:
                    if dfs(i, dest):
                        #print("Anser")
                        return 1
            self.visit[curr] = 0
            return 0

        return dfs(source, destination)
